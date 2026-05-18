# Outbreak.info AI Agent

A natural language interface for the Outbreak.info API. Ask questions about viral lineages and phenotype metrics in plain English and get interpreted answers.

## Setup

1. Create a `.env` file in the project root with the following variables:
```
    TOGETHER_API_KEY=your_key_here
    OUTBREAK_API_BASE=api_address
    LLM_MODEL=model_name_from_together_ai
```
We now use the LLM from [together.ai](https://api.together.ai/models)

2. Install dependencies:
```bash
    pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The agent will prompt for input and support multi-turn conversations. Type `exit` or `quit` to stop.

## Example Questions

1. Give me the total number of lineages in the PANGO lineage system.
2. What is the month with the highest binding score with respect to reference BA.2 in the RBD region?