# Compute the KL divergence between two probability distributions
import numpy as np


def kl_divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


if __name__ == "__main__":
    # Define two probability distributions p and q
    p = np.array([0.1, 0.2, 0.3, 0.4])
    q = np.array([0.2, 0.2, 0.2, 0.4])

    # Compute the KL divergence between the p and q
    kl = kl_divergence(p, q)

    print(f"KL(p||q) = {kl:.4f}")
