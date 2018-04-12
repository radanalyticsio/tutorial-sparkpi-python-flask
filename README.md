# SparkPi
A python implementation of SparkPi using Flask as an HTTP interface

This application is an example tutorial for the
[radanalytics.io](https://radanalytics.io) community. It is intended to be
used as a source-to-image application.

## Quick start

You should have access to an OpenShift cluster and be logged in with the
`oc` command line tool.

1. Create the necessary infrastructure objects
   ```bash
   oc create -f https://radanalytics.io/resources.yaml
   ```

1. Launch sparkpi
   ```bash
   oc new-app --template oshinko-python-spark-build-dc  \
       -p APPLICATION_NAME=sparkpi \
       -p GIT_URI=https://github.com/radanalyticsio/tutorial-sparkpi-python-flask
   ```

1. Expose an external route
   ```bash
   oc expose svc/sparkpi
   ```

1. Visit the exposed URL with your browser or other HTTP tool, for example:
   ```bash
   $ curl http://`oc get routes/sparkpi --template='{{.spec.host}}'`
   Python Flask SparkPi server running. Add the 'sparkpi' route to this URL to invoke the app.

   $ curl http://`oc get routes/sparkpi --template='{{.spec.host}}'`/sparkpi
   Pi is roughly 3.140480
   ```

### Optional parameter

If you would like to change the number of samples that are used to calculate
Pi, you can specify them by adding the `scale` argument to your request
, for example:

```bash
$ curl http://`oc get routes/sparkpi --template='{{.spec.host}}'`/sparkpi?scale=10
Pi is roughly 3.141749
```
