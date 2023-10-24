# Arithmetic-Encoding

This repository contains two Python scripts:

1. `arithmetic_coding.py`: A simple implementation of arithmetic coding for encoding text files.
2. `generate_sample_text.py`: A script to generate a sample text file for use with the arithmetic coding script.

## `script.py`

### Description

The `script.py` script generates a sample script of the name `sample.txt`
### Usage
1. Run the script.

### Example

```bash
$ python3 script.py
```

## `main.py`

### Description

1. The `main.py` script provides a basic implementation of arithmetic coding. It reads a text file and encodes it using arithmetic coding.
The script defines a class called ArithmeticEncoder that handles the encoding process. It contains the following methods and attributes:

2. __init__(self, text): The constructor of the ArithmeticEncoder class takes a text input and initializes the total, low, and high values, along with calculating the cumulative_prob dictionary.

3. calculate_cumulative_probabilities(self): This method calculates the cumulative probabilities for each character in the input text. It uses the Counter class to count the frequency of characters and then computes the probabilities.

4. encode(self): The encode method is responsible for performing the actual arithmetic encoding. It iterates through the input text, updating total, low, and high based on the cumulative probabilities of each character.

5. get_encoded_value(self): This method calculates the final encoded value using the low and high values and returns it.

### Usage

To encode a text file using the script, follow these steps:

1. Run the script.
2. You will be prompted to enter the name of the text file you want to encode.
3. The script will encode the text file and display the encoded value.

### Example

```bash
$ python3 main.py
Enter the name of the text file to encode: sample.txt
Encoded value: [encoded value here]
