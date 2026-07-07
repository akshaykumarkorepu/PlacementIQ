"""Persistence layer — the only module that talks to SQLite/Postgres.

Components:
    raw_db          — immutable Raw DB read/write interface
    structured_db   — versioned Structured DB read/write interface
    run_log         — pipeline run metrics and stage telemetry
"""

__all__: list[str] = []
