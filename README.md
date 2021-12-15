# Scraper for forecastercalculator.integral.co.nz
A scraper for [this site](https://forecastercalculator.integral.co.nz/) to simplify extracting reports.

## Setup
1. Install python3 (I'm using v3.9)
2. Install the requirements (in the project folder)
    pip install -r requirements.txt
3. Run the main.py file
    python main.py

Hopefully, a bunch of files from a test run should be dumped out.

## Usage

```python
from client import ApiClient
import simulate_command

client = ApiClient('<email>', '<password>')

# runs a simulation. the easiest way to get the commands you need are to have a look at the
# request the actual site uses, and copy them into the sample_commands file somewhere.
files = client.simulate(38.221, 176.07, simulate_command.PSEM_1T_COMMANDS)

# the simulation (if it worked) should return a list of files. You can download them using the client.
for file in files:
    client.download_file('test', file)

# For example, if you wanted only xlsx files
for file in files:
    if file[-5:] != '.xlsx': continue

    # You can specify a sub folder you want the file to go in - this should be useful if different lat/lngs (i.e.)
    # f'{custom_lat}_{custom_lng}' for a run name so the downloads for different runs go in different folders.
    client.download_file('excel_files', file)
```