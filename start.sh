#!/bin/sh
set -e

/opt/venv/bin/alembic upgrade head
exec /opt/venv/bin/uvicorn main:app --host 0.0.0.0 --port 9000