"""

This program receives two json files as input, one with a price catalog
and one with sales record for different items. The program calculates
the total sales amount by multyipling price * quantity, this calculation
is performed for all items and then total sales amount is printed out
as the final outpu.

"""

import os
import sys
import json
import time


def load_json(file):
    """
    load json file function to to create a sales dictionary and
    and product list dictionary
    """

    # define current directory
    current_directory = os.getcwd()

    # append file's name to current_directory as string for reading
    file_path = os.path.join(current_directory, file)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


def compute_total_sales(catalog_file, transactions_file):
    """
    compute total sales for each item accordingly and then calculate
    the totales sales amount of all items
    """

    try:
        # Start the timer for the whole calculation
        start_time = time.time()
        # Load product catalog
        catalog = load_json(catalog_file)
        if catalog is None:
            return None
        # Create a dictionary to map product titles to their prices
        prices = {product['title']: product['price'] for product in catalog}

        # Load product transactions
        transactions = load_json(transactions_file)
        if transactions is None:
            return None

        # set total sales amount initial value
        total_sales = 0

        # for every transaction get its product and its quantity
        for transaction in transactions:

            product = transaction.get('Product')
            quantity = transaction.get('Quantity')

            if product is None or quantity is None:
                print(f"Error: Missing data in transaction: {transaction}")
                continue
            if product in prices:
                total_sales = total_sales + quantity * prices[product]
                total_sales = round(total_sales, 2)
            else:
                print(f"Product '{product}' not found in the catalog.")
                print("")

        # once calculation is finished end the timer
        end_time = time.time()

        # calculate the elapsed time
        elapsed_time = end_time - start_time

        # Write total sales to a text file
        with open('sales_results.txt', 'w', encoding='utf-8') as f:
            f.write(f"Total Sales: {total_sales}\n")
            f.write(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

        print(f"Total sales: {total_sales:.4f}\n")
        print(f"Elapsed Time: {elapsed_time:.4f} seconds\n")

        return total_sales

    except NameError as error:
        print(f"An error occurred: {error}")
        return None


# Run file accordingly from terminal
if __name__ == "__main__":

    # Check the input variables of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python computesales.py <variable1><variable2")
        sys.exit(1)

    # Get the variable value from the command line
    productlist = sys.argv[1]
    salesrecords = sys.argv[2]

    # input files print
    print("")
    print("Input file 1: "+productlist)
    print("Input file 2: "+salesrecords)
    print("")

    # Use variable_value in your script
    print("Reading productlist file:", os.path.join(os.getcwd(), productlist))
    print("Reading records file:", os.path.join(os.getcwd(), salesrecords))
    print("")

    try:
        compute_total_sales(productlist, salesrecords)
    except NameError as e:
        print(f"An error occurred: {e}")
