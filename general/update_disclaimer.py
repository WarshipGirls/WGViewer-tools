# Update disclaimer as the same format as LICENSE

import textwrap
import sys

assert(len(sys.argv)==2)
disclaimer_path = sys.argv[1]
wrapper = textwrap.TextWrapper(width=80)

with open(disclaimer_path, 'r') as f:
    text = f.read()

paragraphs = text.split('\n\n')
output = ""
for para in paragraphs:
    word_list = wrapper.wrap(text=para)
    for element in word_list:
        output += element
        output += "  \n"  # markdown 2 trailing whitespaces
    output += "\n"
output = output[:-1]

assert(output != "")
with open(disclaimer_path, 'w') as f:
    f.write(output)