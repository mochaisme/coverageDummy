# my_project.py

def add(a, b):
    """Menambahkan dua angka."""
    return a + b

def subtract(a, b):
    """Mengurangkan dua angka."""
    return a - b

def multiply(a, b):
    """Mengalikan dua angka."""
    return a * b

def divide(a, b):
    """Membagi dua angka, menangani pembagian dengan nol."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
