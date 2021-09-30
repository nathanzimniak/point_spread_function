#!/usr/bin/env python3
# coding: utf-8

'''
Programme pour calculer l'amplitude du champ électrique et la point spread function dans le plan image en fonction de la pupille utilisée
'''

__author__ = 'Nathan Zimniak'


import numpy as np
import matplotlib.pyplot as plt


#CAS 1D

#Initialisation des constantes
aperture_size = 56
nx = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
E1=1
W = 1.0 * (np.abs(x) < aperture_size/2)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.plot(W, color = 'gold')
plt.title("Pupille 1D")
ax2=fig.add_subplot(232)
ax2.plot(np.abs(np.fft.fftshift(E2)), color = 'teal', linewidth=1)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-50,nx/2+50)
ax3=fig.add_subplot(233)
ax3.plot(np.log10(np.abs(np.fft.fftshift(E2))), color = 'teal', linewidth=1)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-50,nx/2+50)
ax4=fig.add_subplot(235)
ax4.plot(np.fft.fftshift(PSF), color = 'crimson', linewidth=1)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-50,nx/2+50)
ax5=fig.add_subplot(236)
ax5.plot(np.log10(np.fft.fftshift(PSF)), color = 'crimson', linewidth=1)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-50,nx/2+50)

plt.tight_layout()
plt.show()





#CAS 2D

#Initialisation des constantes
aperture_size = 56
nx = 513
ny = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
y = np.arange(-ny/2, ny/2, 1, dtype = int)
x2,y2 = np.meshgrid(x,y)
r = np.sqrt(x2**2 + y2**2)
E1=1
W = 1.0 * (r < aperture_size/2.)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft2(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.imshow(W, cmap=plt.cm.cividis)
plt.title("Pupille 2D")
ax2=fig.add_subplot(232)
ax2.imshow(np.abs(np.fft.fftshift(E2)), cmap=plt.cm.viridis)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-150,nx/2+150)
ax2.set_ylim(nx/2-150,nx/2+150)
ax3=fig.add_subplot(233)
ax3.imshow(np.log10(np.abs(np.fft.fftshift(E2))), cmap=plt.cm.viridis)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-150,nx/2+150)
ax3.set_ylim(nx/2-150,nx/2+150)
ax4=fig.add_subplot(235)
ax4.imshow(np.fft.fftshift(PSF), cmap=plt.cm.inferno)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-150,nx/2+150)
ax4.set_ylim(nx/2-150,nx/2+150)
ax5=fig.add_subplot(236)
ax5.imshow(np.log10(np.fft.fftshift(PSF)), cmap=plt.cm.inferno)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-150,nx/2+150)
ax5.set_ylim(nx/2-150,nx/2+150)

plt.tight_layout()
plt.show()





#CAS 2D (spiders croix)

#Initialisation des constantes
aperture_size = 56
nx = 513
ny = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
y = np.arange(-ny/2, ny/2, 1, dtype = int)
x2,y2 = np.meshgrid(x,y)
r = np.sqrt(x2**2 + y2**2)
E1=1
W = 1.0 * (r < aperture_size/2.) * (np.abs(y2) > 1) * (np.abs(x2) > 1)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft2(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.imshow(W, cmap=plt.cm.cividis)
plt.title("Pupille 2D")
ax2=fig.add_subplot(232)
ax2.imshow(np.abs(np.fft.fftshift(E2)), cmap=plt.cm.viridis)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-150,nx/2+150)
ax2.set_ylim(nx/2-150,nx/2+150)
ax3=fig.add_subplot(233)
ax3.imshow(np.log10(np.abs(np.fft.fftshift(E2))), cmap=plt.cm.viridis)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-150,nx/2+150)
ax3.set_ylim(nx/2-150,nx/2+150)
ax4=fig.add_subplot(235)
ax4.imshow(np.fft.fftshift(PSF), cmap=plt.cm.inferno)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-150,nx/2+150)
ax4.set_ylim(nx/2-150,nx/2+150)
ax5=fig.add_subplot(236)
ax5.imshow(np.log10(np.fft.fftshift(PSF)), cmap=plt.cm.inferno)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-150,nx/2+150)
ax5.set_ylim(nx/2-150,nx/2+150)

plt.tight_layout()
plt.show()





#CAS 2D (coronographe)

