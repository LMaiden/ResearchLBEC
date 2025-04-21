import numpy as np
import Functions as F
import matplotlib.pylab as plt
T = 10
R = 10
size = 64;  mid = size // 2;  scale = 1;  cx, cy = 20, 20

y, x = np.ogrid[-mid:mid, -mid:mid]
D = (np.sqrt(x**2 + y**2)) / R
K = (D<1) * F.bell(D, 0.5, 0.15)
fK = np.fft.fft2(np.fft.fftshift(K / np.sum(K)))

# Print the kernel for verification
print(K)

plt.imshow(K, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Ring-Shaped Kernel")
plt.show()