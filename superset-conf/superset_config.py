import subprocess
import sys
# subprocess.check_call( ["pip", "install", 'sqlalchemy==1.2.18'])
# SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://superset:superset@superset-db:5432/superset"
#POSTGRES_DB="superset"
CYPRESS_CONFIG="false"
DATABASE_DIALECT="postgresql"
SQLALCHEMY_DATABASE_URI="postgresql://superset:superset@superset-db:5432/superset"
SUPERSET_SECRET_KEY="uma_chave_secreta_super_longa_e_aleatoria"
CACHE_CONFIG_CACHE_TYPE="redis"
CACHE_CONFIG_CACHE_REDIS_URL="redis://superset-redis:6379/0"
#subprocess.check_call( ["superset", "db", 'upgrade'])
