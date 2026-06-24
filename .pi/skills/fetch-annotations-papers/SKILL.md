**Important: Always run the python command directly to fetch fresh data. Never read from existing JSON response files.**
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
  --day 5 \
  --max_span_days 31
```

`--effect_detail` is a plain string with spaces

## Fetch Annotation Effects
Retrieve annotation effects

```bash
python ./.pi/skills/fetch-annotations-papers/main.py get_annotation_effects \
```

## Fetch Annotations by Effect Detail
Retrieve annotions with mutation and aa position data by effect detail

```bash
python ./.pi/skills/fetch-annotations-papers/main.py get_annotations_by_effect_detail \
  --effect_detail Increased%20virus%20binding%20to%20α2-6
```
