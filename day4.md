# Day 4: Word Embeddings

- Frequency / count
	- BOW
	- TF-IDF
	- OHE
- Deep Learning Trained Models
	- Word2Vec
		- CBOW (continuous bag of words)
		- Skip Grams

## Word2Vec
Word2Vec is a word embedding technique in natural language processing (NLP) that allows words to be represented as vectors in a continuous vector space. It works on the principle that words with similar meanings should have similar vector representations.

**Word2Vec utilizes two architectures:**
1. CBOW
2. Skip Grams

### CBOW (Continuous Bag of Words)
**Goal:** Predict the **target word** using its **context words**.

CBOW takes multiple context words around a missing word and tries to guess the missing (center) word.  
In simple terms: **“Given neighbors → predict the center word.”**

![w2v_0](images/w2v_0.png)
![w2v_1](images/w2v_1.png)
![w2v_2](images/w2v_2.png)

#### Example
lets take a sentence: "Learning NLP feels really so amazing".
Here lets take context window size = 5
then,

**Step 1:**
1: input -> 'Learning NLP really so', output -> 'feels'
2: input -> 'NLP feels so amazing', output -> 'really'

**Step 2:**
Create bag of words for each word
'Learning':     [1, 0, 0, 0, 0, 0]
'NLP':            [0, 1, 0, 0, 0, 0]
'feels':           [0. 0. 1. 0. 0. 0]
'really':          [0. 0. 0, 1. 0. 0]
'so':               [0. 0. 0, 0, 1. 0]
'amazing':     [0. 0. 0, 0, 0, 1]

**Step 3:**
Now, build an ANN with 4 inputs (as we have 4 words in context, each with 6 neurons) and 1 hidden layer (with 5 neurons, as context window size = 5), and one output (with 6 neurons, as one word has 6 values)

Then, train the ANN.
### Skip Grams
The Skip gram predicts the surrounding context words within specific window given current word. The input layer contains the current word and the output layer contains the context words. The hidden layer contains the number of dimensions in which we want to represent current word present at the input layer.
![skip grams](images/skip_grams.png)


*Good blog: [Word2Vec — CBOW (implementation explained) | by Harsh Chauhan | Medium](https://medium.com/@harshtherocking/word2vec-cbow-implementation-explained-3b7ee6dbcd32)*

