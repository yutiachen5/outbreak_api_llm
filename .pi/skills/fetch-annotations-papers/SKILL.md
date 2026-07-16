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