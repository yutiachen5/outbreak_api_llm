---
name: fetch-pheno-metrics
description: Retrieves phenotype metrics data from the outbreak API.
---

## Fetch Phenotype Metrics

Retrieve all phenotype metrics and their assay types

```bash
python ./.pi/skills/fetch-pheno-metrics/main.py get_phenotype_metrics 
```

## Fetch Min and Max Values for a Phenotype Metric

Retrieve the minimum and maximum values for a given phenotype metric. This should only be used when the user asks for visualization.

```bash
python ./.pi/skills/fetch-pheno-metrics/main.py get_phenotype_metric_min_max \
  --phenotype_metric_name sa26_usage_increase_new
```
