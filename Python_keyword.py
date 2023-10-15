import keyword
import os
import sys

print(f'You are running on {os.name} \nwith Python {sys.version}')

kw = keyword.kwlist
print("\nThe list of keywords: ")
#print(kw)

# flexible table of keywords
for i in range(len(kw)):
    if i%5 == 0: print()
    print(kw[i].ljust(10),end='')
    
#print(keyword.iskeyword('match'))      # False
#print(keyword.issoftkeyword('match'))  # True

skw = keyword.softkwlist    
print("\n\nThe list of SOFT keywords: ",skw)
# ['_', 'case', 'match'] with Python 3.11
# ['_', 'case', 'match', 'byte'] with Python 3.12

print(f'\nThere are {len(kw)} keywords and {len(skw)} soft keywords.')