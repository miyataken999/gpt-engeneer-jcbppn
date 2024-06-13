#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Run tests in parallel
pytest tests/

# Run the main script
python autoscriptest/main.py
