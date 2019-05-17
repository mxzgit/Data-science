import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def graphRawFx():
    
    date,bid,ask = np.loadtxt('../Data/GBPUSD/GBPUSD1d.txt', unpack=True, delimiter=',',converters={0:bytespdate2num('%Y%m%d%H%M%S')})

    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan = 40, colspan=40)

    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H-%M-%S'))
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)


    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    graphRawFx()