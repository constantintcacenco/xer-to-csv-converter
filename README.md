# xer2csv
This package provides tools to convert XER files to CSV files.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [xer2csv](https://pypi.org/project/xer2csv/).
```
pip install xer2csv
```

## Testing
test.py file will parse all the ".xer" files from the `input_dir` location and will parse them to the `output_dir` directory. For each table from XER file a separate CSV file will be created (within a subdirectory with the name of the original XER file).
usage: 
```
python test.py input_dir output_dir
```

## License
[MIT](https://choosealicense.com/licenses/mit/)