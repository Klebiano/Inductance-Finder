#Author: Klebiano Kennedy
#Year: 2018
import matplotlib.pyplot as plt
from numpy import linspace

'''Program to plot the inductance by modifying the permeability of the material used'''

N = 500 #Turns
Ac = 0.0009 #meters^2       
lc = 0.3 #meters            #lenght of the core
uvac = 12.56637e-7          #Vacuum permeability
Rg = 442097 #Ae/m

def Rec(ur):
    return (lc/(ur * uvac * Ac)+Rg) #depending on the permeability of the material ur

def Rec2(g):
    return lc/(70000 * uvac * Ac)+(g/(uvac*Ac)) #depending on the length of the air gap lc/(70000*uvac*Ac)+(g/uvac*Ac)
                                                #obs: values in centimeters for better visualization of the graph


#Example

ur = linspace(100, 100000, 100)
L1 = (N**2)/Rec(ur)

g = linspace(1e-4, 0.001, 80)
L2 = (N**2)/Rec2(g)

plt.figure(1)
plt.subplot(211)
plt.plot(ur, L1, '-g')
plt.xlabel('Material Magnetic Permeability')
plt.ylabel('Inductance(H)')

plt.subplot(212)
plt.plot(g, L2, '-r.')
plt.xlabel('Air Gap Lenght (m)')
plt.ylabel('Iinductance(H)')

plt.show()

