
def global_align(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """Performs global alignment using Needleman-Wunsch algorithm."""
    # Placeholder for actual implementation
    print(f"Aligning {seq1} and {seq2} globally.")
    return 0 # Placeholder score

def local_align(seq1, seq2, match=2, mismatch=-1, gap=-1):
    """Implemented Smith-Waterman algorithm for local alignment."""
    # Actual Smith-Waterman implementation (simplified for example)
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    score_matrix = [[0] * cols for _ in range(rows)]
    max_score = 0

    for i in range(1, rows):
        for j in range(1, cols):
            match_mismatch = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            delete = score_matrix[i-1][j] + gap
            insert = score_matrix[i][j-1] + gap
            score_matrix[i][j] = max(0, match_mismatch, delete, insert)
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]

    print(f"Locally aligning {seq1} and {seq2} with Smith-Waterman. Max score: {max_score}")
    return max_score

if __name__ == "__main__":
    s1 = "ATGC"
    s2 = "ATGC"
    global_align(s1, s2)
    local_align(s1, s2)
