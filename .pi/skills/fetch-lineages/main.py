import json
import argparse
from datetime import datetime

from lineage_tools import get_lineages_by_lineage_system, get_mutation_profile_by_lineage, get_mutation_incidence_by_lineage

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

    # -- get_mutation_inidence_by_lineage subcommabnd
    p_mut_incidence = subparsers.add_parser("get_mutation_incidence_by_lineage", help="Get mutation incidence by lineage and lineage system")
    p_mut_incidence.add_argument("--lineage", required=True)
    p_mut_incidence.add_argument("--lineage_system_name", default = "usda_genoflu")
    p_mut_incidence.add_argument("--prevalence_threshold", type = float, default = 0.75)
    p_mut_incidence.add_argument("--change_bin", default = "aa")

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

    print(json.dumps(result, indent=2))

    # save the result in json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"response_{args.command}_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    
if __name__ == "__main__":
    main()