#!/bin/bash

# Run pylint and save the score
score=$(pylint test.py | awk '/Your code has been rated at/ {print $7}')

# Check if score is less than 5
if [ $(echo "$score < 5" | bc -l) -eq 1 ]; then
  echo "Pylint check-style violations detected. Quality gate not met"
  exit 1
else
  echo "Pylint score: $score"
  echo "Quality gate passed"
fi

