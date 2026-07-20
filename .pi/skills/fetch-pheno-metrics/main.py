import json
import argparse
from datetime import datetime

from pheno_metric_tools import get_phenotype_metrics, get_phenotype_metric_min_max

def main():
    parser = argparse.ArgumentParser(description="Outbreak API phenotype metric tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    metric_parser = subparsers.add_parser("get_phenotype_metrics")
    
    min_max_parser = subparsers.add_parser("get_phenotype_metric_min_max")
    min_max_parser.add_argument("--phenotype_metric_name", required=True)

    args = parser.parse_args()

    if args.command == "get_phenotype_metrics":
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