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
The region here should be a gene region (gff feature) not a geopraphic location.
mapping between segment and phenotype metric
HA - entry_in_293t_cells, stability, sa26_usage_increase, sa26_usage_increase_new, mature_h5_site, ferret_sera_escape, mouse_sera_escape, entry_in_sa26_and_sa23_293t_cells, evescape, evescape_sigmoid
PB2 - mutdiffsel


## Fetch Region(Segment) and GFF Feature

Retrieve the mapping one-to-one mapping dictionary between gff feature and region(segment). No input parameter is needed.

```bash
python ./.pi/skills/fetch-mutations/main.py get_region_and_gff
```

## Fetch Mutation by Sample Query

Fetch mutations using individual filter parameters or a custom query string for country, time period, state, and host.

```bash
python ./.pi/skills/fetch-mutations/main.py get_mutation_by_sample -q "host=United%20States" 
```
When you want to write the filter query for q, always look up the schema of SampleInfo to decide which column to use.
Common filters: country (country_name), time (collection_start_date/collection_end_date), state (admin1_name), host (cattle, chicken, etc)