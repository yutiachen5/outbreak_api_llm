import os
import json
import requests
from datetime import datetime
from together import Together

from config import LLM_MODEL, TOGETHER_API_KEY, SYSTEM_PROMPT,\
      LLM_PER_REQUEST_TIMEOUT, LLM_TIMEOUT
from tools import TOOL_MAP
from schemas import TOOL_SCHEMAS


class LLM_Agent():
    def __init__(self, args):
        self.verbose = args.verbose
        self.save_response = args.save_response
        self.client = Together(api_key=TOGETHER_API_KEY, timeout=LLM_TIMEOUT)
        self.messages = []

    def save_result(self, result: dict):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"response_{timestamp}.json", "w") as f:
            json.dump(result, f, indent=2)

    def run_agent(self, user_message: str) -> str:
        result = None
        self.messages.extend([{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user_message},])

        while True:
            response = self.client.chat.completions.create(
                model=LLM_MODEL,
                messages=self.messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto",
                timeout=LLM_PER_REQUEST_TIMEOUT,
            )

            choice = response.choices[0] # the first response from LLM, contains:
            # Choice(finish_reason=, index=, message=ChoiceMessage(content=, role=, function_call=, reasoning=, tool_calls=[ToolChoice(id=, function=Function(arguments=, name=), index=, type=)]), ...)

            if choice.finish_reason == "tool_calls":
                self.messages.append(choice.message)

                for tool_call in choice.message.tool_calls: # LLM decidese which tool to use
                    fn_name = tool_call.function.name # fetch_lineage
                    fn_args = json.loads(tool_call.function.arguments) # LLM will extract the parameters from user input and overwirte the default ones

                    if self.verbose:
                        print(f"[tool call] {fn_name}({fn_args})")

                    if fn_name not in TOOL_MAP:
                        result = {"error": f"Unknown tool: {fn_name}"} 
                    else:
                        try:
                            result = TOOL_MAP[fn_name](fn_args) # result - raw data in json format
                        except requests.ConnectionError:
                            result = {"error": "Outbreak API is not reachable at localhost:8003"}
                        except requests.HTTPError as e:
                            result = {"error": str(e)}

                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(result), # human readable content summarized by LLM
                    }) # grow each interation
            else:
                if self.save_response and result: # only save res when it's not empty
                    self.save_result(result)
                return choice.message.content 





