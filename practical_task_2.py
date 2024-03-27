import spacy
import csv

nlp = spacy.load('en_core_web_md')

# Variable containing the file path
file_path = 'movies.txt'

# Initialise an empty dictionary to store the data
films_dict = {}

# Open the file in read mode
with open(file_path, 'r') as file:
    # Create a CSV reader with colon as the delimiter
    reader = csv.reader(file, delimiter=':')

    # Loop through each row in the file
    for row in reader:
        # Assuming there are at least two columns in each row
        if len(row) >= 2:
            # Extract the movie title (first column) and the rest of the text
            film_title = row[0].strip()
            film_description = ":".join(row[1:]).strip()

            # Add the data to the dictionary
            films_dict[film_title] = film_description
        else:
            print(f"Invalid row: {row}")

# Variable containing the film description to be compared with each
# film description in films_dict
query_description = "Will he save their world or destroy it? When the Hulk \
                    becomes too dangerous for the Earth, the Illuminati trick \
                    Hulk into a shuttle and launch him into space to a planet \
                    where the Hulk can live in peace. Unfortunately, Hulk \
                    lands on the planet Sakaar where he is sold into slavery \
                    and trained as a gladiator."

print("\n------ Query <> Film descriptions similarity scores ------\n")

# Empty dictionary to contain similarity scores
scores = {}


def calculate_similarity(description, p_query_description):
    '''Function compares the semantic similarity of the query description 
    with the film descriptions which make up the list of options'''
    doc1 = nlp(description)
    doc2 = nlp(p_query_description)
    return doc1.similarity(doc2)


# Iterate through film dictionary, creating a similarity score for each
# film and inserting it to the scores dictionary
for film, description in films_dict.items():
    similarity_score = calculate_similarity(description, query_description)
    scores[film] = similarity_score
    print(f"{film:11} {round(similarity_score, 3)}")

# Identify highest similarity score and save film to variable
recommended_film = max(scores, key=scores.get)

# Print recommendation 
print(f"\nRecommended film: {recommended_film}\n")

