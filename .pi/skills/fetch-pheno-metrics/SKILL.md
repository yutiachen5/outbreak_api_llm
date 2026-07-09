---
name: fetch-pheno-metrics
description: Retrieves phenotype metrics data from the outbreak API.
---

## Fetch Phenotype Metrics

Retrieve all phenotype metrics and their assay types

```bash
python ./.pi/skills/fetch-pheno-metrics/main.py get_phenotype_metrics 
```


## Fetch Aggregated Phenotype Metrics Values for Mutations by Sample and Collection Date

Retrieve aggregated phenotype metric values for mutations by sample and collection date.

```bash
python ./.pi/skills/fetch-pheno-metrics/main.py get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date \
  --phenotype_metric_name delta_bind \
  --lineage_system_name PANGO \
  --background NC_045512.2_BA.1_rbd \
  --date_bin month \
  --day 5 \
  --max_span_days 366
```

`--background` is optional — omit it if the user does not specify on e, use the format like NC_045512.2, NC_045512.2_BA.1_rbd, and NC_045512.2_BA.2_rbd
`--date_bin` accepts: `month` (default), `week`, or `year`.


## Fetch Min and Max Values for a Phenotype Metric

Retrieve the minimum and maximum values for a given phenotype metric.

```bash
python ./.pi/skills/fetch-pheno-metrics/main.py get_phenotype_metric_min_max \
  --phenotype_metric_name sa26_usage_increase_new
```

## Example Prompts
- "Retrieve all phenotype metrics and their assay types."
- "Get aggregated phenotype metric values for the mutation D614G, using the delta_bind metric"
- "Fetch aggregated phenotype metric values for the mutation D614G, using the delta_bind metric, grouped by month, starting from day 5, with a maximum span of 366 days."
- "Get the minimum and maximum values for the phenotype metric sa26_usage_increase_new."
- "What phenotype metrics are available?"
- "What is the range of values for sa26_usage_increase_new?"