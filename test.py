from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import math

def quantum_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    backend = AerSimulator()
    compiled_circuit = transpile(qc, backend)
    job = backend.run(compiled_circuit, shots=1)
    result = job.result()
    counts = result.get_counts()
    return int(list(counts.keys())[0])

def quantum_random_number(max_value):
    num_bits = math.ceil(math.log2(max_value))
    while True:
        bits = [str(quantum_bit()) for _ in range(num_bits)]
        number = int("".join(bits), 2)
        if 1 <= number <= max_value:
            return number

def roll_quantum_dice(sides=6):
    return quantum_random_number(sides)

# Number of dice rolls
num_rolls = 5

# Array to store results
results = []

for _ in range(num_rolls):
    roll = roll_quantum_dice(6)
    results.append(roll)

print("Quantum dice rolls:", results)
