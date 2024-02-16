# %%
import sympy as sp
# %%
x, y, z, w = sp.symbols('x y z w')
# %%
icognitas = sp.Matrix([[x, y], [z, w]])
# %%
num = sp.Matrix([[2,3], [3,4]])
# %%
resul = sp.Matrix([[1, 0], [0, 1]])
# %%
icognitas * num