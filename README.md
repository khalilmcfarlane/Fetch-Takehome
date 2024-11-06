# Take Home Assignment for Fetch

## Overview
Fetch Take-Home Exercise — Site Reliability Engineering Overview: Implement a program to check the health of a set of HTTP endpoints. A basic overview is given in this section. Additional details are provided in the Prompt section. Read an input argument to a file path with a list of HTTP endpoints in YAML format. Test the health of the endpoints every 15 seconds. Keep track of the availability percentage of the HTTP domain names being monitored by the program. Log the cumulative availability percentage for each domain to the console after the completion of each 15-second test cycle.
See [Health-check.pdf](https://github.com/khalilmcfarlane/Fetch-Takehome/blob/main/health-check.pdf) for more info.

## Steps to run
1. `python main.py <test.yaml>`
   1. **NOTE:** If using Mac, run `python3 main.py <yaml_file>`
   2. Works on any YAML file.

## Dependencies
1. `python version >= 3.5`
2. `pip install pyyaml`
3. `pip install requests`
<br>
Use `pip3` instead if on Mac.


**NOTE**: Typing module is used to support lower python versions.

Code follows PEP 8 Standard.