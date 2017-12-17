import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from numpy.random import binomial

atoms = {'Rn222': 1000000,
         'Po218': 0,
         'Pb214': 0,
         'Bi214': 0,
         'Pb210': 0}

atoms_over_time = []

atoms_over_time.append(atoms.copy())
for x in range(10000):
    Rn222_Po218 = binomial(atoms['Rn222'], 0.000126)
    Po218_Pb214 = binomial(atoms['Po218'], 0.001240)
    Pb214_Bi214 = binomial(atoms['Pb214'], 0.003450)
    Bi214_Pb210 = binomial(atoms['Bi214'], 0.012046)

    atoms['Rn222'] -= Rn222_Po218
    atoms['Po218'] += Rn222_Po218

    atoms['Po218'] -= Po218_Pb214
    atoms['Pb214'] += Po218_Pb214

    atoms['Pb214'] -= Pb214_Bi214
    atoms['Bi214'] += Pb214_Bi214

    atoms['Bi214'] -= Bi214_Pb210
    atoms['Pb210'] += Bi214_Pb210
    atoms_over_time.append(atoms.copy())
v = dict(zip(atoms_over_time[0], zip(*[d.values() for d in atoms_over_time])))
plt.plot(v['Rn222'])
plt.plot(v['Po218'])
plt.plot(v['Pb214'])
plt.plot(v['Bi214'])
plt.plot(v['Pb210'])
plt.show()