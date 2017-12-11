import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt

randbin = np.loadtxt("neumann_long.txt", comments=' ')
print len(randbin[randbin>0])
print len(randbin[randbin<1])

#print number of bins
print "Number of random bits: "+str(len(randbin))

#binary resolution of unit interval
N = 8

binvals = np.array([2**i for i in range(N)])
#make length divisible by N
if len(randbin) % N != 0:
    randbin = randbin[:-(len(randbin) % N)]
#fold by 8 and sum binary values
randnums = (randbin.reshape([len(randbin)/N,N])*binvals).sum(-1)/(2.0**N)
#make length divisible by 2
if len(randnums) % 2 != 0:
    randnums = randnums[:-1]
#fold by 2
randvecs = randnums.reshape([len(randnums)/2,2])
print "Number of random vectors: "+str(len(randvecs))
#draw points and quarter circle
incirc = 0.0
x = np.linspace(0,1,100)
y = np.sqrt(1-x**2)
for vec in randvecs:
    if vec[0]**2 + vec[1]**2 < 1:
        incirc += 1.0
        plt.scatter(vec[0],vec[1], c='g')
    else:
        plt.scatter(vec[0],vec[1], c='b')
area = incirc/len(randvecs)
pi = 4*area

#generate from python mersenne twister
n = 100
numpis = np.zeros(n)
for i in range(n):
    numpbin = randint(2, size=10*len(randbin))
    numpnums = (numpbin.reshape([len(numpbin)/N,N])*binvals).sum(-1)/(2.0**N)
    if len(numpnums) % 2 != 0:
        numpnums = numpnums[:-1]
    numpvecs = numpnums.reshape([len(numpnums)/2,2])
    print "Number of numpy vectors: "+str(len(numpvecs))
    innump = 0.0
    for vec in numpvecs:
        if vec[0]**2 + vec[1]**2 < 1:
            innump += 1.0
    nump = innump/len(numpvecs)
    numpis[i] = 4*nump
numpi = numpis.mean()
numperr = numpis.std()

#plot all
print pi, numpi, numperr
plt.plot(x,y, 'r', label='pi~'+str(pi)[:5]+'('+str(numpi)[:5]+','+str(numperr)[:5]+')')
plt.ylim(0,1)
plt.xlim(0,1)
plt.axis('equal')
plt.title('Monte Carlo Approximation of circle, N='+str(len(randvecs)))
plt.legend()
plt.show()
