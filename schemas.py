
TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "fetch_lineages",
            "description": (
                "Fetch viral lineage data from the outbreak API. "
                "Returns a list of lineages for the specified classification system. "
                "Use this to answer questions about viral variants and their lineages."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "lineage_system_name": {
                        "type": "string",
                        "description": "The lineage system to query, e.g. 'PANGO' for SARS-CoV-2 variants.",
                    }
                },
                "required": ["lineage_system_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "fetch_pheno_metric_for_mutation_aggregated_by_sample_and_collection_date",
            "description": (
                "Fetch aggregated phenotype metric values for mutations by sample and collection date. "
                "Use this to answer questions about phenotype metrics like binding or escape scores "
                "for viral variants over time."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "phenotype_metric_name": {
                        "type": "string",
                        "description": "The phenotype metric to query, e.g. 'delta_bind', 'delta_expr', 'evescape'.",
                    },
                    "lineage_system_name": {
                        "type": "string",
                        "description": "The lineage system to query, e.g. 'PANGO'. Defaults to 'PANGO' if not specified.",
                        "default": "PANGO",
                    },
                    "background": {
                        "type": ["string", "null"],
                        "description": "The reference background, e.g. 'NC_045512.2_BA.1_rbd'. Nullable — omit if the user does not specify a background.",
                    },
                    "date_bin": {
                        "type": "string",
                        "description": "Time binning: 'month', 'week', or 'year'. Defaults to 'month' if not specified.",
                        "default": "month",
                    },
                    "max_span_days": {
                        "type": "integer",
                        "description": "Maximum collection span in days. Defaults to 366 if not specified.",
                        "default": 366,
                    },
                },
                "required": ["phenotype_metric_name"],  # only truly required ones
            }
        }
    }
]

