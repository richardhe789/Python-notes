# Some csv format data files have large size.
# This program is to split a csv file into a few small files.
# Then you can read the small csv file on Windows with small memory size or open with Notepad.
# Encoding:utf-8   
# Support unicode filename and file content

import io
import sys
n = len(sys.argv)
   
if n==3:
    myfilename = sys.argv[1]
    result = myfilename.rsplit('.', 1)[0]    
    lines_per_file = int(sys.argv[2])
else:
    print("python split_csv_file.py csv_filename lines_per_file\n E.g. python split_csv_file.py aa.csv 30000")
    sys.exit()

smallfile = None
i=1

with io.open(myfilename, 'r', encoding='utf8') as largefile:
    for line_no, line in enumerate(largefile):
        if line_no % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = result +  '{num:02d}.csv'.format(num=i)
            i = i + 1
            smallfile = io.open(small_filename, "w", encoding='utf8')
        smallfile.write(line)
    if smallfile:
        smallfile.close()

print("Done")
# C:\python\python split_csv_file.py  csv_filename lines_per_file      
