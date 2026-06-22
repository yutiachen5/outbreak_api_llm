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
python ./.pi/skills/fetch-lineage/main.py get_mutation_incidence_by_lineage \
  --lineage D1.1 \
  --lineage_system_name usda_genoflu \
  --prevalence_threshold 0.75 \
  --change_bin aa
```