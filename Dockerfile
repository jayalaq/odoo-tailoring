FROM python:3.12-slim-bookworm

LABEL maintainer="Tailoring Consult"

# Evitar prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Dependencias del sistema para Odoo 19
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    gcc \
    g++ \
    git \
    libfreetype6-dev \
    libfribidi-dev \
    libharfbuzz-dev \
    libjpeg62-turbo-dev \
    liblcms2-dev \
    libldap2-dev \
    libopenjp2-7-dev \
    libpq-dev \
    libsasl2-dev \
    libtiff5-dev \
    libwebp-dev \
    libxml2-dev \
    libxslt1-dev \
    libssl-dev \
    node-less \
    npm \
    postgresql-client \
    xfonts-75dpi \
    xfonts-base \
    && rm -rf /var/lib/apt/lists/*

# Instalar wkhtmltopdf (para reportes PDF)
RUN curl -o /tmp/wkhtmltox.deb -sSL \
    https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb \
    && apt-get update \
    && apt-get install -y --no-install-recommends /tmp/wkhtmltox.deb \
    && rm /tmp/wkhtmltox.deb \
    && rm -rf /var/lib/apt/lists/*

# Instalar rtlcss para soporte RTL
RUN npm install -g rtlcss

# Crear usuario odoo
RUN useradd -m -d /opt/odoo -s /bin/bash odoo

# Crear directorios necesarios
RUN mkdir -p /opt/odoo/extra-addons \
    && mkdir -p /etc/odoo \
    && mkdir -p /var/lib/odoo

# Copiar codigo fuente de Odoo
COPY . /opt/odoo/odoo

WORKDIR /opt/odoo/odoo

# Instalar dependencias Python de Odoo
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir psycopg2-binary

# Copiar configuracion
COPY odoo.conf /etc/odoo/odoo.conf

# Permisos
RUN chown -R odoo:odoo /opt/odoo \
    && chown -R odoo:odoo /etc/odoo \
    && chown -R odoo:odoo /var/lib/odoo

# Cambiar a usuario odoo
USER odoo

EXPOSE 8069 8071 8072

CMD ["python3", "odoo-bin", "-c", "/etc/odoo/odoo.conf"]
