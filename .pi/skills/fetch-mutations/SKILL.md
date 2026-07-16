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
mapping between segment and phenotype metric
HA - entry_in_293t_cells, stability, sa26_usage_increase, sa26_usage_increase_new, mature_h5_site, ferret_sera_escape, mouse_sera_escape, entry_in_sa26_and_sa23_293t_cells, evescape, evescape_sigmoid
PB2 - mutdiffsel


## Fetch Region(Segment) and GFF Feature

Retrieve the mapping one-to-one mapping dictionary between gff feature and region(segment). No input parameter is needed.

```bash
python ./.pi/skills/fetch-mutations/main.py get_region_and_gff
```

## Fetch Mutation by Sample Query
Fetch mutations that exist in samples where (user query). This should be used when the user is asking for the mutation in a certain time period or host level or geolocation.... Some common column names to use:

time - collection_start_date/collection_end_date 
country - country_name
state - admin1_name
host - host

```bash
python ./.pi/skills/fetch-mutations/main.py get_mutation_by_sample \
  -q "collection_start_date%3E%3D2024-01-01%5Ecollection_start_date%3C%3D2024-12-31"
```


