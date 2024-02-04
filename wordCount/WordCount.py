"""

This program reads a txt file, identifies the different words
showing on it, and then counts how many times a word shows
on the whole text.

"""

import sys
import time
import os


def compute_word_frequency(numbers):
    """
    Function used to calculate the word frequency of a word within a text
    """

    # create dictionary word_freq, this dictionary will store
    # all different words contained within the text.
    word_freq = {}

    for string in numbers:

        # Split the string within the txt file into  dufferent words
        words = string.split()

        # For each word convert it to lowercase and remove puntctiation signs
        for word in words:
            word = word.strip('.,!?').lower()

            # Check if the word is contained within the dictionary
            # and increase its value of count by one
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq



def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """

    try:
        # start processing flag timer
        start_time = time.time()

        # open file as read mode with utf-8 ecncoding
        with open(file_path, 'r', encoding="utf-8") as file:

            # Read the words from the file and convert them to a list
            words = []

            # iterate over the the lines of the file
            for index, line in enumerate(file):
                try:
                    words.append(line.strip())
                except ValueError:
                    print(f"Error: File detected in line {index+1}")

            result_string = "Row Labels	Count\n"
            word_frequency_dict = compute_word_frequency(words)

            # for each word and its count in the dictionary
            # append the results to the "result_string" that will be displayed

            for key, value in word_frequency_dict.items():
                result_string += f"{key}: {value}\n"

            # get the total amount of words within the txt file
            total_sum = sum(word_frequency_dict.values())
            result_string += f"Grand Total {total_sum}"

            #finish timer
            end_time = time.time()
            #calculate processing time
            elapsed_time_ms = (end_time - start_time) * 1000

            print(result_string)
            print("\n")

            execution_time_result = f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
            print(execution_time_result)

            with open("WordCountResults.txt", "w", encoding="utf-8") as file:

                # Print the object to the file using the print function
                print(result_string, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")



if __name__ == "__main__":

    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python WordCount.py <variable>")
        sys.exit(1)

    # Get the variable value from the command line
    variable_value = sys.argv[1]

    # Use variable_value in your script
    print("Input file:", variable_value)

    # Get the current working directory
    current_directory = os.getcwd()

    # Run analysis on txt file provided
    text_file_path = os.path.join(current_directory,variable_value)
    print("Reading data from address: "+text_file_path)
    print_numbers(text_file_path)
