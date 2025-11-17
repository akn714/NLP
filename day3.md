# Day 3

### 3. TF-IDF (Term Frequency - Inverse Document Frequency)

**Procedure:**
Step 1: Apply stopwords on the corpus
Step 2: Calculate the frequencies of all the words in the corpus
Step 3: Calculate TF and IDF for all the remaining words in the corpus
Step 4: Create a sparse matrix by calculating `TFxIDF` of all the words

$$
\text{Term Frequency} = \frac{\text{Number of repeated occurrences of the word}}{\text{Total number of words in the sentence}}
$$
$$
\text{IDF} = \log_c \left( \frac{\text{no. of sentences}}{\text{no. of sentences containing the word}} \right)
$$
$$
TF-IDF = TF \times IDF
$$

**Example:**
D1 -> He is a good boy -> good boy
D2 -> She is a good girl -> good girl
D3 -> Boy and Girl are good -> boy girl good
*in the second phase we have removed unnecessary words using stopwords

#### Term Frequency

| Word     | Sent 1 | Sent 2 | Sent 3 |
| -------- | ------ | ------ | ------ |
| **good** | 1/2    | 1/2    | 1/3    |
| **boy**  | 1/2    | 0      | 1/3    |
| **girl** | 0      | 1/2    | 1/3    |

#### IDF

| Word     | IDF                        |
| -------- | -------------------------- |
| **good** | $$<br>log_c(3/3) = 0<br>$$ |
| **boy**  | $$<br>log_c(3/2)<br>$$     |
| **girl** | $$<br>log_c(3/2)<br>$$     |
*ignore `<br>` tag

#### TF x IDF

These are the final vector or sparse matrix:

|            | f1: good | f2: body         | f3: girl         |
| ---------- | -------- | ---------------- | ---------------- |
| **sent 1** | 0        | (1/2) x log(3/2) | 0                |
| **sent 2** | 0        | 0                | (1/2) x log(3/2) |
| **send 3** | 0        | (1/3) x log(3/2) | (1/3) x log(3/2) |

| **Advantages**                 | **Disadvantages**    |
| ------------------------------ | -------------------- |
| 1. Intutive                    | 1. Sparcity          |
| 2. Word importance is captured | 2. Out of vocabulary |

