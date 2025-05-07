#!/usr/bin/env python3
"""Entrypoint for terminal or API use."""

import os
import sys
from dotenv import load_dotenv
from orchestrator.input_parser import parse_input
from orchestrator.context_tracker import ContextTracker
from orchestrator.router import route_request

def main():
    """Main entry point."""
    # Load environment variables
    env_path = os.path.join(os.path.dirname(__file__), 'config', 'settings.env')
    load_dotenv(env_path)

    # Collect user input
    user_input = ' '.join(sys.argv[1:])
    if not user_input:
        print("Please provide input.")
        sys.exit(1)

    # Parse input and initialize context
    parsed = parse_input(user_input)
    context = ContextTracker()

    # Route request through orchestrator
    result = route_request(parsed, context)
    print(result)

if __name__ == "__main__":
    main()
