import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch
import numpy as np

# -----------------------------
# Figure setup
# -----------------------------
fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(-1.85, 3.55)   # widened to create empty space on the right
ax.set_ylim(-1.7, 1.65)
ax.set_aspect("equal")
ax.axis("off")

# -----------------------------
# Main cross-section geometry
# -----------------------------
center = (0, 0)

# Dialysate side / shell
dialysate = Circle(center, 1.22, facecolor="#d8ecfb", edgecolor="black", linewidth=1.1, zorder=1)
ax.add_patch(dialysate)

# Membrane wall
membrane = Circle(center, 0.88, facecolor="#cfcfcf", edgecolor="#777777", linewidth=1.0, zorder=2)
ax.add_patch(membrane)

# Blood lumen
lumen = Circle(center, 0.72, facecolor="#ffd6d6", edgecolor="#9b5a5a", linewidth=1.4, zorder=4)
ax.add_patch(lumen)

# Inner membrane outline
inner_ring = Circle(center, 0.75, fill=False, edgecolor="#cc7777", linewidth=1.2, zorder=5)
ax.add_patch(inner_ring)

# -----------------------------
# Membrane pores
# -----------------------------
np.random.seed(42)
for _ in range(115):
    angle = np.random.uniform(0, 2 * np.pi)
    r = np.random.uniform(0.78, 0.86)
    x, y = r * np.cos(angle), r * np.sin(angle)
    pore = Circle((x, y), 0.011, facecolor="#8f8f8f", edgecolor="none", zorder=3)
    ax.add_patch(pore)

# -----------------------------
# Drawing functions
# -----------------------------
def draw_rbc(ax, x, y, angle=0, scale=1.0, z=8):
    outer = Ellipse(
        (x, y), 0.22 * scale, 0.13 * scale, angle=angle,
        facecolor="#cf2027", edgecolor="#a01418", linewidth=1.0, zorder=z
    )
    inner = Ellipse(
        (x, y), 0.105 * scale, 0.055 * scale, angle=angle,
        facecolor="#f07272", edgecolor="none", alpha=0.9, zorder=z + 1
    )
    ax.add_patch(outer)
    ax.add_patch(inner)

def draw_urea(ax, x, y, radius=0.018, z=10):
    outer = Circle((x, y), radius, facecolor="#1269c7", edgecolor="#004ba0", linewidth=0.35, zorder=z)
    inner = Circle((x - radius * 0.25, y + radius * 0.25), radius * 0.42, facecolor="#61b7ff", edgecolor="none", zorder=z + 1)
    ax.add_patch(outer)
    ax.add_patch(inner)

def draw_protein(ax, cx, cy, scale=1.0, z=9):
    offsets = [
        (0, 0), (0.035, 0.025), (-0.035, 0.025), (0.035, -0.025),
        (-0.035, -0.025), (0, 0.05), (0, -0.05),
        (0.055, 0.0), (-0.055, 0.0), (0.02, 0.07), (-0.02, -0.07)
    ]
    for dx, dy in offsets:
        c = Circle(
            (cx + dx * scale, cy + dy * scale),
            0.028 * scale,
            facecolor="#8d5bc1",
            edgecolor="#7041a5",
            linewidth=0.5,
            zorder=z
        )
        ax.add_patch(c)

# -----------------------------
# Red blood cells
# -----------------------------
rbc_positions = [
    (-0.43, 0.45, -20, 1.05),
    (0.25, 0.34, 15, 1.05),
    (-0.56, -0.08, 15, 1.0),
    (-0.13, -0.02, -15, 1.0),
    (0.35, -0.48, 20, 1.0),
    (-0.33, -0.61, 20, 1.0),
]
for x, y, ang, s in rbc_positions:
    draw_rbc(ax, x, y, ang, s)

# -----------------------------
# Proteins
# -----------------------------
draw_protein(ax, -0.33, -0.38, 1.1)
draw_protein(ax, 0.08, 0.48, 0.9)
draw_protein(ax, 0.50, -0.20, 1.15)

# -----------------------------
# Urea molecules
# -----------------------------
np.random.seed(7)

# More urea in blood side
for _ in range(42):
    angle = np.random.uniform(0, 2 * np.pi)
    r = np.sqrt(np.random.uniform(0.02, 0.68**2))
    x, y = r * np.cos(angle), r * np.sin(angle)
    draw_urea(ax, x, y, radius=0.017)

# Fewer urea in dialysate side
for _ in range(19):
    angle = np.random.uniform(0, 2 * np.pi)
    r = np.random.uniform(0.94, 1.15)
    x, y = r * np.cos(angle), r * np.sin(angle)
    draw_urea(ax, x, y, radius=0.017)

# -----------------------------
# Diffusion arrows
# -----------------------------
arrow_y_values = [0.44, 0.25, 0.08, -0.10, -0.30, -0.52]
for y in arrow_y_values:
    ax.annotate(
        "",
        xy=(1.08, y),
        xytext=(0.44, y),
        arrowprops=dict(
            arrowstyle="-|>",
            color="#1e5bb8",
            lw=2.0,
            mutation_scale=15
        ),
        zorder=12
    )

