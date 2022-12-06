#!/usr/bin/env bash

# Start a uvicorn ASGI server.
uvicorn candidate_api.main:app --host 0.0.0.0 --port 8081 --reload