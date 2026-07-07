"""Per-component settings modules.

Each sub-module defines a typed Pydantic settings object for one component.
Settings modules are leaf nodes: they import from stdlib and Pydantic only,
and are imported by exactly one component. No global god-config.
"""

__all__: list[str] = []
