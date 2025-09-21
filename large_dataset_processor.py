
import gc

def process_large_data(data_path, chunk_size=10000):
    """Processes large datasets in chunks to optimize memory usage."""
    print(f"Processing data from {data_path} in chunks of {chunk_size}.")
    processed_records = 0
    # Simulate reading and processing data in chunks
    for i in range(5):
        print(f"  Processing chunk {i+1}...")
        # Simulate memory-intensive operation
        temp_data = [j for j in range(chunk_size)]
        processed_records += len(temp_data)
        del temp_data # Explicitly delete to free memory
        gc.collect() # Force garbage collection
    print(f"Finished processing {processed_records} records.")
    return processed_records

if __name__ == "__main__":
    process_large_data("genomic_data.csv")
