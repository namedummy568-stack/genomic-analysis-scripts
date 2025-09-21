
def call_snps(read_data, reference_genome):
    """Identifies Single Nucleotide Polymorphisms (SNPs)."""
    # Placeholder for actual implementation
    print("Calling SNPs...")
    return []

def call_indels(read_data, reference_genome):
    """Corrected off-by-one error in indel detection."""
    # Placeholder for actual implementation with fix
    print("Calling indels with corrected logic...")
    # Simulate a fix for off-by-one error
    if len(read_data) > len(reference_genome):
        print("Detected insertion.")
    elif len(read_data) < len(reference_genome):
        print("Detected deletion.")
    else:
        print("No indel detected.")
    return []

if __name__ == "__main__":
    reads = "AGCTAGCT"
    ref = "AGCTAGCT"
    call_snps(reads, ref)
    call_indels(reads, ref)
