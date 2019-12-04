#ideas de https://github.com/ComputoCienciasUniandes/FISI2028-201920/blob/master/ejercicios/19/JaimeForero_Ejercicio19.py y del mio entregado esa clase
import numpy as np
import matplotlib.pylab as plt
datos=np.loadtxt("month.dat")

def four(datos):
	n=len(datos)
	x=np.zeros(n, dtype=complex)
	for i in range(n):
		x[i]=0.0j
		for y in range(n):
			x[i]+=datos[y]*np.exp(-2.0*np.pi*1.0j/n)**(i*n)
	return x
a=four(datos[:200,3])
b=datos[:200,0]
c=np.linspace(np.pi/2,17*np.pi,1152)
plt.scatter(datos[:,0],datos[:,3], s=2)
plt.plot(datos[:,0],50*np.cos(c)+50)
plt.savefig("solar.png")
