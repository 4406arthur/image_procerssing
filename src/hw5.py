import cv2
import numpy as np
from matplotlib import pyplot as plt
import cmath #lib provide api to operate complex math

def compute_dft_complex(input):
    n = len(input)
    output = [complex(0)] * n
    for k in range(n):  #for generate output list
        s = complex(0)
        for t in range(n):  # calculate by formula
            s += input[t] * cmath.exp(-2j*cmath.pi*t*k/n)
        output[k] = s
    return output


img = cv2.imread('google-icon.png', 0)

res = compute_dft_complex(img)

cv2_res = cv2.dft(np.float32(img))


res_shift = np.fft.fftshift(res)
cv2_res_shift = np.fft.fftshift(cv2_res)

magnitude_spectrum = 20*np.log(np.abs(res_shift))
cv2_magnitude_spectrum =  20*np.log(np.abs(cv2_res_shift))


plt.subplot(121),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('after compute_dft_complex()'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cv2_magnitude_spectrum, cmap = 'gray')
plt.title('after cv2.dft()'), plt.xticks([]), plt.yticks([])
plt.show()
