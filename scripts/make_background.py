"""Render the website background: a periodic 2D Zel'dovich-approximation cosmic web."""
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter

NX, NY, OVER, LX, AMP, R, SEED = 3000, 2000, 2, 360.0, 2.0, 0.55, 11
nx, ny = NX*OVER, NY*OVER; LY = LX*ny/nx
rng = np.random.default_rng(SEED)
kx = 2*np.pi*np.fft.rfftfreq(nx, d=LX/nx)[None, :]; ky = 2*np.pi*np.fft.fftfreq(ny, d=LY/ny)[:, None]
k2 = kx**2+ky**2; k2[0, 0] = 1.0; k = np.sqrt(k2); q = k/0.2
T = np.log(1+2.34*q)/(2.34*q)*(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**-0.25
P = k**0.96*T**2*k*np.exp(-k2*R**2); P[0, 0] = 0
dk = np.fft.rfft2(rng.standard_normal((ny, nx)).astype(np.float32))*np.sqrt(P)
d = np.fft.irfft2(dk, s=(ny, nx)); dk *= AMP/d.std(); del d
psix = (np.fft.irfft2(1j*kx/k2*dk, s=(ny, nx))*(NX/LX)).astype(np.float32)
psiy = (np.fft.irfft2(1j*ky/k2*dk, s=(ny, nx))*(NY/LY)).astype(np.float32)
del dk, k2, k, q, T, P
rho = np.zeros(NX*NY)
qx = np.arange(nx, dtype=np.float32)[None, :]/OVER; qy = np.arange(ny, dtype=np.float32)[:, None]/OVER
# four interleaved sub-lattices (displacements interpolated between lattice points) to avoid grid patterns
for sy, sx in ((0, 0), (0, 1), (1, 0), (1, 1)):
    px = psix if sx == 0 else 0.5*(psix+np.roll(psix, -1, 1)); py = psiy if sx == 0 else 0.5*(psiy+np.roll(psiy, -1, 1))
    if sy: px = 0.5*(px+np.roll(px, -1, 0)); py = 0.5*(py+np.roll(py, -1, 0))
    X = ((qx+sx*0.5/OVER+px) % NX).ravel(); Y = ((qy+sy*0.5/OVER+py) % NY).ravel(); del px, py
    i0 = np.floor(X).astype(np.int64); j0 = np.floor(Y).astype(np.int64); fx = X-i0; fy = Y-j0; del X, Y
    i0 %= NX; j0 %= NY; i1 = (i0+1) % NX; j1 = (j0+1) % NY
    for jj, ii, w in ((j0, i0, (1-fx)*(1-fy)), (j0, i1, fx*(1-fy)), (j1, i0, (1-fx)*fy), (j1, i1, fx*fy)):
        rho += np.bincount(jj*NX+ii, weights=w, minlength=NX*NY)
    del i0, j0, i1, j1, fx, fy
rho = (rho.reshape(NY, NX)/(4*OVER**2)).astype(np.float32)
rho = gaussian_filter(rho, 0.6, mode="wrap")
np.save("web_rho.npy", rho)
v = np.log10(rho+0.08); lo, hi = np.percentile(v, [0.5, 99.95]); v = np.clip((v-lo)/(hi-lo), 0, 1)
print("mean", rho.mean(), "max", rho.max(), "v median", np.median(v))

def ramp(v, stops):
    xs = [s[0] for s in stops]; out = np.empty(v.shape+(3,), np.float32)
    for c in range(3): out[..., c] = np.interp(v, xs, [s[1][c] for s in stops])
    return (out+0.5).astype(np.uint8)

dark = ramp(v**1.15, [(0, (7, 10, 20)), (0.35, (20, 34, 66)), (0.6, (52, 92, 150)), (0.82, (150, 190, 228)), (1, (245, 250, 255))])
light = ramp(v**1.15, [(0, (255, 255, 255)), (0.35, (226, 233, 242)), (0.6, (172, 190, 214)), (0.82, (96, 122, 160)), (1, (40, 58, 92))])
for name, arr in (("dark", dark), ("light", light)):
    im = Image.fromarray(arr); im.save(f"web_{name}.png")
    im.save(f"web_{name}.webp", "WEBP", quality=86, method=6)
    im.resize((1500, 1000), Image.LANCZOS).save(f"web_{name}_prev.jpg", quality=88)
    im.crop((1000, 600, 1900, 1200)).save(f"web_{name}_crop.png")
import os
for f in sorted(os.listdir(".")):
    if f.startswith("web_") and f.endswith(".webp"): print(f, os.path.getsize(f)//1024, "KB")
