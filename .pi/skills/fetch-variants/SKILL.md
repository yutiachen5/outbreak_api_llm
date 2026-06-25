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

