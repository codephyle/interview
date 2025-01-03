#  Given 'n' sorted sequences, compute the union of these sequences as a sorted sequence.
import heapq

def merge_sorted_sequences(sequences):
    # Initialize an empty result list and a priority queue (min heap)
    result = []
    pq = []

    # Initialize the priority queue with the first element of each sequence
    for i, seq in enumerate(sequences):
        if seq:  # check if the sequence is not empty
            heapq.heappush(pq, (seq[0], i, 0))  # (value, sequence index, index in sequence)

    # Merge the sequences using a min heap
    while pq:
        value, seq_index, index_in_seq = heapq.heappop(pq)
        result.append(value)  # add the current value to the result

        # Move to the next element in the current sequence
        index_in_seq += 1

        # If there are more elements in the current sequence, push the next element to the heap
        if index_in_seq < len(sequences[seq_index]):
            next_value = sequences[seq_index][index_in_seq]
            heapq.heappush(pq, (next_value, seq_index, index_in_seq))

    return result

# Example usage:
sequences = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
print(merge_sorted_sequences(sequences))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]


union([3, 5, 7], [0, 6], [0, 6, 28]) == [0, 0, 3, 5, 6, 6, 7, 28]
