import requests

from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT


TOOL_MAP = {
    "fetch_lineages": lambda args: fetch_lineages(args.get("lineage_system_name", "PANGO")),
    "fetch_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date": lambda args: fetch_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date(
        phenotype_metric_name=args.get("phenotype_metric_name"),
        lineage_system_name=args.get("lineage_system_name", "PANGO"),
        background=args.get("background"), # None if not provided by user
        date_bin=args.get("date_bin", "month"),
        max_span_days=args.get("max_span_days", 366)
    )
}

def fetch_lineages(lineage_system_name: str = "PANGO") -> dict:
    url = f"{OUTBREAK_API_BASE}/lineages"
    response = requests.get(url, params={"lineage_system_name": lineage_system_name}, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()

def fetch_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date(
    phenotype_metric_name: str,
    lineage_system_name: str = "PANGO",
    background: str = None,
    date_bin: str = "month",
    max_span_days: int = 366,
) -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/phenotype_metric_values:forMutationsAggregateBySampleAndCollectionDate"

    params={
        "phenotype_metric_name": phenotype_metric_name,
        "lineage_system_name": lineage_system_name,
        "date_bin": date_bin,
        "max_span_days": max_span_days,
    }
    if background is not None:
        params["background"] = background# only add background to params when it's not null 

    response = requests.get(url, params, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()