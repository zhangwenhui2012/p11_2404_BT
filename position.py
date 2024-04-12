import numpy as np
import h5py
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

PREFIX = "/gpfs/cfel/user/zakharom/P11-April-logs/test/"

with h5py.File(PREFIX+'Scan_493_ifers.h5','r') as df:
     val = df['values_per_point'][...]
     x_cord = df['Ifer-X'][:]
     y_cord = df['Ifer-Y'][:]

Ny = int(x_cord.shape[1]/val)
Nx = x_cord.shape[0]
x_avg = np.zeros((Nx, Ny))
y_avg = np.zeros((Nx, Ny))

N_capture = Ny
for k in range(Nx):
    xi = x_cord[k,:]
    yi = y_cord[k,:]
    x_avg[k] = np.mean(xi.reshape(N_capture, val), axis=1)
    y_avg[k] = np.mean(yi.reshape(N_capture, val), axis=1)
    
# Abhi random numbers, BT mein iski jagah pe detector data ke signals ka sum hoga...    
F = np.random.randint(1,101, size=(Nx,Ny))

plt.figure(1)
aspect_ratio = F.shape[1] / F.shape[0]
plt.imshow(F, extent=[x_cord.max(), x_cord.min(), y_cord.max(), y_cord.min()], aspect=aspect_ratio, origin='lower', cmap='viridis')
plt.colorbar()

plt.figure(2)
plt.imshow(F, aspect= aspect_ratio, origin = 'lower')
plt.title('Click here in the image')
pt_s = plt.ginput(1)
plt.show()

xidx = int( np.round(pt_s[0][1]))
yidx = int( np.round(pt_s[0][1]))
print(pt_s)
print(len(pt_s))
print(f' x and y co-ordinates are: {x_avg[xidx, yidx]} and {y_avg[xidx, yidx]}')
