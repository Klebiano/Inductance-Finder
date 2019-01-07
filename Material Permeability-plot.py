#Author: Klebiano Kennedy
#Year: 2019
import matplotlib.pyplot as plt
from numpy import linspace

# Program to plot the inductance by depending of the permeability of the material or Air Gap

N = 500                     #Number of Turns
Ac = 0.0009                 #meters^2       
lc = 0.3                    #lenght of the core in meters
uvac = 12.56637e-7          #Vacuum permeability
Rg = 442097                 #Ae/m

def Rec(ur):
    return (lc/(ur * uvac * Ac)+Rg)               #depending on the permeability of the material ur

def Rec2(g):
    return lc/(70000 * uvac * Ac)+(g/(uvac*Ac))   #depending on the length of the air gap:                                                                           lc/(70000*uvac*Ac)+(g/uvac*Ac)
                                                  #obs: values in centimeters for better visualization of the graph
ur = linspace(100, 100000, 50)
L1 = (N**2)/Rec(ur)                               

g = linspace(1e-4, 0.001, 40)
L2 = (N**2)/Rec2(g)

plt.subplots_adjust(hspace=0.4)
plt.figure(1)
plt.subplot(211)
plt.plot(ur, L1, '-g.')
plt.xlabel('Material Magnetic Permeability', fontweight='bold')
plt.ylabel('Inductance(H)', fontweight='bold')
plt.ticklabel_format(style='sci', axis='x', scilimits=(-3, 4))
plt.subplot(212)
plt.plot(g, L2, '-r.')
plt.xlabel('Air Gap Lenght (m)', fontweight='bold')
plt.ylabel('Inductance(H)', fontweight='bold')
plt.ticklabel_format(style='sci', axis='x', scilimits=(-3, 4))
plt.show()

