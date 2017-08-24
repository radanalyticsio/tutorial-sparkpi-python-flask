from random import random
from operator import add
import os

from flask import Flask
from flask import request
from pyspark.sql import SparkSession


app = Flask(__name__)


@app.route("/")
def index():
    return "Python Flask SparkPi server running. Add the 'sparkpi' route to this URL to invoke the app."


@app.route("/sparkpi")
def sparkpi():
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()

    partitions = int(request.args.get('partitions', 2))
    n = 100000 * partitions

    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(
        xrange(1, n + 1), partitions).map(f).reduce(add)
    response = "Pi is roughly {}".format(4.0 * count / n)

    spark.stop()

    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
