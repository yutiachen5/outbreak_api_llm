import json
import argparse
from datetime import datetime

from pheno_metric_tools import get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date, get_phenotype_metrics, get_phenotype_metric_min_max

def main():
    parser = argparse.ArgumentParser(description="Outbreak API phenotype metric tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- get_phenotype_metrics subcommand
    p_phenotype_metrics = subparsers.add_parser("get_phenotype_metrics", help="Get phenotype metrics")

    # -- get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date subcommand
    p_mut_agg = subparsers.add_parser("get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date", \
                                      help="Get aggregated pheno values by sample and collection date.")
    p_mut_agg.add_argument("--phenotype_metric_name", required=True, help="e.g. delta_bind, delta_expr, evescape")
    p_mut_agg.add_argument("--lineage_system_name", default="PANGO", help="Lineage classification system (e.g. PANGO)")
    p_mut_agg.add_argument("--background", default=None, help="Reference background, e.g. NC_045512.2_BA.1_rbd")
    p_mut_agg.add_argument("--date_bin", default="month", choices=["month", "week", "year"], help="Time binning interval")
    p_mut_agg.add_argument("--days", default=5, type=int, help="Interval length in days")
    p_mut_agg.add_argument("--max_span_days", type=int, default=366, help="Maximum collection span in days")

    # -- get_phenotype_metric_min_max subcommand
    p_min_max = subparsers.add_parser("get_phenotype_metric_min_max", help="Get min and max values for a phenotype metric")
    p_min_max.add_argument("--phenotype_metric_name", required=True, help="e.g. sa26_usage_increase_new")

    args = parser.parse_args()

    if args.command == "get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date":
        result = get_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date(
            phenotype_metric_name=args.phenotype_metric_name,
            lineage_system_name=args.lineage_system_name,
            background=args.background,
            days=args.days,
            date_bin=args.date_bin,
            max_span_days=args.max_span_days,
        )
    elif args.command == "get_phenotype_metrics":
        result = get_phenotype_metrics()
    elif args.command == "get_phenotype_metric_min_max":
        result = get_phenotype_metric_min_max(
            phenotype_metric_name=args.phenotype_metric_name
        )
    print(json.dumps(result, indent=2))
    
    # save the result in json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"response_{args.command}_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    
if __name__ == "__main__":
    main()