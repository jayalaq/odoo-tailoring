#!/bin/bash
# Tailoring Consult ERP - SSL Setup Script
# Usage: ./setup-ssl.sh yourdomain.com your@email.com

set -e

DOMAIN=$1
EMAIL=$2

if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
    echo "Usage: $0 <domain> <email>"
    echo "Example: $0 erp.mycompany.com admin@mycompany.com"
    exit 1
fi

echo "=== Tailoring Consult ERP - SSL Setup ==="
echo "Domain: $DOMAIN"
echo "Email: $EMAIL"

# Update nginx config with the actual domain
sed -i "s/YOUR_DOMAIN/$DOMAIN/g" ../nginx/nginx.conf
sed -i "s/server_name _;/server_name $DOMAIN;/g" ../nginx/nginx.conf

# Create cert directories
mkdir -p ../nginx/certs
mkdir -p ../nginx/certbot

# First, start nginx without SSL for the ACME challenge
echo "Starting services for SSL verification..."
docker compose -f ../docker-compose.prod.yml up -d nginx

# Request certificate
echo "Requesting SSL certificate..."
docker compose -f ../docker-compose.prod.yml run --rm certbot certonly \
    --webroot \
    --webroot-path=/var/www/certbot \
    --email "$EMAIL" \
    --agree-tos \
    --no-eff-email \
    -d "$DOMAIN"

# Restart all services with SSL
echo "Restarting with SSL enabled..."
docker compose -f ../docker-compose.prod.yml down
docker compose -f ../docker-compose.prod.yml up -d

echo ""
echo "=== SSL Setup Complete ==="
echo "Your Tailoring Consult ERP is available at: https://$DOMAIN"
echo "SSL certificate will auto-renew via certbot."
