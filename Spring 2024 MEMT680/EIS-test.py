import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

R_ohmic = 0
C_d = 0.1
R_ct = 50
omega = 0.01

w = 10**(np.linspace(np.log10(1E6),np.log10(0.01)))
# Z_real = R_ohmic + (R_ct + omega*w**(-0.5))/((1+C_d*omega*w**0.5)**2+w**2*C_d**2*(R_ct + omega*w**-0.5)**2)
# Z_imag = (w*C_d*(R_ct+omega*w**-0.5)**2 + omega*w**-0.5*(w**0.5*C_d*omega + 1))/((1+w**0.5*C_d*omega)**2 + w**2*C_d**2*(R_ct + omega*w**-0.5)**2)
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

for w in w:
    Z_real = R_ohmic + R_ct/(1+w**2*C_d**2*R_ct**2)
    Z_imag = (w*C_d*R_ct**2)/(1+w**2*C_d**2*R_ct**2)
    # Z_real = 5
    # Z_imag = 1/(2*np.pi*w*C_d)
    ax1.scatter(Z_real, Z_imag, color = 'k', s=20)

ax1.set_xlabel('Z_real (Ohms)')
ax1.set_ylabel('-Z_imag (Ohms)')
ax1.set_xlim(-2, 65)
ax1.set_ylim(-2,65)

plt.show()
