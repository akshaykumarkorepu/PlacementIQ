"""SQL templates — one module per canonical question.

Each template is a pure function from a typed intent to a parameterised SQL
query. Templates are deterministic and LLM-free by construction.
"""

__all__: list[str] = []
