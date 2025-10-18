import pandas as pd
from typing import Dict

def csv2hivemetadata(df: pd.DataFrame, table_location: str, table_name: str, delimiter: str) -> str:

    type_mapping: Dict[str, str] = {
        'int64': 'BIGINT',
        'object': 'STRING',
        'float64': 'DOUBLE',
        'bool': 'BOOLEAN',
        'datetime64[ns]': 'TIMESTAMP',
        'int32': 'INT'
    }

    column_definitions = ',\n'.join([
        f'  {column} {type_mapping.get(str(df[column].dtype), "STRING")}'
        for column in df.columns
    ])

    return  f"""CREATE EXTERNAL TABLE {table_name} (
{column_definitions}
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '{delimiter}'
STORED AS TEXTFILE
LOCATION '{table_location}';"""

# Criando um DataFrame de exemplo para testar a função
data = {'id': [1, 2, 3], 'nome': ['Carlos', 'Galatea', 'Gideon'], 'valor': [10.5, 20.1, 30], 'ativo': [True, False, True]}
df = pd.DataFrame(data)

print(csv2hivemetadata(df, '/datalake/raw/clientes_exemplo/', 'clientes_exemplo', ','))