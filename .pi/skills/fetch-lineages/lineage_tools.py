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
        group_by: str = "collection_data",
        date_bin: str="month",
        days = 5,
        change_bin: str = "aa",
        max_span_days =30
) -> dict:
    url =f"{OUTBREAK_API_BASE}/v0/lineages:count" #https://h5n1.outbreak.info/api/v0/lineages:count?group_by=collection_date&date_bin=month&days=5&change_bin=aa&max_span_days=30
    response = requests.get(
        url=url,
        params={"group_by": group_by,"date_bin":date_bin, "days": days, "change_bin": change_bin, "max_span_days": max_span_days},
        timeout = API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()

def plot_lineage_sample_count(
        group_by: str = "lineage_name",
        lineage_system_name = "usda_genoflu",
        output_path: str = "lineage_sample_count.png"
):
    url = f"{OUTBREAK_API_BASE}/v0/lineages:count" #https://h5n1.outbreak.info/api/v0/lineages:count?group_by=lineage_name&lineage_system_name=usda_genoflu
    response = requests.get(
        url =url,
        params = {"group_by": group_by, "lineage_system_name" : lineage_system_name},
        timeout = API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    data = response.json()

    # Filter by lineage_system_name as the API may return multiple systems
    filtered = [item for item in data if item["lineage_system"] == lineage_system_name]
    lineages = [item["lineage"] for item in filtered]
    counts =[item["count"] for item in filtered]

    plt.figure(figsize= (15,6))
    plt.bar(lineages, counts)
    plt.xlabel("Lineage")
    plt.ylabel("Count")
    plt.title("Sample Count by Lineage")
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    return data