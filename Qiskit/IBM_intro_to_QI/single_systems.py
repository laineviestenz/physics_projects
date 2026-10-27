#############################################################
#This File Has Been Moved to a Jupyter Notebook
#######################################################


from IPython.core.display_functions import display
from qiskit import __version__
import numpy as np
from qiskit.visualization import array_to_latex
from qiskit.quantum_info import Statevector

"""Vector Math"""
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])
print(ket0 / 2 + ket1 / 2)

"""Matrix Math"""
M1 = np.array([[1,1], [0,0]])
M2 = np.array([[1,0],[0,1]])
M = M1 / 2 + M2 / 2
print(M)

"""Matrix Multiplication"""
print(f"M1@M2 = {M1@M2}")

u = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
v = Statevector([(1+2.0j) / 3, -2/3])
w = Statevector([1/3, 2/3])

display(u.draw("text"))
display(u.draw("latex_source"))

"""check for valid quantum state vector (Euclidian norm = 1)"""
display(u.is_valid())
display(w.is_valid())