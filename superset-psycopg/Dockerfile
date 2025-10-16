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
RUN apt-get update && apt-get install -y --no-install-recommends gcc heimdal-dev && rm -rf /var/lib/apt/lists/*

# Pil e Drivers para os principais bancos. Infelizmente a instalação do driver mysqlclient não foi possível no momento
RUN uv pip install Pillow psycopg2 sqlalchemy-phoenix phoenixdb pyhive oracledb pymssql 