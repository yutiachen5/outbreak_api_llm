---
name: fetch-mutations
description: Retrieves mutation data from the outbreak API.
---

## Fetch Mutation Frequency Scores by Region and Metric

Retrieve mutation frequency scores by region and metric.

Pass `--visualize` to save a scatter chart to `--output_path`.

```bash
python ./.pi/skills/fetch-mutations/main.py get_mutation_frequency_score \
  --region XAJ25415.1 \
  --metric sa26_usage_increase_new \
  --visualize \
  --output_path mutation_frequency_score.png \
  --export_csv \
  --csv_output_path mutation_data.csv
```

## Example Prompts
- "Retrieve mutation frequency scores for the region XAJ25415.1 and metric sa26_usage_increase_new without visualization."
- "Show me mutation frequency scores for the region XAJ25415.1 and metric sa26_usage_increase_new, and visualize the results"
- "Get mutation frequency scores for region XAJ25415.1 with metric sa26_usage_increase_new."
- "Visualize mutation frequency scores for XAJ25415.1"
- "Get me the DMS scores for mutations in region XAJ25415.1"
- "Export mutation frequency scores for region XAJ25415.1 and metric sa26_usage_increase_new to a CSV file."