import zipfile
from zipfile import ZipFile
with zipfile.ZipFile('archivo.zip','w') as fzip:
    fzip.write('Python.docx')
    fzip.write('Archivo.docx')
    fzip.write('python1.jpg')
    fzip.printdir()
    fzip.extractall()