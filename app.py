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

    scale = int(request.args.get('scale', 2))
    n = 100000 * scale

    def f(_):
        x = random()
        y = random()
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(
        xrange(1, n + 1), scale).map(f).reduce(add)
    response = "Pi is roughly {}".format(4.0 * count / n)

    spark.stop()

    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
