import numpy as np

def get_indices(N, n_batches, split_ratio):
    """Generates splits of indices from 0 to N-1 into uniformly distributed\
       batches. Each batch is defined by 3 indices [i, j, k] where\
       (j-i) = split_ratio*(k-j). The first batch starts with i = 0,\
       the last one ends with k = N - 1.
    Args:
        N (int): total counts
        n_batches (int): number of splits
        split_ratio (float): split ratio, defines position of j in [i, j, k].
        split_ratio = (j-i)/(k-j)
    Returns:
        generator for batch indices [i, j, k]
    """
    a = (N-1)/(n_batches+1/split_ratio)
    step = np.array([a for i in range(3)])
    inds = np.array([0, a/split_ratio, a*(1+1/split_ratio)])
    for i in range(n_batches):
        yield (inds+0.5)//1
        inds = inds + step

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()
