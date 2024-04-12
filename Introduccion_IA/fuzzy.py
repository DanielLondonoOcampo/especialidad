# %% Imports
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# %% Universo de discurso

# Antecedentes
universo_velocidad = np.arange(0, 1001, 1)
universo_angulo = np.arange(-10, 11, 0.1)

# Consecuentes
universo_posicion = np.arange(0, 11, 1)

# %%
velocidad = ctrl.Antecedent(universo_velocidad, "velocidad")
angulo = ctrl.Antecedent(universo_angulo, "angulo")
posicion = ctrl.Consequent(universo_posicion, "posicion")

# %% Fuzzyficar

# Velocidad
