# xer-to-csv-converter
This script converts XER files to CSV

# test file
test.py file will parse all the ".xer" files from the input_dir location and will parse them to the output_dir directory. For each table from XER file a separate CSV file will be created (within a subdirectory with the name of the original XER file).
usage: 
```
python test.py input_dir output_dir
```
e.g: 
```
python test.py test_files output_dir
```
where test_files=directory with all XER files and out_putdir=output(CSVs) location
# installation
```
pip install xertocsv
```
https://pypi.org/project/xertocsv/
