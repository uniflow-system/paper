"""Generate Figure 1: Hexagonal Architecture Diagram with 12 adapters."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import RegularPolygon, FancyBboxPatch
import matplotlib

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.size"] = 9

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(-6, 6)
ax.set_ylim(-5.5, 5.5)
ax.set_aspect("equal")
ax.axis("off")

# Colors
C_CORE = "#3b82f6"  # blue
C_PORT = "#f59e0b"  # amber/yellow
C_INPUT = "#06b6d4"  # cyan/teal
C_PROC = "#8b5cf6"  # purple
C_INFRA = "#10b981"  # emerald
C_BG = "#f8fafc"  # near-white
C_TEXT = "#1e293b"  # dark

# Central hexagon
hex_core = RegularPolygon(
    (0, 0),
    numVertices=6,
    radius=2.0,
    orientation=0,
    facecolor=C_CORE,
    edgecolor="white",
    linewidth=2,
    alpha=0.9,
)
ax.add_patch(hex_core)
ax.text(
    0,
    0.3,
    "Domain Core",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
    color="white",
)
ax.text(
    0,
    -0.3,
    "RAG Orchestration",
    ha="center",
    va="center",
    fontsize=10,
    color="white",
    alpha=0.9,
)


# Port ring labels
def draw_port_label(ax, x, y, text, color):
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=11,
        fontweight="bold",
        color=color,
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor="white",
            edgecolor=color,
            linewidth=1.5,
            alpha=0.95,
        ),
    )


# Adapter boxes
def draw_adapter(ax, x, y, text, color, w=2.0, h=0.65):
    box = FancyBboxPatch(
        (x - w / 2, y - h / 2),
        w,
        h,
        boxstyle="round,pad=0.1",
        facecolor=color,
        edgecolor="white",
        linewidth=1,
        alpha=0.85,
    )
    ax.add_patch(box)
    ax.text(
        x,
        y,
        text,
        ha="center",
        va="center",
        fontsize=8,
        fontweight="bold",
        color="white",
    )


def draw_connection(ax, x1, y1, x2, y2, color):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color=color, lw=1.5, alpha=0.6),
    )


# === INPUT PORT (Left side, 4 adapters) ===
draw_port_label(ax, -4.2, 3.8, "IInputAdapter", C_INPUT)

input_adapters = [
    (-4.2, 2.8, "YouTube Adapter"),
    (-4.2, 1.8, "Web Scraper Adapter"),
    (-4.2, 0.8, "Audio Adapter\n(WhisperX)"),
    (-4.2, -0.3, "Document Adapter"),
]
for x, y, label in input_adapters:
    draw_adapter(ax, x, y, label, C_INPUT)
    draw_connection(ax, x + 1.0, y, -1.7, y * 0.3, C_INPUT)

# === PROCESSING PORT (Top/Bottom, 5 adapters) ===
draw_port_label(ax, 0, 4.8, "IProcessingAdapter", C_PROC)

proc_adapters_top = [
    (-2.2, 3.8, "Chunking"),
    (0, 3.8, "Embedding"),
    (2.2, 3.8, "Metadata"),
]
proc_adapters_bot = [
    (-1.1, -3.8, "Summarization"),
    (1.1, -3.8, "Indexing"),
]
for x, y, label in proc_adapters_top:
    draw_adapter(ax, x, y, label, C_PROC, w=1.8)
    draw_connection(ax, x, y - 0.35, x * 0.3, 1.7, C_PROC)

draw_port_label(ax, 0, -4.8, "IProcessingAdapter", C_PROC)
for x, y, label in proc_adapters_bot:
    draw_adapter(ax, x, y, label, C_PROC, w=1.8)
    draw_connection(ax, x, y + 0.35, x * 0.3, -1.7, C_PROC)

# === INFRASTRUCTURE PORT (Right side, 3 adapters) ===
draw_port_label(ax, 4.2, 3.8, "IInfrastructureAdapter", C_INFRA)

infra_adapters = [
    (4.2, 2.5, "Vector Store\n(Qdrant)"),
    (4.2, 1.3, "LLM Inference\n(Qwen2.5-3B)"),
    (4.2, 0.1, "Prompt\nTemplates"),
]
for x, y, label in infra_adapters:
    draw_adapter(ax, x, y, label, C_INFRA)
    draw_connection(ax, x - 1.0, y, 1.7, y * 0.3, C_INFRA)

# DAG orchestration arrow at bottom
ax.annotate(
    "",
    xy=(2.5, -2.5),
    xytext=(-2.5, -2.5),
    arrowprops=dict(
        arrowstyle="->", color=C_PORT, lw=2.5, alpha=0.7, connectionstyle="arc3,rad=0.3"
    ),
)
ax.text(
    0,
    -2.9,
    "DAG Orchestration (LangGraph)",
    ha="center",
    va="center",
    fontsize=9,
    fontweight="bold",
    color=C_PORT,
    bbox=dict(
        boxstyle="round,pad=0.3", facecolor="white", edgecolor=C_PORT, linewidth=1.5
    ),
)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=C_CORE, label="Domain Core"),
    mpatches.Patch(facecolor=C_INPUT, label="Input Adapters (4)"),
    mpatches.Patch(facecolor=C_PROC, label="Processing Adapters (5)"),
    mpatches.Patch(facecolor=C_INFRA, label="Infrastructure Adapters (3)"),
]
ax.legend(
    handles=legend_elements,
    loc="lower left",
    fontsize=9,
    framealpha=0.95,
    edgecolor="#d1d5db",
)

# Adapter count annotation
ax.text(
    4.2,
    -4.8,
    "12 Adapters Total\n4 Input + 5 Processing + 3 Infrastructure",
    ha="center",
    va="center",
    fontsize=8,
    color="#6b7280",
    style="italic",
)

plt.tight_layout()
plt.savefig("hexagonal-architecture.pdf", dpi=300, bbox_inches="tight")
print("hexagonal-architecture.pdf created")
