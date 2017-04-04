import bz2

cadena=b"Cadena Cadena Cadena Cadena"
cadena_c=bz2.compress(cadena)

print(bz2.decompress(cadena_c))