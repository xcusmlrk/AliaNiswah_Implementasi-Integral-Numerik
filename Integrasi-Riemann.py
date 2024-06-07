import numpy as np
import time

# Fungsi f(x)
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi Riemann
def riemann_integral(N):
    a = 0.0
    b = 1.0
    h = (b - a) / N
    integral = 0.0
    for i in range(N):
        x_i = a + i * h
        integral += f(x_i)
    integral *= h
    return integral

# Fungsi untuk menghitung galat RMS
def rms_error(estimate, reference):
    return np.sqrt((estimate - reference) ** 2)

# Testing dengan variasi nilai N dan pengukuran waktu eksekusi
N_values = [10, 100, 1000, 10000]
pi_reference = 3.14159265358979323846

for N in N_values:
    start_time = time.time()
    pi_intergal = riemann_integral(N)
    execution_time = time.time() - start_time
    error = rms_error(pi_intergal, pi_reference)
    
    print(f"\nN: {N}")
    print(f"Integral Numerik: {pi_intergal}")
    print(f"RMS Error: {error}")
    print(f"Execution Time (s): {execution_time}")

