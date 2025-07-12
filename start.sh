#!/bin/bash

echo "Setting up Todo API..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start the server
echo "Starting the server..."
python main.py
