#!/bin/bash

pylint_exit_code=$(pylint /home/netman/Documents/Lab9/lab9_py/netman_netconf_obj2.py | tee /dev/tty | awk '/Your code has been rated at/ {print $7}')
echo "Pylint score: $pylint_exit_code"

if [ "$pylint_exit_code" -lt "5" ]; then
  echo "Quality gate not met"
  exit 1
else
  echo "Quality gate passed"
fi

