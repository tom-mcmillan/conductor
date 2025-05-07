# Conductor

Central conductor service for the Conduct system.

This project orchestrates modular backend services using the OpenAI Agents SDK and Responses API.

## Project Structure

```text
.
├── agentsdk/
│   └── (SDK files will be added manually)
├── orchestrator/
│   ├── router.py
│   ├── input_parser.py
│   └── context_tracker.py
├── services/
│   ├── artifacting_client.py
│   ├── db_client.py
│   └── argdown_client.py
├── agents/
│   └── conduct_agent.json
├── config/
│   └── settings.env
├── main.py
├── requirements.txt
└── README.md
```

## Next Steps

1. Copy the OpenAI Agents SDK files into `agentsdk/`.
2. Define `conduct_agent.json`.
3. Implement orchestration logic in `orchestrator/router.py`.
4. Create service client contracts in `services/`.
