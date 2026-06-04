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