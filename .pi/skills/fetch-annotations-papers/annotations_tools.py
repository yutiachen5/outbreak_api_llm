#!/usr/bin/env python3

import sys
import requests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT


def get_annotation_papers_by_mutation_and_collection_date(
    effect_detail: str,
    date_bin: str = "month",
    days: int = 5,
    max_span_days: int = 31,
) -> dict:
    # https://h5n1.outbreak.info/api/v0/annotations:byMutationsAndCollectionDate?effect_detail=Enhanced%20replication%20in%20ferrets&date_bin=month&days=5&max_span_days=31
    url = f"{OUTBREAK_API_BASE}/v0/annotations:byMutationsAndCollectionDate"

    params={
        "effect_detail": effect_detail,
        "date_bin": date_bin,
        "days": days,
        "max_span_days": max_span_days,
    }
    
    response = requests.get(url, params=params, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()

def get_annotation_effects() -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/annotationEffects" #https://h5n1.outbreak.info/api/v0/annotationEffects
    response = requests.get(
        url = url,
        timeout= API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()

def get_annotations_by_effect_detail(
        effect_detail: str
) -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/annotations:byMutationsAndAminoAcidPosition" #https://h5n1.outbreak.info/api/v0/annotations:byMutationsAndAminoAcidPosition?effect_detail=Increased%20virus%20binding%20to%20%CE%B12-6
    response = requests.get(
        url=url,
        params = {"effect_detail": effect_detail},
        timeout = API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()