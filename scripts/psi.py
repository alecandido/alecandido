"""Generate the animated wavepacket banner, assets/psi.svg.

A superposition of the lowest harmonic-oscillator eigenstates evolves in time;
the filled curve is |psi|^2, the dashed ones are its real and imaginary parts.
The evolution is exactly periodic, so the loop is seamless. Pure stdlib, run it
again after tweaking the constants below:

    python3 scripts/psi.py > assets/psi.svg
"""

import math

# --- knobs ---------------------------------------------------------------
COEFFS = [0.50, 0.58, 0.50, 0.36, 0.26, 0.14]  # weights of n = 0, 1, 2, ...
WIDTH, HEIGHT = 1200, 200  # viewBox
X_RANGE = 5.2  # plot x in [-X_RANGE, X_RANGE]
POINTS = 60  # samples per curve
FRAMES = 32  # keyframes per period
PERIOD = "14s"  # loop duration
STROKE = "#3b82f6"  # |psi|^2
RE, IM = "#ec4899", "#8b5cf6"  # components
# -------------------------------------------------------------------------

norm = math.sqrt(sum(c * c for c in COEFFS))
COEFFS = [c / norm for c in COEFFS]


def hermite(n: int, x: float) -> float:
    h0, h1 = 1.0, 2.0 * x
    if n == 0:
        return h0
    for k in range(1, n):
        h0, h1 = h1, 2.0 * x * h1 - 2.0 * k * h0
    return h1


def phi(n: int, x: float) -> float:
    pref = 1.0 / math.sqrt(2.0**n * math.factorial(n) * math.sqrt(math.pi))
    return pref * hermite(n, x) * math.exp(-x * x / 2.0)


XS = [-X_RANGE + 2 * X_RANGE * i / (POINTS - 1) for i in range(POINTS)]
BASIS = [[phi(n, x) for x in XS] for n in range(len(COEFFS))]


def psi(t: float) -> tuple[list[float], list[float], list[float]]:
    re, im, dens = [], [], []
    for i in range(POINTS):
        a = b = 0.0
        for n, c in enumerate(COEFFS):
            a += c * BASIS[n][i] * math.cos(n * t)
            b -= c * BASIS[n][i] * math.sin(n * t)
        re.append(a)
        im.append(b)
        dens.append(a * a + b * b)
    return re, im, dens


frames = [psi(2 * math.pi * k / FRAMES) for k in range(FRAMES)]
frames.append(frames[0])  # close the loop

peak = max(max(d) for _, _, d in frames)
amp = max(max(abs(v) for v in re + im) for re, im, _ in frames)
base = round(HEIGHT * 0.66)  # baseline, leaving room for negative components
scale_d = 0.92 * (base - 6) / peak
scale_c = 0.96 * (HEIGHT - base) / amp


def to_px(x_index: int, value: float, scale: float) -> str:
    x = WIDTH * x_index / (POINTS - 1)
    y = base - value * scale
    return f"{x:.0f},{y:.0f}"


def path(values: list[float], scale: float, close: bool) -> str:
    pts = " ".join(to_px(i, v, scale) for i, v in enumerate(values))
    d = f"M{pts}"
    if close:
        d += f" L{WIDTH},{base} L0,{base} Z"
    return d


def animate(key: int, scale: float, close: bool) -> str:
    values = ";".join(path(f[key], scale, close) for f in frames)
    return (
        f'<animate attributeName="d" dur="{PERIOD}" repeatCount="indefinite" '
        f'calcMode="linear" values="{values}"/>'
    )


svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}" role="img" aria-label="A quantum wavepacket oscillating">
<line x1="0" y1="{base}" x2="{WIDTH}" y2="{base}" stroke="#9ca3af" stroke-opacity="0.5" stroke-width="1"/>
<path fill="none" stroke="{RE}" stroke-width="2.2" stroke-dasharray="7 7" stroke-opacity="0.8" d="{path(frames[0][0], scale_c, False)}">{animate(0, scale_c, False)}</path>
<path fill="none" stroke="{IM}" stroke-width="2.2" stroke-dasharray="7 7" stroke-opacity="0.8" d="{path(frames[0][1], scale_c, False)}">{animate(1, scale_c, False)}</path>
<path fill="{STROKE}" fill-opacity="0.16" stroke="none" d="{path(frames[0][2], scale_d, True)}">{animate(2, scale_d, True)}</path>
<path fill="none" stroke="{STROKE}" stroke-width="3" stroke-linejoin="round" d="{path(frames[0][2], scale_d, False)}">{animate(2, scale_d, False)}</path>
</svg>
"""

print(svg, end="")
