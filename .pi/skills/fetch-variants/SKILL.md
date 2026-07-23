---
name: fetch-variants
description: Retrieves variant data from the outbreak API.
---

## Host-level Data

This skill retrieves host-level variant data. Use this when the user asks for host-level variants, intra-host variants, or data from specific hosts (as opposed to population-level mutations).

## Fetch Variant Frequency Scores by Region and Metric

Retrieve variant frequency scores by region and metric.

```bash
python ./.pi/skills/fetch-variants/main.py get_variant_frequency_score \
  --region XAJ25415.1 \
  --metric sa26_usage_increase_new
```
The region here should be a gene region (gff feature) not a geopraphic location.
mapping between region/segment and phenotype metric:
HA - entry_in_293t_cells, stability, sa26_usage_increase, sa26_usage_increase_new, mature_h5_site, ferret_sera_escape, mouse_sera_escape, entry_in_sa26_and_sa23_293t_cells, evescape, evescape_sigmoid
PB2 - mutdiffsel

## Fetch Mutation Lag by Lineage and Lineage System

Retrieve mutation lag by lineage and lineage system.

```bash
  python ./.pi/skills/fetch-variants/main.py get_mutation_lag_by_lineage \
    --lineage B3.13 \
    --lineage_system_name usda_genoflu
```
