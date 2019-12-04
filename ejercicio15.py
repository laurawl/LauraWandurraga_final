#Ideas de: https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/09/ForeroJaime_Ejercicio_09.py, de: https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/14/ForeroJaime_Ejercicio_14.py y mi codigo entregado para el ejercicio 9 que no esta en un repositorio entonces no tiene link 
import numpy as np
import matplotlib.pylab as plt

datos=np.loadtxt("valores.txt")

def prob(sig,x):
    a=np.exp(-0.5*x**2/sig**2)/(sig*np.sqrt(2*np.pi))
    return a
def sig(datos,sigma):
    b=1.0
    for x in datos:
        b=b*prob(sigma,x)
    return b
def metro(datos,puntos,delta):
    c=[np.random.random()]
    for i in range(1,puntos):
        prop=c[i-1]+(np.random.random()-0.5)*delta
        d=min(1,(sig(datos,prop)/sig(datos,c[i-1])))
        e=np.random.random()
        if(e<d):
            c.append(prop)
        else:
            c.append(c[i-1])
    return np.array(c)

plt.figure()
f=metro(datos,10**5,2.0)
g=np.mean(f)
h=np.std(f)
j=str(g)
k=str(h)
i="Valor medio es: "+j+" La desviación estándar es: "+k
plt.hist(f)
plt.xlabel(r'$\sigma$')
plt.ylabel(r'P($\sigma$|x_k)')
plt.title(i,fontsize=10)
plt.savefig("sigma.png")
print(g)
