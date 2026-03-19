#!/bin/bash
# Tailoring Consult ERP - Deployment Script
# Usage: ./deploy.sh

set -e

echo "=== Tailoring Consult ERP - Deployment ==="

cd "$(dirname "$0")/.."

# Check .env file
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo "Copy .env.example to .env and update the values:"
    echo "  cp .env.example .env"
    exit 1
fi

# Build and start
echo "Building containers..."
docker compose -f docker-compose.prod.yml build

echo "Starting services..."
docker compose -f docker-compose.prod.yml up -d

echo "Waiting for database..."
sleep 10

echo ""
echo "=== Deployment Complete ==="
echo "Tailoring Consult ERP is running at http://localhost:8069"
echo ""
echo "Next steps:"
echo "1. Access http://your-server-ip:8069 to create the database"
echo "2. Install the 'tailoring_branding' module first, then 'tailoring_core'"
echo "3. For SSL, run: cd scripts && ./setup-ssl.sh yourdomain.com your@email.com"
