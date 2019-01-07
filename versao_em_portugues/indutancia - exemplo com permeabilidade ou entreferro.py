import matplotlib.pyplot as plt
from numpy import linspace
'''
          Programa para plotar a indutância dependendo da permeabilidade do material ou comprimento do entreferro 
'''
N = 500               #numero de espiras
Ac = 0.0009           #metros^2
lc = 0.3              #metros                        #dados iniciais
uvac = 12.56637e-7    #Permeabilidade do vácuo
Rg = 442097           #Ae/m

def Rec(ur):
    return (lc/(ur * uvac * Ac)+Rg)                   #em função da permeabilidade do material ur
def Rec2(g):
    return (lc/(70000 * uvac * Ac))+(g/(uvac*Ac))       #em função do comprimento do entreferro:                                                                           lc/(70000*uvac*Ac)+(g/uvac*Ac)
                                                      #obs: valores em cm para melhor vizualização do gráfico
ur = linspace(100, 100000, 50)
L1 = (N**2)/Rec(ur)
g = linspace(1e-4, 0.001, 40)
L2 = (N**2)/Rec2(g)
'''                                                Gráfico                                                      '''
plt.subplots_adjust(hspace=0.4)
plt.subplot(211)
plt.plot(ur, L1, '-g.')
plt.xlabel('Permeabilidade magnética do material', fontweight='bold')
plt.ylabel('Indutância(H)', fontweight='bold')
plt.ticklabel_format(style='sci', axis='x', scilimits=(-3, 4))
plt.subplot(212)
plt.plot(g, L2, '-r.')
plt.xlabel('Comprimento do entreferro (m)', fontweight='bold')
plt.ylabel('Indutância(H)', fontweight='bold')
plt.ticklabel_format(style='sci', axis='x', scilimits=(-3, 4))
plt.show()