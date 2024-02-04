
"""

This program computes descrptive statistics for a given file (txt).
The descriptive statistics that are calculated are the followings:

. mean
. median
. mode
. standard deviation
. variance

"""

# filename: print_numbers.py

import os
import sys
import time

# create all required statistical functions

def compute_mean(numbers):
    """
    This function computes the mean of the elements contained within a class
    """

    return sum(numbers) / len(numbers)


def compute_median(numbers):
    """
    This function computes the median of the elements contained within a class
    """

    sorted_array = sorted(numbers)
    n = len(sorted_array)
    median = None


    # Calculate the index of the middle element
    middle_index = n // 2

    # Check if the list has an odd or even number of elements
    if n % 2 == 0:
        # If even, average the two middle elements
        median = (sorted_array[middle_index - 1] + sorted_array[middle_index]) / 2
    else:
        # If odd, take the middle element
        median = sorted_array[middle_index]

    return median


def compute_mode(numbers):
    """
    Method used to calculate the mode of the elements that the class contains
    """
    # raise "N/A" accordingly
    if not numbers:

        return "N/A"

    # create frequency dictionary
    frequency = {}

    # for each nummber received identify how many times does it appear within the list of numbers
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    # identify the highest frequency within the dictionary
    max_frequency = max(frequency.values())

    # create key key-value pair if the value the key equals the value of the highest frequency
    mode = [key for key, value in frequency.items() if value == max_frequency]

    # return the key (number) that is displayed the most in the list of items received
    return "N/A" if len(mode) == len(frequency.values()) else mode[0]


def compute_standard_deviation(numbers):
    """
    Method used to calculate the standard deviation of the elements that the class contains
    """

    # compute mean
    mean = sum(numbers) / len(numbers)

    # compute squared differences from the mean for each number received within the list
    squared_diff = [(x - mean) ** 2 for x in numbers]

    # compute variance
    variance = sum(squared_diff) / len(numbers)

    # Calculate standard deviation as the square root of the variance
    std_deviation = variance ** 0.5

    return std_deviation


def compute_variance(numbers):
    """
    Method used to calculate the variance of the elements that the class contains
    """
    # compute the number of elements within the list
    n = len(numbers)

    # compute the mean
    mean = sum(numbers) / n

    # compute the sum of squared differences
    sum_squared_diff = sum((x - mean) ** 2 for x in numbers)

    # compute the sample variance
    sample_variance = sum_squared_diff / (n - 2)

    return sample_variance


def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """

    try:
        # start flag for timer
        start_time = time.time()

        # open file from the provided path file and encode as utf-8
        with open(file_path,'r',encoding ="utf-8") as file:
            lines = file.readlines()

        # open the file and store all numbers in a placeholder list
        # if an error is found raise the error describing the line number
        with open(file_path,'r',encoding ="utf-8") as file:
            numbers = []
            for index, line in enumerate(file):
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Error: File contains an error in line {index+1}")

            # store all statistics as string within the variable result
            result = (
                f"Statistics.\nCOUNT: {len(lines)}\nMEAN: {compute_mean(numbers)}\n"
                f"MEDIAN: {compute_median(numbers)}\nMODE: {compute_mode(numbers)}\n"
                f"STD DEV: {compute_standard_deviation(numbers)}\nVAR: {compute_variance(numbers)}"
            )

            #end timer
            end_time = time.time()
            #identify processing time
            elapsed_time_ms = (end_time - start_time) * 1000

            # print result variable where all descriptive statisticas are stores
            print(result)
            print("\n")

            # print executione time
            execution_time_result = f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
            print(execution_time_result)

            with open("StatisticsResults.txt", "w", encoding="utf-8") as file:

                # Print the object to the file using the print function

                print(result, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)

    except FileNotFoundError:

        print(f"Error: File '{file_path}' not found.")


if __name__ == "__main__":

    # Check the input variable of command line arguments
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <variable>")
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
