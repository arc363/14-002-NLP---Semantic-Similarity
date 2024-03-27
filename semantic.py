import spacy

nlp = spacy.load('en_core_web_md')

print("-------- Practical Task 1 --------\n")

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')
word4 = nlp('could')
print(word1, word2, word3)
print(round(word1.similarity(word2), 3))
print(round(word1.similarity(word3), 3))
print(round(word2.similarity(word3), 3))
print("Comment: as noted in the documentation, the highest similarity is "
      "between the two animals; \"banana\" is more similar to \"monkey\" than "
      "to \"cat\". ")
print()
word1 = nlp('jump')
word2 = nlp('think')
word3 = nlp('sprint')
print(word1, word2, word3)
print(round(word1.similarity(word2), 3))
print(round(word1.similarity(word3), 3))
print(round(word2.similarity(word3), 3))
print("Comment: the highest similarity is between the verbs \"jump\" and "
      "\"think\", which are closer semantically than either verb and \"think\""
      ".")

print("\nComment: comparing the complaints vs recipes example with two "
      "language models \nThe semantic similarity scores are significantly "
      "lower when the simpler language model is used. This indicates that "
      "semantic similarity between texts may be underestimated and the "
      "program's performance affected.\n")

print("Working with vectors")

tokens = nlp('water sea calm liquid')

for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text:{8}} {token2.text:{8}} {round(token1.similarity(token2), 3)}")
        

print("\nWorking with sentences")
sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in the car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = round(nlp(sentence).similarity(model_sentence), 3)
    print(f"{sentence:{30}} {str(similarity)}")
