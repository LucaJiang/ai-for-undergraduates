"""Minimal visualization for linear transformations and eigenvectors.

Use this file in Part 3 of the workshop to show how code can act as a
microscope for an abstract concept. The goal is not to solve homework, but to
see how a matrix changes vectors and why some directions are special.

Run:
    python examples/linear-transform-visualization.py
"""

import numpy as np
import matplotlib.pyplot as plt


def draw_vector(ax, vector, label, linestyle="-"):
    """Draw a 2D vector from the origin."""
    ax.arrow(
        0,
        0,
        vector[0],
        vector[1],
        head_width=0.08,
        length_includes_head=True,
        linestyle=linestyle,
    )
    ax.text(vector[0] * 1.08, vector[1] * 1.08, label, fontsize=12)


def main():
    # Try changing this matrix and observe which directions stay unchanged.
    A = np.array([[2.0, 0.8], [0.0, 1.0]])

    # A few test vectors. One is an eigenvector-like direction for this matrix.
    vectors = {
        "v1": np.array([1.0, 0.0]),
        "v2": np.array([0.0, 1.0]),
        "v3": np.array([1.0, 1.0]),
        "v4": np.array([-1.0, 1.0]),
    }

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("A vector before and after matrix transformation")
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.grid(True, linewidth=0.4)

    for name, v in vectors.items():
        Av = A @ v
        draw_vector(ax, v, name)
        draw_vector(ax, Av, f"A{name}", linestyle="--")

    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("Matrix A:\n", A)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors are columns of this matrix:\n", eigenvectors)
    print("\nConceptual question: which transformed vectors keep the same direction?")

    plt.show()


if __name__ == "__main__":
    main()
