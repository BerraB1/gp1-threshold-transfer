"""Table 3: effect of calibration size on threshold precision.

If the threshold is the k-th largest score (k = n*alpha) of an n-flow normal calibration set,
the true FPR follows Beta(k, n - k + 1) (Umsonst et al., 2021, 2023). Valid only when
calibration and test normals are i.i.d. from the same distribution.
"""
from scipy.stats import beta


def fpr_upper_bound(alpha, n, conf=0.95):
    k = max(1, round(n * alpha))
    return float(beta.ppf(conf, k, n - k + 1))


def main():
    print("alpha  n  n*alpha  upper95  upper/alpha")
    for alpha in (0.001, 0.01, 0.05):
        for n in (1000, 10000, 100000):
            ub = fpr_upper_bound(alpha, n)
            print(alpha, n, round(n * alpha), round(ub, 5), round(ub / alpha, 2))
    for alpha in (0.001, 0.01, 0.05):  # as-is transfer: source validation n = 50000
        print("n=50000", alpha, round(fpr_upper_bound(alpha, 50000), 5))


if __name__ == "__main__":
    main()
