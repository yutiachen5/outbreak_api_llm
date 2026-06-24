#!/usr/bin/env python3

import sys
import requests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT

def get_variant_frequency_score(
        region: str,
        metric: str
) -> dict:
    url = f"{OUTBREAK_API_BASE}/variants/frequency/score" #https://h5n1.outbreak.info/api/variants/frequency/score?region=XAJ25415.1&metric=sa26_usage_increase_new
    response = requests.get(
        url = url,
        params={"region": region, "metric": metric},
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json(
)

def get_mutation_lag_by_lineage(
        lineage: str,
        lineage_system_name: str
) -> dict:
    url = f"{OUTBREAK_API_BASE}/variants:mutationLag" #https://h5n1.outbreak.info/api/variants:mutationLag?lineage=B3.13&lineage_system_name=usda_genoflu
    response = requests.get(
        url= url,
        params = {"lineage": lineage, "lineage_system_name" : lineage_system_name},
        timeout= API_REQUEST_TIMEOUT
    )
    response.raise_for_status
    return response.json()