from pyspark.sql import SparkSession


from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext(appName="Phoenix test")
sqlContext = SQLContext(sc)
table = sqlContext.read.format("org.apache.phoenix.spark").option("table", "TESTE_PHOENIX").option("zkUrl", "zookeeper:2181").load()
print(table.columns)

sc.stop()