#import libraries for 3D plotting
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#Coordinates for the constellation are given. Pulled from a paper by Nottingham Trent University.
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]

#what does the constellation look like in 2D?
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(x,y)
#does not look like Orion at all
#plot it in 3D
ax2 = fig.add_subplot(212, projection = "3d")
ax2.scatter(x,y,z, color = 'White')
ax2.set_facecolor('Black')
fig.tight_layout()
plt.savefig('starcharts.png')

#this is a test comment