# Materi: Input/Output
name = input("Masukkan nama Anda: ")
print("Halo,", name, "! Selamat datang di program Python.")

# Output 
# Masukkan nama Anda: John
# Halo, John! Selamat datang di program Python.

# Materi: Argument Specifier
age = 25
height = 175.5
print("Umur: %d tahun, Tinggi: %.2f cm" % (age, height))

# Output
# Umur: 25 tahun, Tinggi: 175.50 cm

# Materi: Command-line Arguments
import sys

arguments = sys.argv
print("Jumlah argumen:", len(arguments))
print("Argumen-argumen:", arguments)

# Output
# Jumlah argumen: 1
# Argumen-argumen: ['script_name.py']

# Materi: Dynamic Typing pada Python
x = 5
print("Nilai x:", x, "Tipe x:", type(x))

x = "Hello"
print("Nilai x:", x, "Tipe x:", type(x))

# Output
# Nilai x: 5 Tipe x: <class 'int'>
# Nilai x: Hello Tipe x: <class 'str'>

# Materi: Duck Typing
x = 333

# len(x)  # TypeError: object of type 'int' has no len()

# Materi: Transformasi Angka
x = 1
type(x) # Output: <type 'int'>

str(x).zfill(5)
print(x)

# Traceback (most recent call last):
#  File "script_name.py", line 23, in <module>
#    str(x).zfill(5)
# AttributeError: 'str' object has no attribute 'zfill'


