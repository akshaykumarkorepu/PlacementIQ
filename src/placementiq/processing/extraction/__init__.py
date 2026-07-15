"""Extraction agents — the LLM-bound surface that turns prose into typed records.

Components:
    extractor   — invokes the LLM with a closed JSON schema
    validator   — grounds each extracted field against the source text
    schema      — the closed JSON schema
    prompt      — versioned extraction prompt
"""

__all__: list[str] = []
