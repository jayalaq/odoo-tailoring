#!/bin/bash
# ==============================================
# Script de despliegue de Odoo 19 con Docker
# Tailoring Consult
# ==============================================

set -e

echo "=========================================="
echo "  Despliegue de Odoo 19 - Tailoring Consult"
echo "=========================================="

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Verificar que Docker este instalado
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker no esta instalado. Instalando...${NC}"
    curl -fsSL https://get.docker.com | sh
    systemctl start docker
    systemctl enable docker
    echo -e "${GREEN}Docker instalado correctamente.${NC}"
fi

# Verificar Docker Compose
if ! docker compose version &> /dev/null; then
    echo -e "${RED}Docker Compose no esta disponible.${NC}"
    echo "Instala Docker Compose e intenta de nuevo."
    exit 1
fi

# Crear carpeta de addons extra si no existe
mkdir -p extra-addons

echo ""
echo -e "${YELLOW}IMPORTANTE: Antes de continuar, asegurate de:${NC}"
echo "1. Haber copiado el codigo fuente de Odoo 19 en esta carpeta"
echo "   (debe existir el archivo odoo-bin en este directorio)"
echo "2. Cambiar las contrasenas en docker-compose.yml y odoo.conf"
echo ""

# Verificar que existe odoo-bin
if [ ! -f "odoo-bin" ]; then
    echo -e "${RED}ERROR: No se encontro 'odoo-bin' en el directorio actual.${NC}"
    echo "Asegurate de que el codigo fuente de Odoo 19 este en esta carpeta."
    echo ""
    echo "Si descargaste Odoo de GitHub, copia todos los archivos aqui:"
    echo "  cp -r /ruta/a/odoo/* ."
    echo ""
    exit 1
fi

echo -e "${GREEN}Codigo de Odoo detectado. Iniciando despliegue...${NC}"
echo ""

# Construir y levantar
echo "Paso 1/3: Construyendo imagen Docker..."
docker compose build --no-cache

echo ""
echo "Paso 2/3: Levantando servicios..."
docker compose up -d

echo ""
echo "Paso 3/3: Verificando servicios..."
sleep 5
docker compose ps

echo ""
echo "=========================================="
echo -e "${GREEN}Despliegue completado!${NC}"
echo ""
echo "Accede a Odoo en: http://$(hostname -I | awk '{print $1}'):8069"
echo ""
echo "Credenciales de admin master:"
echo "  Password: TailoringAdmin2024!"
echo "  (Cambiala en odoo.conf -> admin_passwd)"
echo ""
echo "Comandos utiles:"
echo "  Ver logs:      docker compose logs -f odoo-web"
echo "  Reiniciar:     docker compose restart"
echo "  Detener:       docker compose down"
echo "  Reconstruir:   docker compose up -d --build"
echo "=========================================="
