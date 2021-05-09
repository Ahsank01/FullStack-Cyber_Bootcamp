#!/usr/bin/env python3

import sys


def decode_message(file_name):
    # Open the file
    with open(file_name, 'r') as f:
        # Read the contents of the file
        contents = f.read()
        # List to contain the words in the decoded message
        decoded_message = list()

        # Split the file content into sentences
        for sentence in contents.split('. '):
            # Split the sentence into individual words
            words = sentence.split(' ')
            # Add the first word from the sentence to the decoded message
            decoded_message.append(words[0])

    return ' '.join(decoded_message)


def main():
    # Get the name of the input file
    file_name = sys.argv[1]

    decoded_message = decode_message(file_name)

    # Print the message with a space between each word
    print(decoded_message)


if __name__ == '__main__':
    main()
