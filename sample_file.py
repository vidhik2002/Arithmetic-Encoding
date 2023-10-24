import random
import string

def generate_sample_text_file(file_name, num_lines, line_length):
    with open(file_name, 'w') as file:
        for _ in range(num_lines):
            line = ''.join(random.choice(string.ascii_letters + ' ') for _ in range(line_length))
            file.write(line + '\n')

if __name__ == '__main__':
    file_name = "sample.txt"  
    num_lines = 10  
    line_length = 50  

    generate_sample_text_file(file_name, num_lines, line_length)
    print(f"Sample text file '{file_name}' has been created.")