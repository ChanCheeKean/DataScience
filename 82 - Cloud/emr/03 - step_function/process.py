from pyspark.sql.functions import year, \
    month, dayofmonth


def transform(df):
    return df.withColumn('year', year('created_at')). \
        withColumn('month', month('created_at')). \
        withColumn('day', dayofmonth('created_at'))
