---
name: fetch-variants
description: Retrieves variant data from the outbreak API.
---

## Fetch Variant Frequency Scores by Region and Metric

Retrieve variant frequency scores by region and metric.

```bash
python ./.pi/skills/fetch-variants/main.py get_variant_frequency_score \
  --region XAJ25415.1 \
  --metric sa26_usage_increase_new
```

## Fetch Mutation Lag by Lineage and Lineage System

Retrieve mutation lag by lineage and lineage system.

```bash
  python ./.pi/skills/fetch-variants/main.py get_mutation_lag_by_lineage \
    --lineage B3.13 \
    --lineage_system_name usda_genoflu
```

## Example Prompts
- "Retrieve variant frequency scores for the region XAJ25415.1 and metric sa26_usage_increase_new."
- "Get mutation lag for the lineage B3.13 using the usda_genoflu lineage system."
- "Show me the variant frequency scores for region XAJ25415.1 with metric sa26_usage_increase_new."
- "What is the mutation lag for lineage D1.1?"
- "Get variant frequency scores for HA region"
- "How long does it take for mutations to appear in lineage B3.13?"