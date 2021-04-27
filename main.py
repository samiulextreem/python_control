# changed something
import control
from control.xferfcn import tf
from control import matlab

import matplotlib.pyplot as plt
import numpy as np

Kp = 5
Ki = 3
Kd = 2
N = 3 ## filter coefficient


s = control.TransferFunction.s


sys_plant = (6  ) / (s**2 + 4* s + 5)
sys_PID = Kp + (Ki / s)  + (Kd * (N/ (1 + (N * (1/s)))) )
sys_series = control.series(sys_PID,sys_plant)



total_transfn = sys_series / (1 + sys_series)



print('H(plant) = ', sys_plant)
print('H(pid) =', sys_PID)
print('H(series) = ',sys_series)


T,Y = control.step_response(total_transfn,T= 30)
info = control.step_info(total_transfn,T=30)
print('Info ',info)

fig , ax = plt.subplots()
ax.grid(True)
ax.set_xlabel('Horizontal / xaxis')
ax.set_ylabel('Vertical / yaxis') 
ax.set_ylim(0,2)
ax.plot(T,Y)


plt.show()