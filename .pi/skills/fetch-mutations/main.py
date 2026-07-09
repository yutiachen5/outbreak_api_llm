import json
import argparse
from datetime import datetime

from mutation_tools import get_mutation_frequency_score

def main():
    parser = argparse.ArgumentParser(description="Outbreak API phenotype metric tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- get_mutation_frequency_score subcommand
    p_mut_freq_score = subparsers.add_parser("get_mutation_frequency_score", help="Get mutation frequency score")
    p_mut_freq_score.add_argument("--region", required=True, help="Region of interest (e.g. XAJ25415.1)")
    p_mut_freq_score.add_argument("--metric", required=True, help="Metric of interest (e.g. sa26_usage_increase_new)")
    p_mut_freq_score.add_argument("--visualize", action="store_true", default=False)
    p_mut_freq_score.add_argument("--output_path", default="mutation_frequency_score.png")
    p_mut_freq_score.add_argument("--export_csv", action="store_true", default=False)
    p_mut_freq_score.add_argument("--csv_output_path", default="mutation_data.csv")


    args = parser.parse_args()
    if args.command == "get_mutation_frequency_score":
        result = get_mutation_frequency_score(
            region=args.region,
            metric=args.metric,
            visualize=args.visualize,
            export_csv=args.export_csv,
            csv_output_path=args.csv_output_path,
            output_path=args.output_path
        )

    print(json.dumps(result, indent=2))

    # save the result in json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"response_{args.command}_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()