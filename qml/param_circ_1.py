from qiskit.circuit import QuantumCircuit, Parameter
from qiskit import Aer, execute
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator', shots=200)

qc = QuantumCircuit(2)
theta_param = Parameter("theta")
qc.rz(theta_param,0)
qc.measure_all()

bound_qc = qc.bind_parameters({theta_param: 0.5})


result = execute(bound_qc, simulator).result()

print(result.get_counts(bound_qc))

qc.draw("mpl")

from qiskit.circuit.library import ZZFeatureMap

simulator_zz = Aer.get_backend('qasm_simulator', shots=200)
fmap = ZZFeatureMap(2, reps=2)
qc_zz = QuantumCircuit(2)
qc_zz.append(fmap, range(2))
qc_zz.h(0)
qc_zz.cx(0,1)
qc_zz.measure_all()
params_fmap = fmap.parameters
param_names = [str(param) for param in params_fmap]
print(param_names)

fmap.decompose().draw("mpl")
qc_zz.decompose().draw("mpl")

plt.show()
params = [Parameter('x[{}]'.format(i)) for i in range(fmap.num_parameters)]
print(params)
values = [0.1, 0.2]
print(params_fmap)
dict_fmap = {params_fmap[0]: 0.1, params_fmap[1]: 0.2}
#bound_circuits = [qc_zz.bind_parameters(dict(zip(params, values)))]
print('bound_circuits')
bound_circuits = qc_zz.bind_parameters(dict_fmap)

print('result_zz')
result_zz = execute(bound_circuits, simulator_zz).result()

print(result_zz.get_counts(bound_circuits))