#Initialisation des constantes
aperture_size = 56
nx = 513
ny = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
y = np.arange(-ny/2, ny/2, 1, dtype = int)
x2,y2 = np.meshgrid(x,y)
r = np.sqrt(x2**2 + y2**2)
E1=1
W = 1.0 * (r < aperture_size/2.) * (r > aperture_size/4)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft2(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.imshow(W, cmap=plt.cm.cividis)
plt.title("Pupille 2D")
ax2=fig.add_subplot(232)
ax2.imshow(np.abs(np.fft.fftshift(E2)), cmap=plt.cm.viridis)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-150,nx/2+150)
ax2.set_ylim(nx/2-150,nx/2+150)
ax3=fig.add_subplot(233)
ax3.imshow(np.log10(np.abs(np.fft.fftshift(E2))), cmap=plt.cm.viridis)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-150,nx/2+150)
ax3.set_ylim(nx/2-150,nx/2+150)
ax4=fig.add_subplot(235)
ax4.imshow(np.fft.fftshift(PSF), cmap=plt.cm.inferno)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-150,nx/2+150)
ax4.set_ylim(nx/2-150,nx/2+150)
ax5=fig.add_subplot(236)
ax5.imshow(np.log10(np.fft.fftshift(PSF)), cmap=plt.cm.inferno)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-150,nx/2+150)
ax5.set_ylim(nx/2-150,nx/2+150)

plt.tight_layout()
plt.show()





#CAS 2D (2 pupilles)

#Initialisation des constantes
aperture_size = 56
nx = 513
ny = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
y = np.arange(-ny/2, ny/2, 1, dtype = int)
x2,y2 = np.meshgrid(x,y)
r1 = np.sqrt((x2-aperture_size)**2 + y2**2)
r2 = np.sqrt((x2+aperture_size)**2 + y2**2)
E1=1
W = 1.0 * (r1 < aperture_size/2.) + 1.0 * (r2 < aperture_size/2.)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft2(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.imshow(W, cmap=plt.cm.cividis)
plt.title("Pupille 2D")
ax2=fig.add_subplot(232)
ax2.imshow(np.abs(np.fft.fftshift(E2)), cmap=plt.cm.viridis)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-150,nx/2+150)
ax2.set_ylim(nx/2-150,nx/2+150)
ax3=fig.add_subplot(233)
ax3.imshow(np.log10(np.abs(np.fft.fftshift(E2))), cmap=plt.cm.viridis)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-150,nx/2+150)
ax3.set_ylim(nx/2-150,nx/2+150)
ax4=fig.add_subplot(235)
ax4.imshow(np.fft.fftshift(PSF), cmap=plt.cm.inferno)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-150,nx/2+150)
ax4.set_ylim(nx/2-150,nx/2+150)
ax5=fig.add_subplot(236)
ax5.imshow(np.log10(np.fft.fftshift(PSF)), cmap=plt.cm.inferno)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-150,nx/2+150)
ax5.set_ylim(nx/2-150,nx/2+150)
plt.tight_layout()
plt.show()





#CAS 2D (3 pupilles)

#Initialisation des constantes
aperture_size = 56
nx = 513
ny = 513
x = np.arange(-nx/2, nx/2, 1, dtype = int)
y = np.arange(-ny/2, ny/2, 1, dtype = int)
x2,y2 = np.meshgrid(x,y)
r1 = np.sqrt((x2)**2 + y2**2)
r2 = np.sqrt((x2-1*aperture_size)**2 + y2**2)
r3 = np.sqrt((x2+1*aperture_size)**2 + y2**2)
E1=1
W = 1.0 * (r1 < aperture_size/2.) + 1.0 * (r2 < aperture_size/2.) + 1.0 * (r3 < aperture_size/2.)

#Calcul du champ électrique et de la PSF
E2 = np.fft.fft2(W)*E1
PSF = np.abs(E2)**2

#Affiche le résultat
plt.style.use('dark_background')
fig=plt.figure()

ax1=fig.add_subplot(131)
ax1.imshow(W, cmap=plt.cm.cividis)
plt.title("Pupille 2D")

ax2=fig.add_subplot(232)
ax2.imshow(np.abs(np.fft.fftshift(E2)), cmap=plt.cm.viridis)
plt.title("Amplitude du champ électrique \n dans le plan image", fontsize=6)
ax2.set_xlim(nx/2-150,nx/2+150)
ax2.set_ylim(nx/2-150,nx/2+150)
ax3=fig.add_subplot(233)
ax3.imshow(np.log10(np.abs(np.fft.fftshift(E2))), cmap=plt.cm.viridis)
plt.title("Logarithme de l'amplitude du champ \n électrique dans le plan image", fontsize=6)
ax3.set_xlim(nx/2-150,nx/2+150)
ax3.set_ylim(nx/2-150,nx/2+150)
ax4=fig.add_subplot(235)
ax4.imshow(np.fft.fftshift(PSF), cmap=plt.cm.inferno)
plt.title("PSF dans le plan image", fontsize=6)
ax4.set_xlim(nx/2-150,nx/2+150)
ax4.set_ylim(nx/2-150,nx/2+150)
ax5=fig.add_subplot(236)
ax5.imshow(np.log10(np.fft.fftshift(PSF)), cmap=plt.cm.inferno)
plt.title("Logarithme de la PSF \n dans le plan image", fontsize=6)
ax5.set_xlim(nx/2-150,nx/2+150)
ax5.set_ylim(nx/2-150,nx/2+150)

plt.tight_layout()
plt.show()

