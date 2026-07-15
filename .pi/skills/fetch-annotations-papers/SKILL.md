---
name: fetch-annotations-papers
description: Retrieves annotation papers from the outbreak API.
---

## Fetch Annotation Papers by Mutation and Collection Date

Retrieve annotated papers by mutation and collection date.

```bash
python ./.pi/skills/fetch-annotations-papers/main.py get_annotation_papers_by_mutation_and_collection_date \
  --effect_detail "Enhanced replication in ferrets" \
  --date_bin month \
  --days 5 \
  --max_span_days 31 \
  --visualize
```

`--effect_detail` is a plain string with spaces
`--visualize` is optional and will generate side-by-side proportion and count charts

## Fetch Annotation Effects
Retrieve annotation effects

```bash
python ./.pi/skills/fetch-annotations-papers/main.py get_annotation_effects 
```

## Fetch Annotations by Effect Detail
Retrieve annotions with mutation and aa position data by effect detail

```bash
python ./.pi/skills/fetch-annotations-papers/main.py get_annotations_by_effect_detail \
  --effect_detail "Increased virus binding to α2-6" \
  --segment HA \
  --visualize
```

`--effect_detail` is required
`--segment` is optional(default: HA)
`--visualize` is optional and will generate a bar chart by amino acid position

## Example Prompts
- "Fetch annotation papers for the mutation XAJ25415.1 with the effect detail 'Enhanced replication in ferrets' and group the results by month, starting from day 5, with a maximum span of 31 days."
- "Retrieve all annotation effects available in the outbreak API."
- "Get annotations for the effect detail 'Increased virus binding to α2-6' and include mutation and amino acid position data."
- "What annotation effects are available?"
- "Show me the annotation for enhanced replication in ferrets."
- "Get me annotations by effect detail for increased virus binding."
- "Visualize increased virus binding to α2-6 by amino acid position."
- "Show me mutations by position for the effect detail 'Increased virus binding to α2-6' and visualize the results."
- "What's the trend in unique mutations annotated with Enhanced replication in ferrets from 2022 to 2026?"