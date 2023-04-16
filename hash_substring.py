import os
import sys

def obtain_input():
    input_type = input().strip().upper()
    if input_type == "I":
        pattern = input().strip()
        text = input().strip()
    elif input_type == "F":
        file_path = 'tests/06'
        try:
            with open(file_path) as file:
                pattern = file.readline().strip()
                text = file.readline().strip()
        except FileNotFoundError:
            print("Error: file not found")
            sys.exit(1)
        except Exception as e:
            print("Error:", e)
            sys.exit(1)
    else:
        print("Error: invalid input choice")
        sys.exit(1)
    return input_type, pattern, text

def display_occurrences(output):
    print(' '.join(map(str, output)))

def find_occurrences(input_type, pattern, text):
    text_length = len(text)
    pattern_length = len(pattern)
    prime = 31
    prime_powers = [pow(prime, i) for i in range(pattern_length)]
    pattern_hash = sum([ord(pattern[i]) * prime_powers[pattern_length - 1 - i] for i in range(pattern_length)])
    text_hash = sum([ord(text[i]) * prime_powers[pattern_length - 1 - i] for i in range(pattern_length)])
    found_matches = []

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i + pattern_length]:
                found_matches.append(i)
        if i < text_length - pattern_length:
            text_hash = (text_hash - ord(text[i]) * prime_powers[pattern_length - 1]) * prime + ord(text[i + pattern_length])

    return found_matches

if __name__ == '__main__':
    display_occurrences(find_occurrences(*obtain_input()))
