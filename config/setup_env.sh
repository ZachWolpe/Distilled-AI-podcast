#!/bin/bash

# Define the full path for the environment

ENV_NAME="spark-podcast"
ENV_CONFIG="config/environment.yml"

Check if the conda environment already exists
if conda env list | grep -q "$ENV_NAME"; then
    echo "Updating conda environment..."
    conda env update -f $ENV_CONFIG
else
    echo "Creating conda environment..."
    conda env create -f $ENV_CONFIG
fi


