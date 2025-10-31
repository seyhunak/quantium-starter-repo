#!/bin/bash

# Exit immediately if a command fails
set -e

# Activate your Python virtual environment
# Replace 'venv' with the name/path of your venv
source venv/bin/activate

# Run the test suite with pytest
pytest test_app.py

# Capture the exit code from pytest
EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

# Exit with the pytest exit code
exit $EXIT_CODE
