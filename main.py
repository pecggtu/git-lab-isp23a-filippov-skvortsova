"""Учебный калькулятор."""

def calculate(a, b, operation):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Операнды должны быть числами")
    if operation == "+":
        return add(a, b)
    if operation == "-":
        return subtract(a, b)
    raise ValueError("Неизвестная операция")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
