"""Ingestion agents — deterministic HTTP fetch and HTML parse pipeline.

This sub-package must never import the LLM SDK. It only writes to database.raw_db.
"""

__all__: list[str] = []
