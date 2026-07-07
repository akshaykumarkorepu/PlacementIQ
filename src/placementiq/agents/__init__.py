"""Processing components grouped by stage of the pipeline.

Sub-packages:
    ingestion   — deterministic: crawler, fetcher, parser, rate_limit, adapters
    extraction  — LLM-bound: extractor, validator, schema, prompt
    analytics   — router + renderer are LLM-bound; engine + confidence are deterministic SQL

The LLM boundary is encoded in the directory tree. See docs/architecture.md.
"""
