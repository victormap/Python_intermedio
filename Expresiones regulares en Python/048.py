import re

if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
    print("Se encontró el patrón")