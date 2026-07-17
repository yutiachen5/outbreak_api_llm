#!/usr/bin/env python3

import sys
import requests
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))
from config import OUTBREAK_API_BASE, API_REQUEST_TIMEOUT


def get_annotation_papers_by_mutation_and_collection_date(
    effect_detail: str,
    date_bin: str = "month",
    days: int = 5,
    max_span_days: int = 31,
    visualize: bool = False,
    output_path: str | None = None
) -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/annotations:byMutationsAndCollectionDate"

    params = {
        "effect_detail": effect_detail,
        "date_bin": date_bin,
        "days": days,
        "max_span_days": max_span_days,
    }
    
    response = requests.get(url, params=params, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    
    if visualize:
        dates = [item["date"] for item in data]
        proportions_with = [round(float(item["proportion"]), 3) for item in data]
        proportions_without = [round(1 - float(item["proportion"]), 3) for item in data]
        counts_with = [item["n"] for item in data]
        counts_without = [item["n_total"] - item["n"] for item in data]
        
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        formatted_dates = []
        for date_str in dates:
            year, month = date_str.split('-')
            month_idx = int(month) - 1
            formatted_dates.append(f"{months[month_idx]} '{year[-2:]}")
        
        step = max(1, len(dates) // 10)
        tick_positions = list(range(0, len(dates), step))
        tick_labels = [formatted_dates[i] for i in tick_positions]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
        
        x_pos = range(len(dates))
        ax1.bar(x_pos, proportions_with, label = effect_detail)
        ax1.bar(x_pos, proportions_without, bottom=proportions_with, label = f"Not Annotated with {effect_detail}")
        ax1.set_ylabel("Proportion")
        ax1.set_title("Proportion of unique mutations")
        ax1.set_xticks(tick_positions)
        ax1.set_xticklabels(tick_labels, rotation=45)
        ax1.set_ylim(0, 1)
        ax1.legend()
        
        ax2.bar(x_pos, counts_with, label = effect_detail)
        ax2.bar(x_pos, counts_without, bottom=counts_with, label = f"Not Annotated with {effect_detail}")
        ax2.set_ylabel("Count")
        ax2.set_title("Count of unique mutations")
        ax2.set_xticks(tick_positions)
        ax2.set_xticklabels(tick_labels, rotation=45)
        ax2.legend()
        
        plt.tight_layout()
        if output_path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_path = f"annotation_papers_{timestamp}.png"
        plt.savefig(output_path)
        plt.close()
    
    return data


def get_annotations_by_effect_detail(
    effect_detail: str,
    visualize: bool = False,
    segment: str = "HA",
    output_path: str | None = None
) -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/annotations:byMutationsAndAminoAcidPosition"
    response = requests.get(url=url, params={"effect_detail": effect_detail}, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    
    if visualize:
        aggregated_data = {}
        for key in data:
            for item in data[key]:
                pos = item["position_aa"]
                count = item["count"]
                aggregated_data[pos] = aggregated_data.get(pos, 0) + count
        
        if aggregated_data:
            positions = sorted(aggregated_data.keys())
            counts = [aggregated_data[p] for p in positions]
            
            fig, ax = plt.subplots(figsize=(12, 4))
            ax.bar(positions, counts)
            ax.set_xlabel("Position")
            ax.set_ylabel("Count")
            ax.set_title("Mutations by Position (HA)")
            
            plt.tight_layout()
            if output_path is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = f"annotations_by_position_{segment}_{timestamp}.png"
            plt.savefig(output_path)
            plt.close()
    
    return data


def get_annotation_effects() -> dict:
    url = f"{OUTBREAK_API_BASE}/v0/annotationEffects"
    response = requests.get(url=url, timeout=API_REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()