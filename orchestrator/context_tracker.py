"""Maintains session or user context."""

class ContextTracker:
    """Tracks context for a user session."""

    def __init__(self):
        self._context = {}

    def update_context(self, key, value):
        """Update the context with a new key-value pair."""
        self._context[key] = value

    def get_context(self):
        """Retrieve the current context."""
        return self._context
