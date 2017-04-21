# flask-sparkpi
A python implementation of SparkPi using Flask as a rest interface

This application is an example tutorial for the
[radanalytics.io](http://radanalytics.io) community. It is intended to be
used as a source-to-image application.

## Quick start

You should have access to an OpenShift cluster and be logged in with the
`oc` command line tool.

1. Create the necessary infrastructure objects
   ```bash
   oc create -f http://radanalytics.io/resources.yaml
   ```

1. Launch spring-sparkpi
   ```bash
   oc new-app --template oshinko-pyspark-build-dc  \
       -p APPLICATION_NAME=flask-sparkpi2 \
       -p GIT_URI=https://github.com/zmhassan/flask-pyspark-pi-example.git  \
       -p APP_FILE=app.py
   ```

1. Expose an external route
   ```bash
   oc expose svc/flask-sparkpi2
   ```

1. Visit the exposed URL with your browser or other HTTP tool, for example:
   ```bash
   $ curl http://`oc get routes/flask-sparkpi2 --template='{{.spec.host}}'`
   Pi is roughly 3.140480
   ```
