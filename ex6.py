from collections import defaultdict
def calculate_ngram_probabilities(corpus):
    ngrams = defaultdict(int)
    context = defaultdict(int)
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words) - 2):
            trigram = (words[i], words[i+1], words[i+2])
            ngrams[trigram] += 1
            context[trigram[:2]] += 1
    probabilities = defaultdict(float)
    for trigram, count in ngrams.items():
        context_count = context[trigram[:2]]
        probability = (count + 1) / (context_count + len(ngrams))
        probabilities[trigram] = probability
    return probabilities
corpus = [
    "I love to code",
    "I love to learn",
    "I love NLP",
    "I enjoy to code"
]
trigram_probabilities = calculate_ngram_probabilities(corpus)
for trigram, probability in trigram_probabilities.items():
    print(f"Trigram: {trigram}, Probability: {probability:.4f}")