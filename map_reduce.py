from collections import defaultdict

# Read the tokenized text file
with open('tokenized_text_by_id.txt', 'r') as file:
    tokenized_text_by_id = file.read()

# Split the text into lines, each line representing tokenized text for a specific ARTICLE_ID
articles = tokenized_text_by_id.strip().split('\n\n')

# Initialize a dictionary to store unique terms across all articles
unique_terms_all = set()

# Iterate through each ARTICLE_ID section to collect unique terms
for article in articles:
    lines = article.split('\n')
    text = ' '.join(lines[1:])  # Extract tokenized text
    tokens = text.split()  # Split text into tokens
    unique_terms_all.update(tokens)  # Add tokens to set of unique terms

# Create a vocabulary with unique terms and assign unique IDs
vocabulary = {term: idx for idx, term in enumerate(unique_terms_all)}

# Mapper function to emit intermediate key-value pairs
def mapper(token):
    if token in vocabulary:
        yield (token, 1)

# Reducer function to aggregate intermediate key-value pairs
def reducer(term, frequencies):
    yield (vocabulary[term], sum(frequencies))

# Initialize a defaultdict to store intermediate key-value pairs
intermediate = defaultdict(list)

# Map step
for article in articles:
    tokens = article.split()[1:]  # Extract tokenized text, excluding ARTICLE_ID
    for token in tokens:
        for key, value in mapper(token):
            intermediate[key].append(value)

# Reduce step
tf_list = []
for term, frequencies in intermediate.items():
    for key, value in reducer(term, frequencies):
        tf_list.append((key, value))

# Sort the list based on the term IDs
tf_list.sort()

# Print the term frequency list
print("Term Frequency (TF):")
for item in tf_list:
    print(item)
