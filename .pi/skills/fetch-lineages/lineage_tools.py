#!/usr/bin/env python3
import sys
import requests
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT


def get_lineages_by_lineage_system(lineage_system_name: str = "usda_genoflu") -> dict:
    url = f"{OUTBREAK_API_BASE}/lineages" # https://h5n1.outbreak.info/api/lineages?lineage_system_name=usda_genoflu
    response = requests.get(url, params={"lineage_system_name": lineage_system_name}, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()

def get_mutation_profile_by_lineage(
        lineage_name: str = "D1.3",
        lineage_system_name: str = "usda_genoflu"
) -> dict: 
    url = f"{OUTBREAK_API_BASE}/v0/lineages:mutationProfile" # https://h5n1.outbreak.info/api/v0/lineages:mutationProfile?lineage=D1.3&lineage_system_name=usda_genoflu
    response = requests.get(
        url=url, 
        params={"lineage": lineage_name, "lineage_system_name": lineage_system_name}, 
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()

def get_mutation_incidence_by_lineage(
        lineage, 
        prevalence_threshold= 0.75,
        change_bin: str= "aa",
        lineage_system_name: str = "usda_genoflu"
) -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/lineages:mutationIncidence" #https://h5n1.outbreak.info/api/v0/lineages:mutationIncidence?lineage=D1.1&change_bin=aa&lineage_system_name=usda_genoflu&prevalence_threshold=0.75
    response = requests.get(
        url = url,
        params={"lineage":lineage, "change_bin":change_bin, "lineage_system_name":lineage_system_name, "prevalence_threshold":prevalence_threshold},
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()

def get_lineage_count(
        group_by: str | None = None,
        date_bin: str = "month",
        days: int = 5,
        q: str | None = None,
        max_span_days: int = 30,
        lineage_system_name: str = "usda_genoflu",
        visualize: bool = False,
        output_path: str | None = "lineage_sample_count.png",
) -> dict | list:
    url = f"{OUTBREAK_API_BASE}/v0/lineages:count"
    params = {"date_bin": date_bin, "days": days, "max_span_days": max_span_days, "lineage_system_name": lineage_system_name}
    if group_by is not None:
        params["group_by"] = group_by
    if q is not None:
        params["q"] = q
    response = requests.get(url=url, params=params, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()

    if isinstance(data, list) and visualize and output_path is not None:
        filtered = [item for item in data if item.get("lineage_system") == lineage_system_name]
        lineages = [item["lineage"] for item in filtered]
        counts = [item["count"] for item in filtered]
        plt.figure(figsize=(15, 6))
        plt.bar(lineages, counts)
        plt.xlabel("Lineage")
        plt.ylabel("Count")
        plt.title("Sample Count by Lineage")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

    return data