# main.py
import konversi

# Konversi Celcius ke Fahrenheit
c = float(input("Masukkan suhu Celcius: "))
print("Suhu dalam Fahrenheit =", konversi.c_to_f(c))

# Konversi Fahrenheit ke Celcius
f = float(input("Masukkan suhu Fahrenheit: "))
print("Suhu dalam Celcius =", konversi.f_to_c(f))
