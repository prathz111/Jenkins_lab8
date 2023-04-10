#!/bin/bash

# Run pylint and capture its exit code
pylint_exit_code=$(pylint --exit-zero /home/netman/Documents/Lab9/lab9_py/netman_netconf_obj2.py)

# Check if pylint exited with a non-zero exit code
if [[ $pylint_exit_code -ne 0 ]]; then
    # Check if the quality gate of 5 was not met
    if [[ $pylint_exit_code -ge 5 ]]; then
        echo "Pylint check-style violations detected. Quality gate not met."
        exit 1
    else
        echo "Pylint check-style violations detected. Quality gate met. Proceeding with pipeline."
    fi
else
    echo "No Pylint check-style violations detected. Proceeding with pipeline."
fi

