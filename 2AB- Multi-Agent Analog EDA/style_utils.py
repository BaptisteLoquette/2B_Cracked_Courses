"""
3Blue1Brown-inspired visualization utilities for the Multi-Agent Analog EDA course.

Usage in notebooks:
    import sys; sys.path.insert(0, '..')
    from style_utils import *
    setup_3b1b_style()
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap

# ─── 3B1B Color Palette ───────────────────────────────────────────
BACKGROUND = "#1c1c1c"
SURFACE = "#252525"
TEXT = "#ece6d5"
TEXT_DIM = "#888888"
GRID = "#333333"

BLUE = "#3b82f6"
TEAL = "#06b6d4"
GREEN = "#10b981"
YELLOW = "#eab308"
GOLD = "#f59e0b"
RED = "#ef4444"
ROSE = "#f43f5e"
PURPLE = "#8b5cf6"
CYAN = "#22d3ee"
ORANGE = "#f97316"

PALETTE = [BLUE, TEAL, GREEN, YELLOW, RED, PURPLE, ORANGE, ROSE, CYAN, GOLD]


def setup_3b1b_style():
    """Apply 3Blue1Brown-inspired matplotlib style globally."""
    mpl.rcParams.update({
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": BACKGROUND,
        "axes.edgecolor": GRID,
        "axes.labelcolor": TEXT,
        "axes.titlesize": 16,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "axes.titlepad": 16,
        "axes.grid": True,
        "axes.prop_cycle": mpl.cycler(color=PALETTE),

        "grid.color": GRID,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.5,

        "xtick.color": TEXT_DIM,
        "ytick.color": TEXT_DIM,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,

        "text.color": TEXT,
        "font.size": 11,
        "font.family": "sans-serif",

        "legend.facecolor": SURFACE,
        "legend.edgecolor": GRID,
        "legend.fontsize": 10,
        "legend.framealpha": 0.9,

        "figure.dpi": 150,
        "savefig.dpi": 150,
        "savefig.facecolor": BACKGROUND,

        "lines.linewidth": 2.2,
        "lines.antialiased": True,
    })


def glow_line(ax, x, y, color, label=None, linewidth=2.5, glow_width=8, alpha=0.15):
    """Draw a line with a soft glow effect (3B1B signature style)."""
    ax.plot(x, y, color=color, linewidth=glow_width, alpha=alpha)
    ax.plot(x, y, color=color, linewidth=glow_width * 0.6, alpha=alpha * 1.5)
    ax.plot(x, y, color=color, linewidth=linewidth, alpha=1.0, label=label)


def glow_fill(ax, x, y1, y2, color, alpha=0.08):
    """Fill between with soft glow gradient."""
    ax.fill_between(x, y1, y2, color=color, alpha=alpha)
    ax.fill_between(x, y1, y2, color=color, alpha=alpha * 0.5)


def styled_box(ax, x, y, w, h, label, sublabel, color, fontsize=10):
    """Draw a rounded box with label and sublabel for architecture diagrams."""
    rect = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.12",
        facecolor=color, alpha=0.15,
        edgecolor=color, linewidth=2
    )
    ax.add_patch(rect)
    ax.text(x + w / 2, y + h * 0.62, label,
            fontsize=fontsize, fontweight="bold",
            color=color, ha="center", va="center")
    if sublabel:
        ax.text(x + w / 2, y + h * 0.28, sublabel,
                fontsize=max(fontsize - 3, 7),
                color=TEXT_DIM, ha="center", va="center")


def styled_arrow(ax, x1, y1, x2, y2, color="white", lw=1.5, style="->"):
    """Draw a clean directional arrow."""
    ax.annotate(
        "", xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                        connectionstyle="arc3,rad=0")
    )


def finish_plot(fig=None, ax=None):
    """Apply final styling to a plot."""
    if fig is None:
        fig = plt.gcf()
    fig.patch.set_facecolor(BACKGROUND)
    if ax is not None:
        ax.set_facecolor(BACKGROUND)
        for spine in ax.spines.values():
            spine.set_color(GRID)
    plt.tight_layout()


def plotly_3b1b_layout():
    """Return a dict of Plotly layout properties for 3B1B style."""
    return dict(
        template="plotly_dark",
        paper_bgcolor=BACKGROUND,
        plot_bgcolor=BACKGROUND,
        font=dict(color=TEXT, family="sans-serif"),
        title_font=dict(size=16),
    )
