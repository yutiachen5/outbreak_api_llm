#!/usr/bin/env python3

import sys
import requests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT

def get_phenotype_metrics() -> dict:
    url = f"{OUTBREAK_API_BASE}/phenotype_metrics" #https://h5n1.outbreak.info/api/phenotype_metrics
    response = requests.get(
        url=url,
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()


def get_phenotype_metric_min_max(
        phenotype_metric_name: str
) -> list:
    url = f"{OUTBREAK_API_BASE}/v0/phenotype_metric_values:getMinAndMaxValues" #https://h5n1.outbreak.info/api/v0/phenotype_metric_values:getMinAndMaxValues?phenotype_metric_name=sa26_usage_increase_new\

    params ={
        "phenotype_metric_name": phenotype_metric_name
    }
    
    response = requests.get(url, params=params, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()