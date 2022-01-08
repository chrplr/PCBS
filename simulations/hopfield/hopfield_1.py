import numpy as np
import matplotlib.pyplot as plt

def compute_next_state(state, weight):
    """
    This implements the syncrhonous update rule in a Hopfield network:
    all the units are updated at the same time in one iteration.

    Parameters
    ----------
    state: array of shape (N,)
        state vector with binary values, coded as +1 or -1
    weight: 2d array of shape (N, N)
        weight matrix where weight[i, j] is the connection weight from
        unit j to unit i and from unit i to unit j (connections are symmetric
        in a Hopfield network)

    Returns
    -------
    next_state: array of shape (N,)
    """
    # Note: '@' is a shorthand for 'np.matmul()'. Numpy automatically promotes
    # 1D arrays (vectors) into 2D arrays (matrices) before applying the
    # matrix multiplication, turning the left operand (here 'state') into a
    # matrix of shape (1, N). After applying the matrix multiplication,
    # numpy then perform the inverse transformation to give back a 1D array.
    next_state = np.where(state @ weight >= 0, +1, -1)
    return next_state

def compute_final_state(initial_state, weight, max_iter=1000):
    """
    Returns
    -------
    final_state: array of shape (N,)
    is_stable: bool
        whether the final state is a stable state
    n_iter: int
        number of iterations of compute_next_state performed
    """
    previous_state = initial_state
    next_state = compute_next_state(previous_state, weight)
    is_stable = np.all(previous_state == next_state)
    n_iter = 0
    while (not is_stable) and (n_iter <= max_iter):
        previous_state = next_state
        next_state = compute_next_state(previous_state, weight)
        is_stable = np.all(previous_state == next_state)
        n_iter += 1

    return previous_state, is_stable, n_iter


if __name__ == '__main__':
    initial_state = np.array([+1, -1, -1, -1])
    weight = np.array([
        [0, -1, -1, +1],
        [-1, 0, +1, -1],
        [-1, +1, 0, -1],
        [+1, -1, -1, 0]])
    final_state, is_stable, n_iter = compute_final_state(initial_state, weight)
    print("final_state", final_state)
    print("is_stable", is_stable)
