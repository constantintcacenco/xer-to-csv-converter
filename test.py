import XerToCsvConverter as conv
import sys
import os

converter = conv.XerToCsvConverter()

input_path = sys.argv[1]
output_path = sys.argv[2]

entries = os.listdir(input_path)
for f in entries:

    # aditional check for xer format
    if f.endswith('.xer'):

        print("Parsing " + f + " ...")
        converter.read_xer(os.path.join(input_path,f))
        output_subdir = os.path.join(output_path,f.split('.')[0])
        
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)
        converter.convert_to_csv(output_subdir)

