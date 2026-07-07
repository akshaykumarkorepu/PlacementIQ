"""Analytics agents — the online query path.

Components:
    router      — LLM-bound: maps a student question to a canonical query intent
    engine      — deterministic SQL: executes the canonical query templates
    confidence  — deterministic: scores the answer's trust
    renderer    — LLM-bound: turns structured query results into cited prose
    templates/  — one SQL template per canonical question

engine and confidence are pure SQL/python; only router and renderer use the LLM.
"""

__all__: list[str] = []
