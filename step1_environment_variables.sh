#!/bin/sh

##Set Region
export REGION=us-east1

##FILES_SOURCE is set up as an environment variable
export FILES_SOURCE=dlt-sntmnt-poc-284722-files-source-1599614649

##FUNCTIONS_BUCKET to stage functions during deployment is set up as an environment variable
export FUNCTIONS_BUCKET=dlt-sntmnt-poc-284722-functions-1599614727

##Provision a Pub/Sub topic, called 'streaming_error_topic', to handle the error path.
export STREAMING_ERROR_TOPIC=streaming_error_topic

##Provision a Pub/Sub topic, called 'streaming_success_topic', to handle the success path.
export STREAMING_SUCCESS_TOPIC=streaming_success_topic

##Handle streaming errors
##Create your Cloud Storage bucket to store problematic files.
##FILES_ERROR is set up as an environment variable with a unique name for the bucket
##that stores error files.
export FILES_ERROR=dlt-sntmnt-poc-284722-files-error-1599615079

##Handle successful streaming
##Create your Coldline Cloud Storage bucket. FILES_SUCCESSis set up as an environment
##variable with a unique name for the bucket that stores success files.
export FILES_SUCCESS=dlt-sntmnt-poc-284722-files-success-1599615235
