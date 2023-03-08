from summary import summarise
from transcript import transcribe
from math import ceil
from decouple import config

def split_string(string, chunk_size):
    """Split a string into chunks of specified size."""
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

API_KEY = config("API_KEY")
MAX_TRANSCRIPT_CHUNK_TOKEN_LENGTH = 3500

transcript = transcribe("../media/audio_13m.mp3", API_KEY)

transcript_tokens = len(transcript) / 3
max_tokens = 4097 - transcript_tokens - 5

amount_of_times_transcript_fits_into_max_token_length = ceil(len(transcript) / MAX_TRANSCRIPT_CHUNK_TOKEN_LENGTH)
chunk_length: int = ceil(len(transcript) / amount_of_times_transcript_fits_into_max_token_length)

# If the last chunk is too small, merge it with the previous chunk
chunks = split_string(transcript, chunk_length)
if len(chunks) >= 2 and len(chunks[-1]) < (len(chunks[-2])/2):
    # Merge last two chunks
    chunks[-2] += chunks[-1]
    chunks.pop()

# A token is equal to 3 characters. Given the max number of tokens that each chunk can have,
# split the transcript into chunks and for each call summarise
summaries = []
# for i in range(0, amount_of_times_transcript_fits_into_max_token_length):
    # chunk_audio_data = transcript[i*chunk_length, (i+1)*chunk_length]
for i, chunk in enumerate(chunks):
    prompt = f"The following is a chunk of a conversation between a customer care agent and a customer. This is chunk number {i} of {len(chunks)}. Summarize the customer's problems: {chunk}\n"
    summary = summarise(API_KEY, max_tokens, prompt)
    summaries.append(summary)

print('\nSummaries:\n')
print(summaries)

if len(summaries) > 0:
    summary = summarise(API_KEY, max_tokens,
    f"This are summaries of different pieces of the same conversation (in sequence) between a customer care agent and a customer. Generate a summary focusing on the customer's problems: {summaries}\n")


print('\nFinal summary:\n')
print(summary)

