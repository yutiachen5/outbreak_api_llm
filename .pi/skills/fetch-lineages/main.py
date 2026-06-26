import json
import argparse
from datetime import datetime
import matplotlib

from lineage_tools import get_lineages_by_lineage_system, get_mutation_profile_by_lineage, get_mutation_incidence_by_lineage, get_lineage_count, plot_lineage_sample_count

def main():
    parser = argparse.ArgumentParser(description="Outbreak API lineage tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- get_lineages_by_lineage_system subcommand
    p_lineages = subparsers.add_parser("get_lineages_by_lineage_system", help="Get lineages by lineage system")
    p_lineages.add_argument("--lineage_system_name", default="usda_genoflu")

    # -- get_mutation_profile_by_lineage subcommand
    p_mut_profile = subparsers.add_parser("get_mutation_profile_by_lineage", help="Get mutation profile by lineage and lineage system")
    p_mut_profile.add_argument("--lineage_name", required=True)
    p_mut_profile.add_argument("--lineage_system_name", default="usda_genoflu")

    # -- get_mutation_incidence_by_lineage subcommand
    p_mut_incidence = subparsers.add_parser("get_mutation_incidence_by_lineage", help="Get mutation incidence by lineage and lineage system")
    p_mut_incidence.add_argument("--lineage", required=True)
    p_mut_incidence.add_argument("--lineage_system_name", default = "usda_genoflu")
    p_mut_incidence.add_argument("--prevalence_threshold", type = float, default = 0.75)
    p_mut_incidence.add_argument("--change_bin", default = "aa")

    # -- get_lineage_count subcommand
    p_lineage_count = subparsers.add_parser("get_lineage_count", help="Get lineage count by various parameters")
    p_lineage_count.add_argument("--group_by", default="collection_data")
    p_lineage_count.add_argument("--date_bin", default="month")
    p_lineage_count.add_argument("--days", type=int, default=5)
    p_lineage_count.add_argument("--change_bin", default="aa")
    p_lineage_count.add_argument("--max_span_days", type=int, default=30)

    # -- plot_lineage_sample_count
    p_plot_lineage = subparsers.add_parser("plot_lineage_sample_count", help= "Plot sample count by lineage")
    p_plot_lineage.add_argument("--lineage_system_name", default = "usda_genoflu")
    p_plot_lineage.add_argument("--group_by", default = "lineage_name")
    p_plot_lineage.add_argument("--output_path", default = "lineage_sample_count.png")


    args = parser.parse_args()



    if args.command == "get_lineages_by_lineage_system":
        result = get_lineages_by_lineage_system(lineage_system_name=args.lineage_system_name)
    elif args.command == "get_mutation_profile_by_lineage":
        result = get_mutation_profile_by_lineage(
            lineage_name=args.lineage_name,
            lineage_system_name=args.lineage_system_name)
    elif args.command == "get_mutation_incidence_by_lineage":
        result = get_mutation_incidence_by_lineage(
            lineage=args.lineage,
            lineage_system_name=args.lineage_system_name,
            prevalence_threshold=args.prevalence_threshold,
            change_bin=args.change_bin)
    elif args.command == "get_lineage_count":
        result = get_lineage_count(
            group_by=args.group_by,
            date_bin = args.date_bin,
            days = args.days,
            change_bin =args.change_bin,
            max_span_days =args.max_span_days
        )
    elif args.command == "plot_lineage_sample_count":
        result = plot_lineage_sample_count(
            group_by =args.group_by,
            lineage_system_name=args.lineage_system_name,
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