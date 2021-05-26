from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
from qiskit_textbook.widgets import binary_widget

binary_widget(n=5)
n = 8
n_c = n
n_p = n

qc = QuantumCircuit(n_c, n_p)

for j in range(n):
    qc.measure(j,j)

qc.draw()