# -----------------------------
# Labels and callouts
# -----------------------------
ax.annotate(
    "Blood side\n(lumen)",
    xy=(-0.35, 0.55),
    xytext=(-0.85, 1.38),
    fontsize=13,
    fontweight="bold",
    color="#c62020",
    ha="center",
    va="center",
    arrowprops=dict(arrowstyle="-", color="black", lw=1.2),
    zorder=20
)

ax.annotate(
    "Membrane wall",
    xy=(0.16, 0.84),
    xytext=(0.38, 1.43),
    fontsize=13,
    fontweight="bold",
    color="#222222",
    ha="center",
    va="center",
    arrowprops=dict(arrowstyle="-", color="black", lw=1.2),
    zorder=20
)

ax.annotate(
    "Dialysate side\n(shell)",
    xy=(1.03, 0.62),
    xytext=(1.62, 1.35),
    fontsize=13,
    fontweight="bold",
    color="#1956bf",
    ha="center",
    va="center",
    arrowprops=dict(arrowstyle="-", color="black", lw=1.2),
    zorder=20
)

# -----------------------------
# Concentration boxes
# -----------------------------
high_box = FancyBboxPatch(
    (-1.72, -0.05), 0.55, 0.30,
    boxstyle="round,pad=0.035",
    facecolor="white",
    edgecolor="#c62020",
    linewidth=1.4,
    zorder=15
)
ax.add_patch(high_box)
ax.text(
    -1.445, 0.10,
    "Higher urea\nconcentration",
    ha="center",
    va="center",
    fontsize=10.5,
    color="#c62020",
    fontweight="bold",
    zorder=16
)

low_box = FancyBboxPatch(
    (1.42, -0.05), 0.62, 0.30,
    boxstyle="round,pad=0.035",
    facecolor="white",
    edgecolor="#1956bf",
    linewidth=1.4,
    zorder=15
)
ax.add_patch(low_box)
ax.text(
    1.73, 0.10,
    "Lower urea\nconcentration",
    ha="center",
    va="center",
    fontsize=10.5,
    color="#1956bf",
    fontweight="bold",
    zorder=16
)

# -----------------------------
# Bottom brackets
# -----------------------------
bracket_y = -1.32

sections = [
    (-1.05, -0.25, "Blood side\n(lumen)"),
    (-0.25, 0.25, "Membrane\nwall"),
    (0.25, 1.25, "Dialysate side\n(shell)")
]

for x1, x2, label in sections:
    ax.plot([x1, x2], [bracket_y, bracket_y], color="black", lw=1.2, zorder=20)
    ax.plot([x1, x1], [bracket_y, bracket_y + 0.07], color="black", lw=1.2, zorder=20)
    ax.plot([x2, x2], [bracket_y, bracket_y + 0.07], color="black", lw=1.2, zorder=20)
    ax.text(
        (x1 + x2) / 2,
        bracket_y - 0.10,
        label,
        ha="center",
        va="top",
        fontsize=10.5,
        color="black"
    )

# -----------------------------
# Legend (moved farther right)
# -----------------------------
legend_x, legend_y = 2.35, 0.42

legend_bg = FancyBboxPatch(
    (legend_x - 0.18, legend_y - 0.72),
    1.18,
    1.22,
    boxstyle="round,pad=0.04",
    linewidth=1.2,
    edgecolor="#333333",
    facecolor="white",
    zorder=30
)
ax.add_patch(legend_bg)

ax.text(
    legend_x + 0.41,
    legend_y + 0.38,
    "Legend",
    ha="center",
    va="center",
    fontsize=11,
    fontweight="bold",
    zorder=31
)

# Legend RBC
draw_rbc(ax, legend_x + 0.08, legend_y + 0.20, angle=0, scale=0.72, z=31)
ax.text(
    legend_x + 0.28,
    legend_y + 0.20,
    "Red blood cell",
    va="center",
    fontsize=9.2,
    zorder=31
)

# Legend protein
draw_protein(ax, legend_x + 0.08, legend_y - 0.03, scale=0.70, z=31)
ax.text(
    legend_x + 0.28,
    legend_y - 0.03,
    "Protein\n(remains in blood)",
    va="center",
    fontsize=9.2,
    zorder=31
)

# Legend urea
draw_urea(ax, legend_x + 0.08, legend_y - 0.30, radius=0.020, z=31)
ax.text(
    legend_x + 0.28,
    legend_y - 0.30,
    "Urea molecule\n(diffuses)",
    va="center",
    fontsize=9.2,
    zorder=31
)

# Legend arrow
ax.annotate(
    "",
    xy=(legend_x + 0.22, legend_y - 0.55),
    xytext=(legend_x - 0.06, legend_y - 0.55),
    arrowprops=dict(
        arrowstyle="-|>",
        color="#1e5bb8",
        lw=1.8,
        mutation_scale=13
    ),
    zorder=31
)
ax.text(
    legend_x + 0.28,
    legend_y - 0.55,
    "Urea diffusion\n(high → low concentration)",
    va="center",
    fontsize=9.2,
    zorder=31
)



plt.tight_layout()
plt.show()