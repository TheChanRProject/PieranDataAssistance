from sympy import *
from sympy.abc import x
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def build_base_function():
    return float(input("Write in a mathematical function using x for variable: "))
