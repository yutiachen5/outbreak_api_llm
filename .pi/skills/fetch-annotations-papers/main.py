import json
import argparse
from datetime import datetime

from annotations_tools import get_annotation_papers_by_mutation_and_collection_date, get_annotation_effects, get_annotations_by_effect_detail

def main():
    parser = argparse.ArgumentParser(description="Outbreak API annotations tools dispatcher")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # -- get_annotation_papers_by_mutation_and_collection_date subcommand
    a_by_mut_and_date = subparsers.add_parser("get_annotation_papers_by_mutation_and_collection_date", \
                                      help="Get annotation papers by mutation and collection date.")
    a_by_mut_and_date.add_argument("--effect_detail", required=True, type=str, help="Plain string with spaces")
    a_by_mut_and_date.add_argument("--date_bin", default="month", choices=["month", "week", "year"], help="Time binning interval")
    a_by_mut_and_date.add_argument("--days", default=5, type=int, help="Interval length in days")
    a_by_mut_and_date.add_argument("--max_span_days", type=int, default=31, help="Maximum collection span in days")

    # -- get_annotation_effects subcommand
    a_effects = subparsers.add_parser("get_annotation_effects", \
                                      help="Get annotation effects.")

    # - - get_annotations_by_effect_detail subcommand
    a_by_effect = subparsers.add_parser("get_annotations_by_effect_detail", \
                                        help ="Get annotations by effect detail")
    a_by_effect.add_argument("--effect_detail", required=True, type=str, help="Plain string with spaces")

    args = parser.parse_args()

    if args.command == "get_annotation_papers_by_mutation_and_collection_date":
        result = get_annotation_papers_by_mutation_and_collection_date(
            effect_detail=args.effect_detail,
            days=args.days,
            date_bin=args.date_bin,
            max_span_days=args.max_span_days,
        )
    elif args.command == "get_annotation_effects":
        result = get_annotation_effects()
    elif args.command == "get_annotations_by_effect_detail":
        result = get_annotations_by_effect_detail(
            effect_detail=args.effect_detail
        )

    print(json.dumps(result, indent=2))
    
    # save the result in json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"response_{args.command}_{timestamp}.json"
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)
    
if __name__ == "__main__":
    main()