#!/usr/bin/env python3

import sys
import requests
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT


def get_lienages_by_lineage_system(lineage_system_name: str = "PANGO") -> dict:
    url = f"{OUTBREAK_API_BASE}/lineages" # 'http://localhost:8005/lineages?lineage_system_name=PANGO'
    response = requests.get(url, params={"lineage_system_name": lineage_system_name}, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()

def get_mutation_profile_by_lineage(
        lineage_name: str = "BA.1",
        lineage_system_name: str = "PANGO"
) -> dict: 
    url = f"{OUTBREAK_API_BASE}/v0/lineages:mutationProfile" # http://172.29.32.104:8005/v0/lineages:mutationProfile?lineage=BA.1&lineage_system_name=PANGO
    response = requests.get(
        url=url, 
        params={"lineage": lineage_name, "lineage_system_name": lineage_system_name}, 
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()
