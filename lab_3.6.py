import findspark
findspark.init()

import random
from datetime import datetime, timedelta
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType, FloatType

spark = SparkSession.builder \
    .appName("Synthetic Data Generation") \
    .getOrCreate()

#Настройки
num_records = 1000  # Количество строк
products = ["Телевизор", "Компьютер", "Телефон", "Наушники", "Монитор"] # Список возможных товаров
filepath = "data.csv" # Путь до файла

# Функция для генерации случайной даты в пределах последнего года
def random_date():
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    return start_date + (end_date - start_date) * random.random()

# Функция для генерации случайных данных
def generate_data(num_records):
    data = []
    for i in range(num_records):
        date = random_date()
        user_id = random.randint(1, 1000)
        product = random.choice(products)
        quantity = random.randint(1, 10)
        price = round(random.uniform(10, 1000), 2)
        data.append((date, user_id, product, quantity, price))
    return data

schema = StructType([
    StructField("Date", DateType(), True),
    StructField("UserID", IntegerType(), True),
    StructField("Product", StringType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("Price", FloatType(), True)
])

data = generate_data(num_records)

df = spark.createDataFrame(data, schema)

df.write.csv(filepath, header=True)

spark.stop()