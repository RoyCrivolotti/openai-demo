def split_conversation(string, chunk_size):
    indexes = [0]
    # indexes of a given character in a string
    indexes = indexes + [i for i, char in enumerate(string) if char == "."]

    indexes.append(len(string))

    chunks = []
    chunk_to_add = ''
    for i in range(1, len(indexes)):
        current_index = indexes[i]
        previous_index = indexes[i - 1]

        current_chunk = string[previous_index:current_index]

        test_chunk = chunk_to_add + current_chunk

        if len(test_chunk) > chunk_size:
            chunks.append(chunk_to_add)
            chunk_to_add = ""
        else:
            chunk_to_add = test_chunk

    if current_chunk:
        chunks.append(current_chunk)

    return chunks