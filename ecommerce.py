# Databricks notebook source


import os

os.environ["KAGGLE_USERNAME"] = "your_kaggle_username_here"
os.environ["KAGGLE_KEY"] = "your_kaggle_key_here"

print("Kaggle credentials configured!")


spark.sql("""
CREATE SCHEMA IF NOT EXISTS workspace.ecommerce
""")

spark.sql("""
CREATE VOLUME IF NOT EXISTS workspace.ecommerce.ecommerce_data
""")

df_n = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Nov.csv", 
                      header=True,
                      inferSchema=True)



df = spark.read.csv("/Volumes/workspace/ecommerce/ecommerce_data/2019-Oct.csv", 
                    header=True,
                    inferSchema=True)

print(f"October 2019 - Total Events: {df.count():,}")
print("\n" + "="*60)
print("SCHEMA:")
print("="*60)
df.printSchema()


print("\n" + "="*60)
print("SAMPLE DATA (First 5 rows):")
print("="*60)
df.show(5, truncate=False)



def load_ecommerce_data(month):
    path = f"/Volumes/workspace/ecommerce/ecommerce_data/2019-{month}.csv"
    return spark.read.csv(path, header=True, inferSchema=True)



# Load your data
events = load_ecommerce_data("Oct")

# Verify it's working
print(f"Ready to go! Loaded {events.count():,} events")
events.show(5)

# Create simple DataFrame
data = [("iPhone", 999), ("Samsung", 799), ("MacBook", 1299)]
df = spark.createDataFrame(data, ["product", "price"])
df.show()

# Filter expensive products
df.filter(df.price > 1000).show()


# Basic operations
events.select("event_type", "product_id", "price").show(10)
events.filter("price > 100").count()
events.groupBy("event_type").count().show()
top_brands = events.groupBy("brand").count().orderBy("count", ascending=False).limit(5)



from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Top 5 products by revenue
revenue = events.filter(F.col("event_type") == "purchase") \
    .groupBy("product_id") \
    .agg(F.sum("price").alias("revenue")) \
    .orderBy(F.desc("revenue")).limit(5)

revenue.show(5)

# Running total per user
window = Window.partitionBy("user_id").orderBy("event_time")
events.withColumn("cumulative_events", F.count("*").over(window))

# Conversion rate by category
conversion = events.groupBy("category_code") \
    .pivot("event_type") \
    .count() \
    .withColumn(
        "conversion_rate",
        F.col("purchase") / F.col("view") * 100
    )


conversion.show(10)