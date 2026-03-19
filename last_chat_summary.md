# Resumen del Ultimo Chat - Instalacion de Odoo

## Tema: Instalar Odoo en un repositorio separado (con Docker)

### Contexto
Se decidio instalar Odoo usando Docker en el VPS de Hostinger (IP: 195.35.11.19), manteniendo el ERP actual sin cambios.

### Version de Odoo
- **Odoo 12.0** (version 2019)
- **Base de datos**: PostgreSQL 13

### Pasos acordados

#### Paso 1: Crear la carpeta
```bash
mkdir -p /root/odoo/addons
```

#### Paso 2: Crear el archivo docker-compose.yml
```bash
cat > /root/odoo/docker-compose.yml << 'EOF'
version: '3.1'
services:
  odoo-web:
    image: odoo:12.0
    depends_on:
      - odoo-db
    ports:
      - "8069:8069"
    volumes:
      - odoo-data:/var/lib/odoo
      - ./addons:/mnt/extra-addons
    environment:
      - HOST=odoo-db
      - USER=odoo
      - PASSWORD=odoo_password_segura
    restart: always

  odoo-db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo_password_segura
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - db-data:/var/lib/postgresql/data/pgdata
    restart: always

volumes:
  odoo-data:
  db-data:
EOF
```

#### Paso 3: Levantar Odoo
```bash
cd /root/odoo
docker compose up -d
```

#### Paso 4: Verificar que este corriendo
```bash
docker compose ps
```

#### Paso 5: Acceder a Odoo
Abrir en el navegador: `http://195.35.11.19:8069`

### Notas importantes
- Los modulos personalizados van en la carpeta `addons/` y Odoo los detecta automaticamente.
- Se puede configurar un subdominio (ej: `odoo.tailoringconsult.com`) con Nginx apuntando al puerto 8069.
- **IMPORTANTE**: Cambiar `odoo_password_segura` por una contrasena segura real antes de ejecutar en produccion.
