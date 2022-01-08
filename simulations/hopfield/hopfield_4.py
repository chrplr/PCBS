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

def im_from_string(s):
    # extract each line which correspond to one row of the image
    lines = s.strip().split()
    # convert each character into a digit and concatenate them into a 2d array
    digits = [[(1 if c == '1' else -1) for c in line] for line in lines]
    return np.array(digits)

def state_from_im(im):
    return im.reshape((-1,))

def im_from_state(state, width):
    return state.reshape((-1, width))

def state_from_string(s):
    return state_from_im(im_from_string(s))

str_L = """
        1....
        1....
        1....
        1....
        11111
        """

str_P = """
        11111
        1...1
        11111
        1....
        1....
        """

str_S = """
        11111
        1....
        11111
        ....1
        11111
        """

str_X = """
        1...1
        .1.1.
        ..1..
        .1.1.
        1...1
        """

str_L_corrupted = (
    """
    1....
    1....
    1....
    1....
    11.11
    """)

str_L_corrupted_2 = (
    """
    1....
    1....
    11..1
    11.11
    11.11
    """)

str_P_corrupted = (
    """
    111.1
    1..11
    1.11.
    1.1..
    1....
    """)

str_X_corrupted = (
    """
    1..11
    .1.1.
    ..1..
    .1.1.
    11..1
    """)

str_X_corrupted_2 = (
    """
    1...1
    .111.
    ..1..
    .111.
    1...1
    """)

str_bars = (
    """
    1...1
    1...1
    1...1
    1...1
    1...1
    """)

str_wtf = (
    """
    1...1
    ....1
    1...1
    ....1
    1...1
    """)

str_zero = (
    """
    .....
    .....
    .....
    .....
    .....
    """)


if __name__ == '__main__':
    memory_states = [ state_from_string(s) for s in [str_L, str_P, str_S, str_X]]
    weight = weight_to_memorize_states(memory_states)

    for s in (str_L_corrupted, str_L_corrupted_2, str_P_corrupted,
        str_X_corrupted, str_X_corrupted_2, str_bars, str_wtf, str_zero):
        initial_state = state_from_string(s)
        final_state, is_stable, n_iter = compute_final_state(initial_state, weight)
        print("is_stable, n_iter", is_stable, n_iter)
        initial_im = im_from_state(initial_state, 5)
        final_im = im_from_state(final_state, 5)
        fig, axes = plt.subplots(nrows=1, ncols=2)
        axes[0].imshow(initial_im, cmap="binary")
        axes[0].set_title("Initial state")
        axes[1].imshow(final_im, cmap="binary")
        axes[1].set_title("Final state")
        plt.show()

