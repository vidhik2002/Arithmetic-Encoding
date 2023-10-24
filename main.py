from collections import Counter
from decimal import Decimal

class ArithmeticEncoder:
    def __init__(self, text):
        self.text = text
        self.total = Decimal(1)
        self.low = Decimal(0)
        self.high = Decimal(1)
        self.cumulative_prob = self.calculate_cumulative_probabilities()

    def calculate_cumulative_probabilities(self):
        freq = dict(Counter(self.text))
        cumulative_prob = {}
        total_chars = len(self.text)

        for char, count in freq.items():
            probability = Decimal(count) / Decimal(total_chars)
            cumulative_prob[char] = probability

        return cumulative_prob

    def encode(self):
        for char in self.text:
            char_prob = self.cumulative_prob[char]
            self.total *= char_prob
            self.high = self.low + (self.high - self.low) * char_prob
            self.low = self.low + (self.high - self.low) * self.cumulative_prob.get(char, 0)  # Use .get() method to handle characters not in cumulative_prob

    def get_encoded_value(self):
        return (self.low + self.high) / 2

def main():
    file_name = input("Enter the name of the text file to encode: ")
    try:
        with open(file_name, 'r') as file:
            text = file.read()

        encoder = ArithmeticEncoder(text)
        encoder.encode()
        encoded_value = encoder.get_encoded_value()

        print(f"Encoded value: {encoded_value}")

    except FileNotFoundError:
        print("File not found!")

if __name__ == '__main__':
    main()
