#!/bin/sh

##Set Region
export REGION=us-east1

##FILES_SOURCE is set up as an environment variable
export FILES_SOURCE=tidal-glider-217500-files-source-1586544872

##FUNCTIONS_BUCKET to stage functions during deployment is set up as an environment variable
export FUNCTIONS_BUCKET=tidal-glider-217500-functions-1586545717

##Provision a Pub/Sub topic, called 'streaming_error_topic', to handle the error path.
export STREAMING_ERROR_TOPIC=streaming_error_topic

##Provision a Pub/Sub topic, called 'streaming_success_topic', to handle the success path.
export STREAMING_SUCCESS_TOPIC=streaming_success_topic

##Handle streaming errors
##Create your Cloud Storage bucket to store problematic files.
##FILES_ERROR is set up as an environment variable with a unique name for the bucket
##that stores error files.
export FILES_ERROR=tidal-glider-217500-files-error-1586547274

##Handle successful streaming
##Create your Coldline Cloud Storage bucket. FILES_SUCCESSis set up as an environment
##variable with a unique name for the bucket that stores success files.
export FILES_SUCCESS=tidal-glider-217500-files-success-1586547731
