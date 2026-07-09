---
name: fetch-lineages
description: Retrieves strain lineage data from the outbreak API.
---

## Fetch Lineages

Retrieve all lineages for a given classification system (default: usda_genoflu).

```bash
python ./.pi/skills/fetch-lineages/main.py get_lineages_by_lineage_system \
  --lineage_system_name usda_genoflu
```

## Fetch Mutation Profile by Lineage and Lineage System

Retrieve mutation profile (region, ref_nt, alt_nt, and count) for a given lineage and lineage system.

```bash
python ./.pi/skills/fetch-lineages/main.py get_mutation_profile_by_lineage \
  --lineage_name D.1.3 \
  --lineage_system_name usda_genoflu
```

## Fetch Mutation Incidence by Lineage and Lineage System

Retrieve mutation incidence for a given lineage and lineage system
Use change_bin='aa' for amino acid changes or 'nt' for nucleotide changes 

```bash
python ./.pi/skills/fetch-lineages/main.py get_mutation_incidence_by_lineage \
  --lineage D1.1 \
  --lineage_system_name usda_genoflu \
  --prevalence_threshold 0.75 \
  --change_bin aa
```

## Fetch Lineage Counts

Retrieve lineage counts grouped by `--group_by`. Behavior depends on the value of `--group_by`:

- **No `--group_by`** (default): returns per-lineage sample counts filtered by `--lineage_system_name`.
- **`--group_by collection_date`**: returns counts binned by collection date; uses `--date_bin`, `--days`, and `--max_span_days`.
- **`--group_by <other date field>`** (e.g. `submission_date`): returns counts binned by that date field; uses `--date_bin` and `--days`.

`--date_bin` accepts: `month` (default), `week`, or `day`.

Pass `--visualize` to save a bar chart to `--output_path` (only applies when the response is per-lineage counts).

```bash
# Per-lineage sample counts (with visualization)
python ./.pi/skills/fetch-lineages/main.py get_lineage_count \
  --lineage_system_name usda_genoflu \
  --visualize \
  --output_path lineage_sample_count.png

# Counts grouped by collection date
python ./.pi/skills/fetch-lineages/main.py get_lineage_count \
  --group_by collection_date \
  --date_bin month \
  --days 90 \
  --max_span_days 30

# Counts grouped by another date field
python ./.pi/skills/fetch-lineages/main.py get_lineage_count \
  --group_by submission_date \
  --date_bin week \
  --days 30
```
## Example Prompts
- "Get mutation incidence for lineage D1.1"
- "Retrieve all lineages for the usda_genoflu classification system."
- "Get the mutation profile for lineage D.1.3 using the usda_genoflu lineage system."
- "Fetch mutation incidence for lineage D1.1 with a prevalence threshold of 0.75 and amino acid changes."
- "Get lineage counts grouped by collection date, binned by month, starting from day"
- "Show me a bar chart of lineage sample counts for usda_genoflu."
- "What lineages are in the pango system?"
- "Get mutation incidence for B3.13 and visualize it."
- "Get lineage counts grouped by collection date, binned by month, starting from day 5 with a max spam of 30 days."