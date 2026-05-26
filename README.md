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
```

## Usage

We use the [skillS](https://pi.dev/docs/latest/skills) from pi-agent to handle the harness. To pull the data from api, call
```
 /skill:skill_name tool_name arg1 arg2 

 /skill:fetch_lineages get_mutation_profile_by_lineage BA.1 PANGO 
```
