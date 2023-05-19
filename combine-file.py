#!/usr/bin/env python3
# Combine English version document and Chinese version document together
#
# You have a Chinese version document, 
# you can use Google translator (support .docx, .pdf, .pptx, or .xlsx) to translate into English
# You want to combine English version document and Chinese version document together
# such that you want to get the actual meaning.
#
def combine_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8',errors='ignore') as f1, open(file2, 'r', encoding='utf-8', errors='ignore') as f2, open(output_file, 'w', encoding='utf-8') as output:
        for line1, line2 in zip(f1, f2):
            output.write(line1.strip() + '\n' + line2.strip() + '\n')

            
file1 = 'myfile-en1.txt'
file2 = 'myfile-cn1.txt'
output_file = 'combinedfile.txt'

combine_files(file1, file2, output_file)
