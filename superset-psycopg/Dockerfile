# Argumento para podermos usar a mesma receita para o Master e o RegionServer
ARG SUPERSET_IMAGE=apache/superset:latest

# Use a imagem base do HBase da BDE
FROM ${SUPERSET_IMAGE}

# Diretório de trabalho
WORKDIR /app

# Precisamos do root para as instalações
USER root

# Instala gcc, necessário para compilar os pacotes (Não deixe isso instalado em um ambiente de produção!), 
# e o heimdal requerido para compilar o phoenixdb devido a um problema na distro
# pkg-config para a instalação do 
RUN apt-get update && apt-get install -y --no-install-recommends gcc heimdal-dev pkg-config && rm -rf /var/lib/apt/lists/*

# Pil e Drivers para os principais bancos. 
RUN uv pip install Pillow psycopg2 sqlalchemy-phoenix phoenixdb pyhive oracledb pymssql  mysqlclient thrift thrift_sasl
# six


# "Hack" para corrigir o import problemático no driver sqlalchemy-phoenix
# Patch para corrigir a biblioteca 'sqlalchemy-phoenix' e torná-la compatível com Python 3
RUN \
    # Define o caminho do arquivo para facilitar a leitura
    export TARGET_FILE=/app/.venv/lib/python3.10/site-packages/sqlalchemy_phoenix/phoenix_db.py && \
    # 1. Corrige o import relativo do PhoenixDialect
    sed -i 's/from base import PhoenixDialect/from .base import PhoenixDialect/g' $TARGET_FILE && \
    # 2. Substitui o 'import urlparse' antigo pela versão moderna do Python 3
    sed -i 's/import urlparse/from urllib import parse as urlparse/g' $TARGET_FILE && \
    # 3. Comenta o 'import urllib' que se tornou desnecessário
    sed -i 's/import urllib/#import urllib/g' $TARGET_FILE && \
    # 4. Corrige a chamada da função 'urlencode'
    sed -i 's/urllib.urlencode/urlparse.urlencode/g' $TARGET_FILE

# Volta para o usuário padrão do Superset
USER superset