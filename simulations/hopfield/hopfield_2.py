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
    next_state: array of shape (N)
    """
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

def weight_to_memorize_states(states):
    """
    Parameters
    ----------
    states: sequence of arrays of shape (N,)
        the states to be memorized
    
    Returns
    -------
    weight: 2d array of shape (N, N)
        the weight matrix that will memorize the given states
    """
    # concatenate into a matrix with each state as one column of this matrix 
    states_matrix = np.column_stack(states)
    # this will compute the sum of the outer products of each column vectors
    # in the matrix, which are the given states
    weight = states_matrix @ states_matrix.T
    # zero out the diagonal (there are no self-recurrent connections in Hopfield
    # networks)
    np.fill_diagonal(weight, 0)
    return weight

if __name__ == '__main__':

    state_1 = np.array([+1, -1, -1, +1])
    state_2 = np.array([-1, +1, +1, +1])
    memory_states = (state_1, state_2)
    print("memorized states")
    for state in memory_states:
        print(state)

    weight = weight_to_memorize_states(memory_states)
    print("weight\n", weight)

    initial_states = [
        np.array([+1, -1, -1, -1]), # 1 bit flipped from state_1
        np.array([-1, +1, +1, -1]), # 1 bit flipped from state_2
        np.array([-1, -1, +1, -1]), # 2 bits from state_2, 3 bits from state_1
    ]
    for initial_state in initial_states:
        final_state, is_stable, n_iter = compute_final_state(initial_state, weight)
        print(f"initial state {initial_state} -> final state {final_state}, is stable? {is_stable}")

