import json
import argparse
from datetime import datetime

from variant_tools import get_variant_frequency_score, get_mutation_lag_by_lineage

def main():
    parser = argparse.ArgumentParser(description="Outbreak API variant tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- get_variant_frequency_score subcommand
    p_var_freq_score = subparsers.add_parser("get_variant_frequency_score", help="Get variant frequency score by region and metric")
    p_var_freq_score.add_argument("--region", required=True, help="Region identifier (e.g. XAJ25415.1)")
    p_var_freq_score.add_argument("--metric", required=True, help="Metric name (e.g. sa26_usage_increase_new)")

    # -- get_mutation_lag_by_lineage subcommand
    p_mut_lag = subparsers.add_parser("get_mutation_lag_by_lineage", help = "Get mutation lag by lineage and lineage system")
    p_mut_lag.add_argument("--lineage", required = True)
    p_mut_lag.add_argument("--lineage_system_name", required = True)

    args = parser.parse_args()

    if args.command == "get_variant_frequency_score":
        result = get_variant_frequency_score(
            region=args.region,
            metric=args.metric
       )
    elif args.command == "get_mutation_lag_by_lineage":
        result = get_mutation_lag_by_lineage(
            lineage= args.lineage,
            lineage_system_name = args.lineage_system_name
        )

    print(json.dumps(result, indent=2))
    
    # save the result in json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"response_{args.command}_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()