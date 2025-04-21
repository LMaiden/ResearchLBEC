import numpy as np
import scipy.signal
import matplotlib.pylab as plt

def bell(x ,m ,s):
    return np.exp(-((x-m)/s)**2 /2)


#### Unit tests ####
def belltest():
    x = np.linspace(-5, 5, 1000)
    y = bell(x, 0, 1)
    plt.plot(x, y)
    plt.title("Bell function")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.show()
    
def main():
    belltest()
    
if __name__ == "__main__":
    main()