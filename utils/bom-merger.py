import argparse, os, csv
import pandas as pd 

# Author: Nemo Andrea, 2023
# Must run as Python 3.5+

"""
Simple utility that combines smaller BOM (bill of materials) file into one bigger BOM file.
The combined BOM is useful for guaging total cost and variety of suppliers,
but individual BOMs for subassemblies are more manageable and will also facilitate 
modular adoption of a project (maybe you only want to use one subassembly for your own project)

It assumes you have CSV BOM files for subassemblies that contain "BOM-" or "-BOM" in their filename.
BOM files should follow the columns laid out in bom-template.csv in the same directory as this
script. Example name "BOM-subassembly.csv", "cool-pcb-design-BOM.csv" 

In addition, the template column names "Name" and "Price Total" should be present to generate the total
project cost. You can change the names around, but you must then change the names to match below.
"""

template = pd.read_csv('bom-template.csv')
print(template)

# set the working directory to be the repository root
# the current working directory will always be the start of the SEARCH for BOM files
os.chdir("..")

## Set up a parser

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true",
                    help="Search for all BOM files but no not generate/change the combined BOM file")
parser.add_argument("-p", "--path", 
                    help="override the default location for the combined BOM file")
parser.add_argument("-s", "--skiptotal", action="store_true", 
                    help="Do not add a final row to project BOM with total cost")
args = parser.parse_args()

## Handle paths

if args.path is not None:  # someone wants to set a different home directory, 
    print(f"changing path is not yet supported, it is currently set to {os.getcwd()} dd")
    savepath = os.getcwd()
else:  
    # default save location (root of repository)
    savepath = os.getcwd()

## Looks for BOMs

from pathlib import Path

def collect_BOMs(target, results=[]):
    """Simple recursive function that looks for BOM files.

    Returns:
        list of BOMs as Pandas dataframes
    """
    for item in Path(target).glob("*"):
        if not item.is_file():  # it is a directory, search it
            collect_BOMs(item, results)
        else:  # it is a file, lets see if it a BOM file
            if (item.suffix == ".csv") or (item.suffix == ".CSV"):
                if ("BOM-" in item.name) or ("-BOM" in item.name):
                    print(f"> Found BOM in: {item}")
                    results.append(pd.read_csv(item))
    return results

BOM_files = collect_BOMs(os.getcwd())

if not args.test:
    print("\n Combining subassembly BOMs into project BOM...")
    
    project_BOM = pd.concat(BOM_files)  

    if not args.skiptotal:
        total_cost = project_BOM['Price Total'].sum()
        project_BOM = project_BOM.append(pd.Series(dtype="float64"), ignore_index=True)  # empty line
        project_BOM = project_BOM.append({"Name":"total", "Price Total":total_cost}, ignore_index=True)

    bompath = os.path.join(savepath, "BOM.csv")
    project_BOM.to_csv(bompath, index=False)

    print(f"\n>>> Done! Stored project BOM at {bompath}")    
else: 
    print("\n Script run in test mode, ignoring project BOM creation/modification")