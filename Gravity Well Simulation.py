# PROJECT - 2

## Importing Libraries
import numpy as np
import matplotlib.pyplot as plt

## Intial Conditions
x = 10.00
y = 0.00
dx = 0.00
dy = 5.00
print("Initial Condition:\nx=%d, y=%d, x'=%d & y'=%d"%(int(x),int(y),int(dx),int(dy)))

## Finding the path of the object using the intial conditions
dt = float(input("Time interval = "))
n = float(input("Number of intervals = ")) 
print("Final time = ",dt*n)

path=np.empty((0,3),float)

for i in range(0,int(n)+1): 
    u = (x**2 + y**2)**0.5
    du = (x*dx + y*dy)/u
    z = (u - 1)**0.5
    dz = 1/(2*((u-1)**0.5))
    d2z = -1/(4*((u-1)**1.5))
    path=np.append(path,[[x,y,z]],axis=0)
    R = (((dx**2 + dy**2 - du**2)*dz/u + (du**2)*d2z + 9.8)/(u*(dz + 1/dz)))
    d2x = -x*R
    d2y = -y*R
    x = x + dx*dt + d2x*(dt**2/2)
    y = y + dy*dt + d2y*(dt**2/2)
    dx = dx + d2x*dt
    dy = dy + d2y*dt

print("\nPath taken By the object\n",path)

## Visualising the path taken the by the object in a 3D graph
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(path[:,0],path[:,1],path[:,2],linewidth=1.5,color='red')
ax.scatter(path[0,0],path[0,1],path[0,2], color = 'black')
plt.title('Path followed by the object is shown below\n\n')
plt.show()



