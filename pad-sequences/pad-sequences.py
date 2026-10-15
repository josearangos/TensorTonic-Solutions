import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """

    if not seqs:
        return np.empty((0,0), dtype=np.int16)

    N = len(seqs)
    L = max(len(seq) for seq in seqs) or 0

    if max_len is not None:
        L = max_len


    result = np.full((N,L), fill_value=pad_value)

    print(result.shape)

    for i in range(N):
        j = 0
        while j < len(seqs[i]) and j<L:
            result[i][j] = seqs[i][j]
            j+=1

    return result