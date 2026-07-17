#!/usr/bin/env python3
import sys
import requests
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent)) # go up 4 dirs
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT

def get_mutation_frequency_score(
        region: str,
        metric: str,
        visualize: bool = False,
        output_path: str | None = "mutation_frequency_score.png",
        export_csv: bool = False,
        csv_output_path: str = "mutation_data.csv"
) -> dict:
    url = f"{OUTBREAK_API_BASE}/mutations/frequency/score" #https://h5n1.outbreak.info/api/mutations/frequency/score?region=XAJ25415.1&metric=sa26_usage_increase_new
    response = requests.get(
        url = url,
        params={"region": region, "metric": metric},
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    data = response.json()

    if visualize and output_path is not None:
        min_max_url = f"{OUTBREAK_API_BASE}/v0/phenotype_metric_values:getMinAndMaxValues"
        min_max_response = requests.get(
            min_max_url,
            params={"phenotype_metric_name": metric},
            timeout=API_REQUEST_TIMEOUT
        )
        min_max_response.raise_for_status()
        min_max_data = min_max_response.json()
        x_max = min_max_data[1]
        pheno_values = [item["pheno_value"] for item in data]
        counts = [item["count"] for item in data]
        plt.figure(figsize=(10, 6))
        plt.scatter(pheno_values, counts)
        plt.xlim(0, x_max)
        plt.yscale("log")
        plt.xlabel("Pheno Value")
        plt.ylabel("Count")
        plt.title(f"Mutation Frequency Score for Region: {region}, Metric: {metric}")
        plt.tight_layout()      
        plt.savefig(output_path)
        plt.close()
    if export_csv == True:
        site_map = load_site_numbering_map()
        with open(csv_output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Mutation", "H3 Site Number", "Count", "DMS"])
            for item in data:
                mutation = f"{item['ref_aa']}{item['position_aa']}{item['alt_aa']}"
                h3_site = site_map.get(str(item['position_aa']), "N/A")
                writer.writerow([mutation, h3_site, item['count'], item['pheno_value']])
    return data



def load_site_numbering_map():
    lookup ={}
    csv_path=Path(__file__).parent / "site_numbering_map.csv"
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lookup[row["sequential_site"]] = row["reference_site"]
    return lookup

def get_region_and_gff() -> dict:
    url = f"{OUTBREAK_API_BASE}/mutations:regionAndGffFeature" #https://h5n1.outbreak.info/api/mutations:regionAndGffFeature
    response = requests.get(
        url=url,
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    data = response.json()
    return data

def get_mutation_by_sample(
        q: str = None,
        country: str = None,
        collection_start_date: str=None, 
        collection_end_date: str=None,
        host: str=None
) -> dict:
    if q is None:
        filters =[]
        if country:
            filters.append(f"country:{country}")
        if collection_start_date:
            filters.append(f"collection_start_date:>={collection_start_date}")
        if collection_end_date:
            filters.append(f"collection_end_date:<={collection_end_date}")
        if host:
            filters.append(f"host:{host}")
        if filters:
            q="^".join(filters)
    url = f"{OUTBREAK_API_BASE}/mutations/by/sample?q={q}" #https://h5n1.outbreak.info/api/mutations/by/sample?q=
    response = requests.get(
        url=url,
        timeout=API_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    data = response.json()
    return data