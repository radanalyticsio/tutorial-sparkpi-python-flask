import os

from flask import Flask
from flask import request
from pyspark.sql import SparkSession


app = Flask(__name__)


def produce_pi(scale):
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()
    n = 100000 * scale

    def f(_):
        from random import random
        x = random()
        y = random()
        return 1 if x ** 2 + y ** 2 <= 1 else 0

    count = spark.sparkContext.parallelize(
        xrange(1, n + 1), scale).map(f).reduce(lambda x, y: x + y)
    spark.stop()
    pi = 4.0 * count / n
    return pi


@app.route("/")
def index():
    return "Python Flask SparkPi server running. Add the 'sparkpi' route to this URL to invoke the app."


@app.route("/sparkpi")
def sparkpi():
    scale = int(request.args.get('scale', 2))
    pi = produce_pi(scale)
    response = "Pi is roughly {}".format(pi)

    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
