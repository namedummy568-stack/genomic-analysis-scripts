
def global_align(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """Performs global alignment using Needleman-Wunsch algorithm."""
    # Placeholder for actual implementation
    print(f"Aligning {seq1} and {seq2} globally.")
    return 0 # Placeholder score

def local_align(seq1, seq2, match=2, mismatch=-1, gap=-1):
    """Performs local alignment using Smith-Waterman algorithm."""
    # Placeholder for actual implementation
    print(f"Aligning {seq1} and {seq2} locally.")
    return 0 # Placeholder score

if __name__ == "__main__":
    s1 = "ATGC"
    s2 = "ATGC"
    global_align(s1, s2)
    local_align(s1, s2)
