# Word Vector Analogies

## Description
This Python program implements a word vector analogy solver using FastText word embeddings. The main goal of the application is to solve analogies like:
- **man is to woman as king is to queen**
- **doctor is to hospital as teacher is to school**

The program reads word vectors from a FastText file, processes the input analogy, and calculates the most similar word to complete the analogy using cosine similarity between vectors.

## Objective
The main objective of the lab is to practice using word embeddings to solve word analogies through vector math, including subtraction and addition of word vectors, and finding the most similar word to complete the analogy.

## Requirements
- Python 3.x
- FastText word vector file (e.g., `wiki-news-300d-1M.vec` or `FastText100K.txt` for faster debugging).
- Libraries:
  - `time`
  - `math`

## Setup
1. **Download FastText Vectors**:
   - You can download the word vectors from [Facebook FastText](https://fasttext.cc/docs/en/english-vectors.html).
   - Use the smaller file (`FastText100K.txt`) for debugging and testing purposes.
2. **Place the vector file** in the directory where your Python script is located or provide the full path to it.
3. **Install necessary packages** using pip (if needed):
   ```bash
   pip install time
   ```

## Usage
1. **Run the Program**:
   ```bash
   python Nandakumar_Lab4.py
   ```
2. **Input Format**:
   - The program prompts you to enter three words: the first two form a pair of analogy, and the third word represents the start of the second pair.
   - Example: For the analogy "man is to woman as king is to queen," enter:
     ```
     man woman king
     ```

3. **Expected Output**:
   - The program calculates the vector analogy and provides the correct analogy solution:
     ```
     man is to woman as king is to queen
     ```

## Code Walkthrough

### Functions

- **`dot_product(vec_a, vec_b)`**:
  - Calculates the dot product between two vectors.
  
- **`magnitude(vector)`**:
  - Computes the magnitude (length) of a vector.
  
- **`cosine_similarity(vec_a, vec_b)`**:
  - Calculates the cosine similarity between two vectors.
  
- **Main Program Flow**:
  - Loads the FastText word vector file into memory.
  - Prompts the user to input three words representing the analogy.
  - Calculates the missing word by performing vector operations (subtraction and addition).
  - Uses cosine similarity to find the most similar word from the dictionary.

### Vector Analogy Formula
The program calculates the analogy "A is to B as C is to D" using the following vector math:
- Vector 5 (C - A + B) is compared to all words in the dictionary to find the word D that maximizes cosine similarity.

## Example Usage
```
Loading word vector dictionary
16:22:11
16:22:14
Word vector dictionary is loaded

G12- Lab #4 - by Nanda Kumar Balakrishnan
Analogies take the form: A is to B as C is to D
Example: 'man is to woman as king is to queen'

Enter the previous example as: man woman king

Enter 3 analogy word tokens: man woman king
Processing analogy...

man is to woman as king is to queen
```

## Output Examples
For testing purposes, the program should complete at least three valid analogy runs and display the results.

### Analogies to Test:
1. **man woman king**
   - Output: `man is to woman as king is to queen`
2. **doctor hospital teacher**
   - Output: `doctor is to hospital as teacher is to school`
3. **grass green sky**
   - Output: `grass is to green as sky is to blue`

## Notes
- The larger word vector file (`wiki-news-300d-1M.vec`) will take longer to load, so it’s recommended to use the smaller version (`FastText100K.txt`) for faster debugging.
- After processing, the program displays the cosine similarity scores of the top 20 matches.

## License
This project is part of academic coursework for Python Lab 4 at Fanshawe College.
