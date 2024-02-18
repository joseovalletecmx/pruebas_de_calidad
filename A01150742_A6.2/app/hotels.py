
"""

This program is aimed at running unitary tests for
different classes. Three different classes are being created:

*hotel
*reservations
*customers

Each class will have different methods:

    1. Hotels
        a. Create Hotel - checked
        b. Delete Hotel - checked
        c. Display Hotel information - checked
        d. Modify Hotel Information - checked
        e. Reserve a Room - checked
        f. Cancel a Reservation - checked
    2. Customer
        a. Create Customer - checked
        b. Delete a Customer - checked
        c. Display Customer Information - checked
        d. Modify Customer Information - checked

    3. Reservation
        a. Create a Reservation (Customer,Hotel)
        b. Cancel a Reservation

Instances from these classes are created and then saved
as individual jsonfiles as proof of how they are used

The unitarty tests are also deployed for the different methods

Steps homework:

1. Create all classes
2. Learn how to used them and create the json files
3. Unittest the results
4. Learn how to run summary for each test (whatsapp file)
5. pylint / flake8

"""

# import libraries

import json
import os


class Hotel:
    """
    create Hotel to class to instantiate hotel objects
    objects will have the following properties:

    *name
    *location
    *amount of total rooms

    """
    def __init__(self, name, location, rooms):
        """
        init / constructor method for the hotels
        """
        self.name = name
        self.location = location
        self.rooms = {val: "available" for val in list(range(1, rooms + 1))}

    def create_hotel(self):
        """
        Saves hotel data to a file.
        """
        data = {
            'hotel_name': self.name,
            'hotel_location': self.location,
            'hotel_rooms': self.rooms
        }
        current_directory = os.getcwd()
        hotel_name = "hotel_"+self.name
        hotel_file = os.path.join(current_directory, hotel_name)

        with open(hotel_file, "w", encoding='utf-8') as f:
            json.dump(data, f)

    def delete_hotel(self):
        """
        Deletes hotels data file within directory as well as instance
        """
        try:
            current_directory = os.getcwd()
            hotel_name = "hotel_"+self.name
            hotel_file = os.path.join(current_directory, hotel_name)

            if os.path.exists(hotel_file):
                os.remove(hotel_file)
                print(f"File '{hotel_file}' has been removed.")
            else:
                print(f"File '{hotel_file}' does not exist.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def update_data(self):
        """
        update method for customer reservation functionality
        """
        try:
            data = {
                'hotel_name': self.name,
                'hotel_location': self.location,
                'hotel_rooms': self.rooms
            }
            current_directory = os.getcwd()
            hotel_name = "hotel_"+self.name
            hotel_file = os.path.join(current_directory, hotel_name)

            with open(hotel_file, "w", encoding='utf-8') as f:
                json.dump(data, f)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def display_information(self):
        """
        Returns hotel information as a string
        """
        print(f"Name:{self.name},Location:{self.location},Rooms:{self.rooms}")

    def modify_information(self, new_name, new_location):
        """
        Saves hotel data to a file
        """
        new_data = {
            'name': new_name,
            'location': new_location,
            'rooms': self.rooms
        }

        try:
            # open previous files with self.name (previous name)
            current_directory = os.getcwd()
            hotel_name = "hotel_"+new_name
            hotel_file = os.path.join(current_directory, hotel_name)

            # update_data for new name and new_location
            with open(hotel_file, "w", encoding='utf-8') as f:
                json.dump(new_data, f)

            # eliminar archivo previo
            self.delete_hotel()

            # update name and location
            self.name = new_name
            self.location = new_location

        except FileNotFoundError as e:
            print(f"Error: {e}")
        return f"Name: {self.name},Location:{self.location},Rooms:{self.rooms}"

    def reserve_room(self, room_number):
        """
        Reserve a room by updating its availability status
        """
        # room_number = str(room_number)
        try:
            if room_number in self.rooms:
                if self.rooms[room_number] == "available":
                    self.rooms[room_number] = "reserved"
                    print(f"Room {room_number} has been reserved.")
                else:
                    print(f"Room {room_number} is already reserved.")
            else:
                print(f"Room {room_number} does not exist in the hotel.")

            # update_room_availability
            self.update_data()
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def cancel_reservation(self, room_number):
        """
        Cancel reservation for a room by updating its availability status
        """
        try:
            if room_number in self.rooms:
                if self.rooms[room_number] == "reserved":
                    self.rooms[room_number] = "available"
                    print("Reservation for Room has been cancelled")
                else:
                    print(f"Room {room_number} is not reserved.")
            else:
                print(f"Room {room_number} does not exist in the hotel.")

            # update_room_availability
            self.update_data()
        except FileNotFoundError as e:
            print(f"Error: {e}")


class Customer:
    """
    create Customer class

    """
    def __init__(self, name, lastname):
        """
        init / constructor method for the hotels
        """
        self.name = name
        self.lastname = lastname

    def create_customer(self):
        """
        Saves hotel data to a file.
        """
        data = {
            'customer_name': self.name,
            'customer_lastname': self.lastname
        }
        try:
            current_directory = os.getcwd()
            customer_name = "cust_"+self.name+"_"+self.lastname
            cust_file = os.path.join(current_directory, customer_name)

            with open(cust_file, "w", encoding='utf-8') as f:
                json.dump(data, f)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def delete_customer(self):
        """
        Deletes hotels data file within directory as well as instance
        """
        try:
            current_directory = os.getcwd()
            customer_name = "cust_"+self.name+"_"+self.lastname
            cust_file = os.path.join(current_directory, customer_name)

            if os.path.exists(cust_file):
                os.remove(cust_file)
                print(f"File '{cust_file}' has been removed.")
            else:
                print(f"File '{cust_file}' does not exist.")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def display_information(self):
        """
        Returns hotel information as a string
        """
        print(f"Name:{self.name},Last Name:{self.lastname}")

    def modify_information(self, new_name, new_lastname):
        """
        Saves hotel data to a file
        """
        new_data = {
            'customer_name': new_name,
            'customer_lastname': new_lastname,
        }

        # open previous files with self.name (previous name)
        current_directory = os.getcwd()
        customer_name = "cust_"+self.name+"_"+self.lastname
        cust_file = os.path.join(current_directory, customer_name)

        if os.path.exists(cust_file):
            # update_date
            with open(cust_file, "w", encoding='utf-8') as f:
                json.dump(new_data, f)

            # eliminar archivo previo
            self.delete_customer()

            # update name and location
            self.name = new_name
            self.lastname = new_lastname
            self.create_customer()
        else:
            raise FileNotFoundError("Customer file does not exist.")

        return f"Name: {self.name},Last Name:{self.lastname}"


class Reservation:
    """
    Class reservations
    """
    def __init__(self, name, last_name, hotel, room_number):
        self.name = name
        self.last_name = last_name
        self.hotel = hotel
        self.room_number = room_number
        self.status = "Received"

    def save_file(self):
        """
        Save reservation data to directory
        """
        data = {
            'name': self.name,
            'last_name': self.last_name,
            'hotel': self.hotel,
            'room_number': self.room_number,
            'status': self.status
        }
        try:
            current_directory = os.getcwd()
            file_name = f"reservation_{self.name}_{self.last_name}"
            file_path = os.path.join(current_directory, file_name)

            with open(file_path, "w", encoding='utf-8') as f:
                json.dump(data, f)

            print(f"Reservation details saved to {file_path}")
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def create_customer(self):
        """
        create customer based on Customer class
        """
        customer = Customer(self.name, self.last_name)
        customer.create_customer()

    def create_reservation(self):
        """
        Reserve a room by updating its status in the hotel's data file
        """
        # Load hotel data

        current_directory = os.getcwd()
        hotel_file = os.path.join(current_directory, f"hotel_{self.hotel}")

        if os.path.exists(hotel_file):
            with open(hotel_file, "r", encoding='utf-8') as f:
                hotel_data = json.load(f)
                hotel_rooms = hotel_data.get("hotel_rooms", {})

                # Check if room number exists
                if str(self.room_number) in hotel_rooms:
                    if hotel_rooms[str(self.room_number)] == "available":
                        # Update room status to reserved
                        hotel_rooms[str(self.room_number)] = "reserved"

                        # Save updated data back to the file
                        hotel_data["hotel_rooms"] = hotel_rooms
                        with open(hotel_file, "w", encoding='utf-8') as f:
                            json.dump(hotel_data, f)

                        print(f"Room {self.room_number} has been reserved")
                    else:
                        print(f"Room {self.room_number} already reserved.")
                else:
                    print(f"Room {self.room_number} does not exist.")
                    raise KeyError(f"Room {self.room_number} does not exist.")
        else:
            print(f"Hotel {self.hotel} data file does not exist.")
            raise FileNotFoundError(f"Hotel {self.hotel} file does not exist.")
        self.status = 'Accepted'

    def cancel_reservation(self):
        """
        Cancel a reservation by updating room status back to available
        """
        # Load hotel data
        current_directory = os.getcwd()
        hotel_file = os.path.join(current_directory, f"hotel_{self.hotel}")

        if os.path.exists(hotel_file):
            with open(hotel_file, "r", encoding='utf-8') as f:
                hotel_data = json.load(f)
                hotel_rooms = hotel_data.get("hotel_rooms", {})

                # Check if room number exists
                if str(self.room_number) in hotel_rooms:
                    if hotel_rooms[str(self.room_number)] == "reserved":
                        # Update room status to available
                        hotel_rooms[str(self.room_number)] = "available"

                        # Save updated data back to the file
                        hotel_data["hotel_rooms"] = hotel_rooms
                        with open(hotel_file, "w", encoding='utf-8') as f:
                            json.dump(hotel_data, f)

                        print("Reservation has been cancelled.")
                    else:
                        hotel_rooms[str(self.room_number)] = "available"
                        print(f"Room {self.room_number} is not reserved.")
                else:
                    print(f"Room {self.room_number} does not exist.")
                    raise KeyError(f"Room {self.room_number} does not exist.")
        else:
            print(f"Hotel {self.hotel} data file does not exist.")
            raise FileNotFoundError(f"Hotel {self.hotel} file does not exist.")
        self.status = 'Cancelled'


mi_hotel = Hotel("la_cabanita", "slp", 5)
mi_hotel.create_hotel()

mi_reservacion = Reservation("jose", "ovalle", "la_cabanita", "5")
mi_reservacion.save_file()
mi_reservacion.create_customer()
mi_reservacion.create_reservation()
print(mi_reservacion.status)
mi_reservacion.cancel_reservation()
print(mi_reservacion.status)
