"""Shared Pydantic models — the cross-module type contract.

Every type that crosses a module boundary lives here. Components import from
this package; this package imports from common/ and stdlib only.
"""

__all__: list[str] = []
