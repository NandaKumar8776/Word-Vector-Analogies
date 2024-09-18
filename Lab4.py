## Python Lab 4
# Group 12 - Nanda Kumar Balakrishnan

import time
import math

def dot_product(vec_a, vec_b):
    dot_prod = 0.0;
    for i in range(len(vec_a)):
        dot_prod += vec_a[i] * vec_b[i]
    return dot_prod

def magnitude(vector):
    return math.sqrt(dot_product(vector, vector))

def cosine_similarity(vec_a, vec_b):
    dot_prod = dot_product(vec_a, vec_b)
    magnitude_a = magnitude(vec_a)
    magnitude_b = magnitude(vec_b)

    return dot_prod / (magnitude_a * magnitude_b)

# To read the .vec file.
with open('c:\\data\\wiki-news-300d-1M.vec', "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Loading word vector dictionary")
print(time.strftime("%H:%M:%S", time.localtime()))

# Initializing a dictionary for storing words with their vectors, and a seperate cosine value dictionary.
word_dictionary = dict()

# Iterating through the .vec file to store the words and their associated vector values.
for line in lines[1:]:
    line = line.split()
    word_dictionary[line[0]] = [float(i) for i in line[1:]]

# Printing out the time taken to load the text file.
print(time.strftime("%H:%M:%S", time.localtime()))

# Format for printing the output.
print("Word vector dictionary is loaded")
print()
print("G12- Lab #4 - by NandaKumar BalaKrishnan and DeepthiShree Saravanan")
print("Analogies take the form: A is to B as C is to D")
print("Example: \'man is to woman as king is to queen\'")
print()
print("Enter the previous example as: man woman king")
print("The computer will return the full solution: man is to woman as king is to queen")

# Entering loop to prevent reading the file again.
while True:
    print()

    # Receiving the entered 3 words.
    input_string = input("Enter 3 analogy word tokens: ")
    
    # Ends if nothing is entered
    if (input_string == ''):
        break

    print("Processing analogy...")

    # Spliting to obtain the entered words.
    input_string = input_string.strip().split(' ')

    # Obtaining the vector data of the 3 words, using the word dictionary.
    vector1 = word_dictionary[input_string[0]]
    vector2 = word_dictionary[input_string[1]]
    vector3 = word_dictionary[input_string[2]]

    # Calculating vector 4 and 5.
    vector4 = [x - y for x, y in zip(vector2, vector1)]
    vector5 = [x + y for x, y in zip(vector4, vector3)]

    # Initializing a list of 0's to store the highest similarity word similarity cosines.
    similarity_list = [0.0]*20
    cosine_dictionary = dict()

    # For loop which iterates through all words, produce cosine similarites comparing vector 5 and 6.
    for key in word_dictionary.keys():
        
        vector6 = word_dictionary[key]

        cosine_sim = cosine_similarity(vector5,vector6)
        cosine_dictionary[cosine_sim] = key

        # Checks if cosine similarity value is greater that each element in list by checking last element since it is sorted.
        # Also not adding the cosine similary if the word is same as the input word. 
        if cosine_sim > similarity_list[-1] and (key not in input_string):

            similarity_list[-1] = cosine_sim
            similarity_list.sort(reverse=True)
        
    # Printing out the output.
    print()
    print(input_string[0] + " is to " + input_string[1] + " as " + input_string[2] + " is to " + cosine_dictionary[similarity_list[0]])
    print()

    for cos in similarity_list:
        print(str(cos) +"\t" + cosine_dictionary[cos])
