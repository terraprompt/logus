#!/bin/bash
cd /app/app
alembic upgrade head
cd /app
pm2-runtime start ecosystem.config.json