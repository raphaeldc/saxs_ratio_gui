import matplotlib.pyplot as plt
from crystal_lattice import *
from matplotlib.figure import Figure

def saxs_plot(files, strucs, first_peaks, log=True, begin=0, end=0, graph=True):
    f = Figure()
    a = f.add_subplot(111)
    files = np.array(files)
    strucs = np.array(strucs)
    first_peaks = np.array(first_peaks)
    if graph==True:
        for i in range(len(files)):
            data = np.genfromtxt(files[i], skip_header=begin, skip_footer=end, usecols=(0,1), names=['q','I'])
            if log==True:
                a.plot(data['q'], np.log10(data['I'])-i, "-", lw=1)
                a.set_ylabel('log(I) [a.u.]')
            else:
                a.plot(data['q'], data['I']-i, "-", lw=1)
                a.set_ylabel('I [a.u.]')
        for j in range(len(strucs)):
            print(np.around(2 * np.pi * crystals[strucs[j]][0] / first_peaks[j], decimals=3))
            if strucs[j] in ratios:
                for index in ratios[strucs[j]]:
                    a.axvline(x=first_peaks[j] * index, ls='-.', color=lines[j], lw=0.5)
        a.set_xlabel('q [nm^(-1)]')
        a.set_yticks([])
        #plt.show()
    else:
        for j in range(len(strucs)):
            print(np.around(2*np.pi*crystals[strucs[j]][0]/first_peaks[j],decimals=3))
    return f