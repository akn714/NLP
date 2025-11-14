![Image](nlp.png)

## Step 1: Text Preprocessing

```
Tokenization -> Stopwords -> Stemming -> Lemmatization
```

**1. Tokenization**: Converting sentence into words
**2. Stopwords**: Removing unnecessary words like 'to', 'is', 'and', etc.
**3. Stemming**: Reducing the words to their base word.

```
Finally, Final, Finalist -> Fina (This may not have any meaning)
```

| Advantages              | Disadvantages                          |
| ----------------------- | -------------------------------------- |
| Stemming is really fast | It is removing the meaning of the word |
**4. Lemmatization**: Similar to stemming but here the words are converted to meaningful words.

| Advantages              | Disadvantages |
| ----------------------- | ------------- |
| We get meaningful words | It is slow    |

#### ML Usecase

| Stemming              | Lemmatization        |
| --------------------- | -------------------- |
| Spam classification   | Text summarization   |
| Review classification | Language translation |
|                       | Chatbots             |

## Step 2: Words -> Vectors

1. Bag of words
2. TF-IDF (Term Frequency - Inverse Document Frequency)
3. Word2Vec