from qiskit import __version__
import numpy as np

"""Test matrix multiplication"""
M1 = np.array([[1,0], [0,1]])
ket0 = np.array([[1], [0]])

print(M1 @ ket0)

print("empty")
