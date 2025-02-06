#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Download Miniconda installer
MINICONDA_SCRIPT="Miniconda3-latest-Linux-x86_64.sh"
if [ ! -f "$MINICONDA_SCRIPT" ]; then
  echo "Downloading Miniconda installer..."
  wget https://repo.anaconda.com/miniconda/$MINICONDA_SCRIPT
fi

# Install Miniconda silently
bash $MINICONDA_SCRIPT -b -p "$HOME/miniconda"

# Initialize Conda
source "$HOME/miniconda/bin/activate"
conda init

# Create a Python 3.11 virtual environment
ENV_NAME="myenv"
echo "Creating a Python 3.11 virtual environment..."
conda create -n $ENV_NAME python=3.11 -y

# Activate the virtual environment
conda activate $ENV_NAME
