"""

This program reads a file that is assumed to contain only numbers,
then the program reads those numbers and converts them to:

. binary 
. hexadecimal base.

"""

import sys
import time
import os


def compute_decimal_to_binary(number, num_bits=9):
    '''
    Method to convert the input number to binary
    '''

    # if received number == 0 the return 0 as binary representation.
    print(number)
    if number == 0:
        return 0

    # create placeholder for binay representation, this placeholder
    # will appends 0,1's accordingly for binary representation.
    binary_representation = ""

    # get absolute value of the received number
    abs_value = abs(number)

    # for each number divide it by 2 and save the reminder
    # and append it to the binary_reresentation (string)
    # the initial binary_representation will be built accordingly

    for _ in range(num_bits - 1):
        binary_representation = str(abs_value % 2) + binary_representation
        abs_value //= 2

    # if the received number is negative, reverse the order of the representation.
    # once reversed + 1 to the obtained binaary representation.
    # if the received number is positive apply the corresponding logic

    if number < 0:
        inverted_bits = ''.join(['1' if bit == '0' else '0' for bit in binary_representation])
        carry = 1
        result = ""

        for bit in inverted_bits[::-1]:
            current_bit = str((int(bit) + carry) % 2)
            carry = (int(bit) + carry) // 2
            result = current_bit + result

        binary_representation = result
        binary_representation = '1' + binary_representation
        return binary_representation

    for _ in range(num_bits - 1):
        binary_representation = str(abs_value % 2) + binary_representation
        abs_value //= 2            
    return binary_representation

def compute_decimal_to_hexadecimal(decimal_number):
    '''
    Method to convert number to hexadecimal
    '''

    # if the received number is 0 hexadecimal will be calculated as 0
    # if the received number is negative

    decimal_number = int(decimal_number)

    if decimal_number == 0:
        return 0

    if decimal_number < 0:

        # Convert negative numbers to 2's complement hexadecimal representation

        hex_digits = "0123456789ABCDEF"
        hex_value = ""
        # Calculate 2's complements
        decimal_number = (1 << 32) + decimal_number

        # run logic for the updated decimal number where it can now be treated as positive
        while decimal_number > 0:
            remainder = decimal_number % 16
            hex_value = hex_digits[remainder] + hex_value
            decimal_number //= 16

        return hex_value
    # run regular logic if received number is not negative nor 0
    hex_digits = "0123456789ABCDEF"
    hex_value = ""
    while decimal_number > 0:
        remainder = decimal_number % 16
        hex_value = hex_digits[remainder] + hex_value
        decimal_number //= 16

    return hex_value


def print_numbers(file_path):
    """
    Method to print the numbers that the file contains
    """

    try:
        start_time = time.time()
        with open(file_path, 'r', encoding="utf-8") as file:

            # Read the numbers from the file and convert them to a list
            numbers = []

            for line in file:
                numbers.append(line.strip())

            conversion_array = []

            for num in numbers:
                conversion_dictionary = {}

                try:
                    # int_num = int(num)
                    conversion_dictionary['number'] = int(num)
                    binary = compute_decimal_to_binary(int(num))
                    conversion_dictionary['binary'] = binary
                    hexadecimal = compute_decimal_to_hexadecimal(int(num))
                    conversion_dictionary['hex_number'] = hexadecimal
                    conversion_array.append(conversion_dictionary)

                except ValueError:
                    # error_value = "#VALUE!"
                    conversion_dictionary['number'] = num
                    conversion_dictionary['binary'] = "#VALUE!"
                    conversion_dictionary['hex_number'] = "#VALUE!"
                    conversion_array.append(conversion_dictionary)

            result_string = "INDEX		NUMBER	BIN	HEX\n"

            for index, conversion_dictionary in enumerate(conversion_array):

                result_string += (
                    f"{index+1} {conversion_dictionary['number']} "
                    f"{conversion_dictionary['binary']} {conversion_dictionary['hex_number']}\n"
                )

            end_time = time.time()
            elapsed_time_ms = (end_time - start_time) * 1000

            print(result_string)
            print("\n")
            execution_time_result = f"Time of execution: {elapsed_time_ms:.6f} milliseconds"
            print(execution_time_result)

            with open("ConvertionResults.txt", "w", encoding="utf-8") as file:

                # Print the object to the file using the print function

                print(result_string, file=file)
                print("\n", file=file)
                print(execution_time_result, file=file)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


if __name__ == "__main__":

    # Check if a file path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <variable>")
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
