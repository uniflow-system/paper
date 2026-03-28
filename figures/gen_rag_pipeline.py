"""Generate Figure 2: RAG Pipeline Flowchart."""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.size"] = 10

fig, ax = plt.subplots(figsize=(12, 5))
ax.set_xlim(-0.5, 12.5)
ax.set_ylim(-1, 5.5)
ax.axis("off")

# Color palette
C_QUERY = "#dbeafe"  # light blue
C_BM25 = "#fef3c7"  # light yellow
C_SEM = "#d1fae5"  # light green
C_FUSION = "#fce7f3"  # light pink
C_LLM = "#ede9fe"  # light purple
C_RESP = "#f0fdf4"  # light mint
C_BORDER = "#374151"  # dark gray


def draw_box(ax, x, y, w, h, text, color, fontsize=9, bold=False):
    box = mpatches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.15",
        facecolor=color,
        edgecolor=C_BORDER,
        linewidth=1.2,
    )
    ax.add_patch(box)
    weight = "bold" if bold else "normal"
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        wrap=True,
    )


def draw_arrow(ax, x1, y1, x2, y2, label=""):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", color=C_BORDER, lw=1.5),
    )
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(
            mx,
            my + 0.2,
            label,
            ha="center",
            va="bottom",
            fontsize=7,
            color="#6b7280",
            style="italic",
        )


# Row positions
top_y = 3.2
mid_y = 1.8
bot_y = 0.3

# Box dimensions
bw, bh = 1.6, 0.9

# 1. User Query
draw_box(ax, 0, mid_y, bw, bh, "User\nQuery", C_QUERY, fontsize=10, bold=True)

# 2. Fork point
ax.plot(2.1, mid_y + bh / 2, "o", color=C_BORDER, markersize=6)

# 3. BM25 path (top)
draw_box(ax, 2.8, top_y, bw, bh, "BM25\n(Lexical)", C_BM25, fontsize=9, bold=True)
draw_box(ax, 5.0, top_y, bw, bh, "Top-10\nResults", C_BM25)

# 4. Semantic path (bottom)
draw_box(ax, 2.8, bot_y, bw, bh, "Semantic\n(bge-small)", C_SEM, fontsize=9, bold=True)
draw_box(ax, 5.0, bot_y, bw, bh, "Top-10\nResults", C_SEM)

# 5. RRF Fusion
draw_box(ax, 7.2, mid_y, bw, bh, "RRF Fusion\n(c=60)", C_FUSION, fontsize=10, bold=True)

# 6. Context + LLM
draw_box(
    ax, 9.4, mid_y, bw, bh, "Qwen2.5-3B\n(4-bit NF4)", C_LLM, fontsize=9, bold=True
)

# 7. Response
draw_box(ax, 11.3, mid_y, 1.0, bh, "Response", C_RESP, fontsize=10, bold=True)

# Arrows: Query -> fork
draw_arrow(ax, 1.6, mid_y + bh / 2, 2.1, mid_y + bh / 2)

# Fork -> BM25, Fork -> Semantic
draw_arrow(ax, 2.1, mid_y + bh / 2, 2.8, top_y + bh / 2)
draw_arrow(ax, 2.1, mid_y + bh / 2, 2.8, bot_y + bh / 2)

# BM25 -> Top-10, Semantic -> Top-10
draw_arrow(ax, 4.4, top_y + bh / 2, 5.0, top_y + bh / 2, "18ms")
draw_arrow(ax, 4.4, bot_y + bh / 2, 5.0, bot_y + bh / 2, "12+24ms")

# Top-10s -> RRF
draw_arrow(ax, 6.6, top_y + bh / 2, 7.2, mid_y + bh / 2)
draw_arrow(ax, 6.6, bot_y + bh / 2, 7.2, mid_y + bh / 2)

# RRF -> LLM
draw_arrow(ax, 8.8, mid_y + bh / 2, 9.4, mid_y + bh / 2, "3ms")

# LLM -> Response
draw_arrow(ax, 11.0, mid_y + bh / 2, 11.3, mid_y + bh / 2, "95ms")

# Latency summary
ax.text(
    6.3,
    -0.6,
    "End-to-End: 410ms  |  Retrieval: 65ms (16%)  |  Generation: 345ms (84%)",
    ha="center",
    va="center",
    fontsize=9,
    color="#374151",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#f3f4f6", edgecolor="#9ca3af"),
)

plt.tight_layout()
plt.savefig("rag-pipeline.pdf", dpi=300, bbox_inches="tight")
print("rag-pipeline.pdf created")
