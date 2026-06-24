**Important: Always run the python command directly to fetch fresh data. Never read from existing JSON response files.**
---
name: fetch-mutations
description: Retrieves mutation data from the outbreak API.
---

## Fetch Mutation Frequency Scores by Region and Metric

Retrieve mutation frequency scores by region and metric.

```bash
python ./.pi/skills/fetch-mutations/main.py get_mutation_frequency_score \
  --region XAJ25415.1 \
  --metric sa26_usage_increase_new
```

