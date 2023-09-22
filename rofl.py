import os
import psutil
import socket
import threading
import numpy as np
import time

# Funktion zum 100%igen Auslasten der CPU
def fill_cpu():
    while True:
        pass

# Funktion zum 100%igen Auslasten des Arbeitsspeichers
def fill_memory():
    try:
        block_size = 1024 * 1024 * 100  # 100 MB
        while True:
            memory_chunk = bytearray(block_size)
    except MemoryError:
        print("Arbeitsspeicher ist vollständig ausgelastet.")

# Funktion zum 100%igen Auslasten der Festplatte/SSD
def fill_disk():
    try:
        while True:
            with open("fill_disk.txt", "wb") as f:
                f.write(os.urandom(1024 * 1024))  # Schreiben Sie 1 MB zufällige Daten
    except Exception as e:
        print("Festplatte/SSD ist vollständig ausgelastet.")

# Funktion zum 100%igen Auslasten des Netzwerks
def fill_network():
    try:
        while True:
            data = os.urandom(1024 * 1024)  # 1 MB zufällige Daten
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", 12345))
                s.sendall(data)
    except Exception as e:
        print("Netzwerk ist vollständig ausgelastet.")

# Funktion zum 100%igen Auslasten der GPU (NVIDIA CUDA)
def fill_gpu():
    try:
        import cupy as cp  # Erfordert die Installation von Cupy
        while True:
            x = cp.random.rand(1000, 1000)
            y = cp.random.rand(1000, 1000)
            z = cp.dot(x, y)
    except Exception as e:
        print("GPU ist vollständig ausgelastet.")

if __name__ == '__main__':
    num_threads = os.cpu_count()

    # CPU auslasten
    for _ in range(num_threads):
        thread = threading.Thread(target=fill_cpu)
        thread.start()

    # Arbeitsspeicher auslasten
    fill_memory()

    # Festplatte/SSD auslasten
    fill_disk()

    # Netzwerk auslasten
    fill_network()

    # GPU auslasten (NVIDIA CUDA)
    fill_gpu()
