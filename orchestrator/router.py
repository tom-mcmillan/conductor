"""Determines which services to invoke based on parsed input and context."""
import os
from dotenv import load_dotenv
from services.artifacting_client import ArtifactingClient
from services.db_client import DBClient
from services.argdown_client import ArgdownClient

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), os.pardir, 'config', 'settings.env'))

def route_request(parsed_input, context):
    """Route a request to the appropriate services."""
    # Example workflow: create artifact, query DB, process with Argdown
    artifact_data = parsed_input.get("raw_input")
    art_client = ArtifactingClient(os.getenv("ARTIFACTING_SERVICE_URL"))
    artifact = art_client.create_artifact({"content": artifact_data})

    db_client = DBClient(os.getenv("DB_SERVICE_URL"))
    db_result = db_client.query({"artifact_id": artifact.get("id")})

    arg_client = ArgdownClient(os.getenv("ARGDOWN_SERVICE_URL"))
    processed = arg_client.process(artifact)

    # Update context
    context.update_context("last_artifact", artifact)

    return {
        "artifact": artifact,
        "db_result": db_result,
        "processed": processed,
    }
