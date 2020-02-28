#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import binomial 
import seaborn as sns

#fix_time = []
#For T/F if go to fixation
# def simulation(N, s):
#     n1 = 1
#
#     while 0 < n1 < N:
#         n0 = N - n1
#         p1 = n1 * (1 + s) / (n0 + n1 * (1 + s))
#         n1 =np.random.binomial(N, p1)
#     return n1 == N
#

#Time it takes variant to go to fixation 
def simulation(p, N, s, repetitions=1000):
    N = int(2*N) #Don't want floats
    n1 = np.ones(repetitions) * (N*p) #making a large array
    T = np.empty_like(n1) #making large empty array
    update = (n1 > 0) & (n1 < N)
    t = 0
    
    while update.any():
        t += 1
        p = n1 * (1 + s) / (N + n1 * s) 
        n1[update] = np.random.binomial(N, p[update])
        T[update] = t
        update = (n1 > 0) & (n1 < N)

    return n1 == N, T #Where N is fixtation and T is time

#print("Fixate %", simulation(N=100, s=0))

#Defining variable for graphy 
fixations, times = simulation(p = 0.5, N=100, s=0, repetitions=1000)
fixation_prob = fixations.mean()
fixation_time = times[fixations].mean()
#Plotting fixation
fig, ax = plt.subplots()
sns.distplot(times[fixations], ax=ax)
ax.set_title("Histogram 1-Fixation")
ax.axvline(times[fixations].mean(), color='k', ls='--')
ax.set(xlabel='Fixation time', ylabel='Frequency')
fig.savefig("Histogram")

#By way of population size
repetitions = 1000
s = 0
Nrange = np.logspace(1, 4, 10, dtype=np.uint64)

def fix_time_simulation(N):
    fixations, times = simulation(p = 0.5, N=N, s= 0, repetitions= 1000)
    fixation_time_mean = times[fixations].mean()
    fixation_time_std =  times[fixations].std(ddof=1) / np.sqrt(repetitions)
    return fixation_time_mean, fixation_time_std

fix_time_sim = np.array([
    fix_time_simulation(N=N)
    for N in Nrange
])

def fixation_time_plot(N, mean, sem):
    fig, ax = plt.subplots(1, 1)

    ax.errorbar(x=N, y=mean, yerr=sem, 
                fmt='o', capsize=5, label='Simulation')

    ax.set(
        xlabel='Population size (N)',
        ylabel='Fixation time',
        xscale='log', 
        xlim=(0.5 * Nrange.min(), 1.5 * Nrange.max()),
    )
    return fig, ax
    
fixation_time_plot(Nrange, fix_time_sim[:,0], fix_time_sim[:,1]);
plt.show()
fig.savefig("Histogram")

#fixation under a range of different starting allele frequencies
fixation_times3 = {}
allele_freqs = [0.2,0.4,0.6,0.8]
​
for allele_freq in allele_freqs:
    fixation_times3[allele_freq] = []
    for i in range(100):
        fixation_times3[allele_freq].append(simulation(p=allele_freq, N=100, s=0, repetitions=1000))
    
mean3 = []
std_dev3 = []
for allele_freq in allele_freqs:
    mean3.append(np.mean(fixation_times3[allele_freq]))
    std_dev3.append(np.std(fixation_times3[allele_freq]))
​
​
fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(allele_freqs)+1)], mean3, yerr= std_dev3)
ax.set_xlabel("Starting Allele Frequency")
ax.set_xticks([x for x in range(1,len(allele_freqs)+1)])
ax.set_xticklabels(["0.2", "0.4", "0.6", "0.8"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 3")
fig.savefig("varyingallelefreq.png")
plt.show()

#selection coefficient vs time to fixation 
fixation_times4 = {}
selection_coeffs = [0,0.2,0.4,0.6,0.8,1]
​
for selection_coeff in selection_coeffs:
    fixation_times4[selection_coeff] = []
    for i in range(100):
        fixation_times4[selection_coeff].append(simulation(p=0.5, N=100, s=selection_coeff, repetitions=1000))
    
mean4 = []
std_dev4 = []
for selection_coeff in selection_coeffs:
    mean4.append(np.mean(fixation_times4[selection_coeff]))
    std_dev4.append(np.std(fixation_times4[selection_coeff]))
​
​
fig,ax = plt.subplots()
ax.bar([x for x in range(1,len(selection_coeffs)+1)], mean4, yerr= std_dev4)
ax.set_xlabel("Starting Selection Coefficient")
ax.set_xticks([x for x in range(1,len(selection_coeffs)+1)])
ax.set_xticklabels(["0","0.2", "0.4", "0.6", "0.8","1"])
ax.set_ylabel("Generations to Fixation")
plt.title("Plot 4")
fig.savefig("varyingselection_coeff.png")
plt.show()

