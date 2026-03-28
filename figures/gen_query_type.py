"""Generate Figure 4: Query Type Performance bar chart."""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "serif"
matplotlib.rcParams["font.size"] = 11

categories = ["Factual\n(n=150)", "Conceptual\n(n=200)", "Multi-hop\n(n=150)"]
bm25 = [0.81, 0.52, 0.44]
semantic = [0.79, 0.83, 0.62]
hybrid = [0.87, 0.87, 0.75]

x = np.arange(len(categories))
width = 0.24

fig, ax = plt.subplots(figsize=(7, 4.5))

colors = {"BM25": "#60a5fa", "Semantic": "#fb923c", "Hybrid": "#34d399"}

bars1 = ax.bar(
    x - width,
    bm25,
    width,
    label="BM25",
    color=colors["BM25"],
    edgecolor="white",
    linewidth=0.5,
)
bars2 = ax.bar(
    x,
    semantic,
    width,
    label="Semantic",
    color=colors["Semantic"],
    edgecolor="white",
    linewidth=0.5,
)
bars3 = ax.bar(
    x + width,
    hybrid,
    width,
    label="Hybrid (RRF)",
    color=colors["Hybrid"],
    edgecolor="white",
    linewidth=0.5,
)

# Value labels on bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.2f}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )

ax.set_ylabel("Precision@5", fontsize=12)
ax.set_ylim(0, 1.05)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=10)
ax.legend(loc="upper right", fontsize=10, framealpha=0.9)
ax.grid(True, axis="y", alpha=0.3, linestyle="--")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("query-type-performance.pdf", dpi=300, bbox_inches="tight")
print("query-type-performance.pdf created")
