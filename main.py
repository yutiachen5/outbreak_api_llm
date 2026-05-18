import argparse

from agent import LLM_Agent


def main():
    parser = argparse.ArgumentParser(description="AI agent to get response from Outbreak.info API.")
    parser.add_argument("--verbose", default=True, help="Verbose mode")
    parser.add_argument("--save_response", default=True, help="Save API response or not")
    parser.add_argument("--output", default="mutations.tsv", help="The path to save API response")

    args = parser.parse_args()

    print("Outbreak Lineage Assistant")
    print("=" * 40)

    agent = LLM_Agent(args)

    while True: # loop for follow-up questions
        user_query = input("User input: ")
        if user_query.lower() in ("exit", "quit"):
            break
        answer = agent.run_agent(user_query)
        print("\nAssistant:", answer)

if __name__ == "__main__":
    main()

