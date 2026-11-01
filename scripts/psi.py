"""Generate the animated wavepacket banners in assets/.

A superposition of the lowest bound states of a quantum system evolves in
time: the filled curve is |psi|^2, the dashed ones are the real and imaginary
parts of the components. Energies are integer multiples of a base frequency,
so the evolution is exactly periodic and the loop is seamless. Pure stdlib:

    python3 scripts/psi.py well > assets/psi-well.svg
    python3 scripts/psi.py oscillator > assets/psi-oscillator.svg

`well` is a particle in an infinite square well, `oscillator` a harmonic
oscillator; tweak the knobs below and run again.
"""

import math
import sys

# --- knobs ---------------------------------------------------------------
SYSTEMS = {
    # weights of the states n = 1, 2, 3, ... (well) or n = 0, 1, 2, ... (oscillator),
    # and whether to dash every component or only the total psi
    "well": {"weights": [0.55, 0.62, 0.42, 0.30], "components": True},
    "oscillator": {"weights": [0.50, 0.58, 0.50, 0.36, 0.26, 0.14], "components": False},
}
WIDTH, HEIGHT = 1200, 200  # viewBox
POINTS = 48  # samples per curve
FRAMES = 24  # keyframes per period
PERIOD = "14s"  # loop duration
STROKE = "#3b82f6"  # |psi|^2
RE, IM = "#ec4899", "#8b5cf6"  # components
# -------------------------------------------------------------------------


def hermite(n: int, x: float) -> float:
    h0, h1 = 1.0, 2.0 * x
    if n == 0:
        return h0
    for k in range(1, n):
        h0, h1 = h1, 2.0 * x * h1 - 2.0 * k * h0
    return h1


def oscillator(n: int, x: float) -> float:
    pref = 1.0 / math.sqrt(2.0**n * math.factorial(n) * math.sqrt(math.pi))
    return pref * hermite(n, x) * math.exp(-x * x / 2.0)


def well(n: int, x: float) -> float:
    """Infinite square well on [0, 1], levels n = 1, 2, ... with E_n = n^2."""
    return math.sqrt(2.0) * math.sin((n + 1) * math.pi * x)


def system(name: str):
    coeffs = SYSTEMS[name]["weights"]
    norm = math.sqrt(sum(c * c for c in coeffs))
    coeffs = [c / norm for c in coeffs]
    if name == "well":
        xs = [i / (POINTS - 1) for i in range(POINTS)]
        energy = [(n + 1) ** 2 for n in range(len(coeffs))]
        basis = [[well(n, x) for x in xs] for n in range(len(coeffs))]
    else:
        xs = [-5.2 + 10.4 * i / (POINTS - 1) for i in range(POINTS)]
        energy = list(range(len(coeffs)))
        basis = [[oscillator(n, x) for x in xs] for n in range(len(coeffs))]
    return coeffs, energy, basis


def main(name: str) -> str:
    coeffs, energy, basis = system(name)
    components = SYSTEMS[name]["components"]

    def at(t: float):
        """Per component (re, im) and total density, sampled on the grid."""
        comps = []
        for n, c in enumerate(coeffs):
            ph = energy[n] * t
            comps.append(
                (
                    [c * b * math.cos(ph) for b in basis[n]],
                    [-c * b * math.sin(ph) for b in basis[n]],
                )
            )
        dens = [
            sum(re[i] for re, _ in comps) ** 2 + sum(im[i] for _, im in comps) ** 2
            for i in range(POINTS)
        ]
        if not components:
            comps = [
                (
                    [sum(re[i] for re, _ in comps) for i in range(POINTS)],
                    [sum(im[i] for _, im in comps) for i in range(POINTS)],
                )
            ]
        return comps, dens

    frames = [at(2 * math.pi * k / FRAMES) for k in range(FRAMES)]
    frames.append(frames[0])  # close the loop

    peak = max(max(d) for _, d in frames)
    amp = max(abs(v) for comps, _ in frames for re, im in comps for v in re + im)
    base = round(HEIGHT * 0.66)  # baseline, leaving room for negative components
    scale_d = 0.92 * (base - 6) / peak
    scale_c = 0.96 * (HEIGHT - base) / amp

    def path(values, scale, close):
        pts = " ".join(
            f"{WIDTH * i / (POINTS - 1):.0f},{base - v * scale:.0f}" for i, v in enumerate(values)
        )
        return f"M{pts}" + (f" L{WIDTH},{base} L0,{base} Z" if close else "")

    def animated(select, scale, close, attrs):
        values = ";".join(path(select(f), scale, close) for f in frames)
        return (
            f'<path {attrs} d="{path(select(frames[0]), scale, close)}">'
            f'<animate attributeName="d" dur="{PERIOD}" repeatCount="indefinite" '
            f'calcMode="linear" values="{values}"/></path>'
        )

    dashed = 'fill="none" stroke-width="2" stroke-dasharray="7 7" stroke-opacity="0.75"'
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" '
        f'width="{WIDTH}" height="{HEIGHT}" role="img" aria-label="A quantum wavepacket oscillating">',
        f'<line x1="0" y1="{base}" x2="{WIDTH}" y2="{base}" stroke="#9ca3af" stroke-opacity="0.5"/>',
    ]
    for n in range(len(frames[0][0])):
        parts.append(animated(lambda f, n=n: f[0][n][0], scale_c, False, f'stroke="{RE}" {dashed}'))
        parts.append(animated(lambda f, n=n: f[0][n][1], scale_c, False, f'stroke="{IM}" {dashed}'))
    parts.append(
        animated(lambda f: f[1], scale_d, True, f'fill="{STROKE}" fill-opacity="0.16" stroke="none"')
    )
    parts.append(
        animated(
            lambda f: f[1],
            scale_d,
            False,
            f'fill="none" stroke="{STROKE}" stroke-width="3" stroke-linejoin="round"',
        )
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "well"
    if name not in SYSTEMS:
        raise SystemExit(f"unknown system {name!r}, choose from {', '.join(SYSTEMS)}")
    print(main(name), end="")
