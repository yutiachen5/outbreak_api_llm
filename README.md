# Outbreak.info AI Agent

An AI agent to pull data from Outbreak.info API.

## Setup

1. Create a `.env` file in the project root with the following variables:
```
    TOGETHER_API_KEY=your_key_here
    OUTBREAK_API_BASE=api_address
    LLM_MODEL=model_name_from_together_ai
```
We now use the LLM from [together.ai](https://api.together.ai/models)

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Install and activate Pi:
```
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
/login
export TOGETHER_API_KEY=your_key_here
pi
/model and select google/gemma-4-31B-it
/quit
```

## Usage

We use the [skills](https://pi.dev/docs/latest/skills) from pi-agent to handle the harness. To pull the data from api, simply ask the agent in natural language like "Get me the delta_bind phenotype metrics for mutations aggregated by sample and collection date". The agent will choose the skill automatically.

If the agent fails to pick the right skill automatically, you can:

1. Give a hint: "Use the outbreak API fetch_lineages skills to get..."
2. Force it: /skill:fetch_lineages get_mutation_profile_by_lineage BA.1 PANGO 
3. Improve the skill description in SKILL.md to make the trigger more obvious.  

Example questions:

1. Give me the total number of lineages in usda genoflu/pango system (depending on which api you are connecting to).
2. Give me the mutation profile of lineage BA.1 (sc2) or D1,1 (flu).
3. Fetch annotation papers for the effect 'Enhanced replication in ferrets' by month.
4. fetch me the most selective amino acid mutation i.e the aa mutation with the highest binding score using metric sa26_usage_increase_new, in Jan of 2022
