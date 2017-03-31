import re

patron=re.compile("\d\d\d")
print(patron.search("kilo912metro").group())