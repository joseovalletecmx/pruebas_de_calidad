
"""

Program to unittests all different classes
within hotels.py scrip

"""
# import libraries

import unittest
import os
import json
from hotels import Hotel, Customer, Reservation


class TestHotel(unittest.TestCase):
    """
    Unittest for Hotel class
    """
    def setUp(self):
        """
        setUp self
        """
        self.hotel = Hotel("Test Hotel", "Test Location", 10)
        self.hotel.create_hotel()

    def tearDown(self):
        """
        Method to delete hotel
        """
        self.hotel.delete_hotel()

    def test_reserve_room(self):
        """
        Test reserve_room method from Hotel calss
        """
        self.hotel.reserve_room(5)
        with open("hotel_Test Hotel", "r", encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(data["hotel_rooms"]["5"], "reserved")

    def test_cancel_reservation(self):
        """
        Test cancel_reservation method from Hotel calss
        """
        self.hotel.reserve_room(3)
        self.hotel.cancel_reservation(3)
        with open("hotel_Test Hotel", "r", encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(data["hotel_rooms"]["3"], "available")

    def test_modify_information(self):
        """
        Test modify_information method from Hotel calss
        """
        self.hotel.modify_information("New Name", "New Location")
        self.assertEqual(self.hotel.name, "New Name")
        self.assertEqual(self.hotel.location, "New Location")

    def test_delete_nonexistent_hotel(self):
        """
        Test delete non existent hotel from Hotel calss
        """
        hotel = Hotel("Nonexistent Hotel", "Nonexistent Location", 5)
        # Deleting a nonexistent hotel should not raise an error
        self.assertFalse(os.path.exists(f"hotel_{hotel.name}"))
        hotel.delete_hotel()  # This should not raise FileNotFoundError


class TestCustomer(unittest.TestCase):
    """
    Unittest for Customer class
    """
    def setUp(self):
        """
        setUp method
        """
        self.customer = Customer("John", "Doe")
        self.customer.create_customer()

    def tearDown(self):
        """
        tearDown method
        """
        self.customer.delete_customer()

    def test_invalid_customer_modification(self):
        """
        Test modification of information for a non-existent customer
        """
        customer = Customer("Nonexistent", "Customer")
        # Attempting to modify information of a non-existent customer
        with self.assertRaises(FileNotFoundError):
            customer.modify_information("New Name", "New Lastname")

    def test_delete_nonexistent_customer(self):
        """
        Test deleting nont existent customer from Customer class
        """
        customer = Customer("Nonexistent", "Customer")
        # Deleting a nonexistent customer should not raise an error
        path_cust = f"cust_{customer.name}_{customer.lastname}"
        self.assertFalse(os.path.exists(path_cust))
        customer.delete_customer()  # This should not raise FileNotFoundError

    def test_modify_information(self):
        """
        Test modify_information method from Customer class
        """
        self.customer.modify_information("Jane", "Doe")
        with open("cust_Jane_Doe", "r", encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(data["customer_name"], "Jane")
            self.assertEqual(data["customer_lastname"], "Doe")


class TestReservation(unittest.TestCase):
    """
    Unittest for Reservation Class"
    """
    def setUp(self):
        """
        setUp method
        """
        self.hotel = Hotel("Test Hotel", "Test Location", 10)
        self.hotel.create_hotel()
        self.reservation = Reservation("John", "Doe", "Test Hotel", 5)

    def tearDown(self):
        """
        tearDown method
        """
        self.hotel.delete_hotel()

    def test_create_reservation(self):
        """
        test create_reservation method from Reservation class
        """
        self.reservation.create_reservation()
        with open("hotel_Test Hotel", "r", encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(data["hotel_rooms"]["5"], "reserved")
            self.assertEqual(self.reservation.status, "Accepted")

    def test_cancel_reservation(self):
        """
        test cancel_reservation method from Reservation class
        """
        self.hotel.reserve_room(5)  # Reserve a room first
        self.reservation.cancel_reservation()
        with open("hotel_Test Hotel", "r", encoding='utf-8') as f:
            data = json.load(f)
            self.assertEqual(data["hotel_rooms"]["5"], "available")
            self.assertEqual(self.reservation.status, "Cancelled")

    def test_save_file(self):
        """
        test save_file method from Reservation class
        """
        # Ensure save_file method creates a file
        self.reservation.save_file()
        name = self.reservation.name
        last_name = self.reservation.last_name
        self.assertTrue(os.path.exists(f"reservation_{name}_{last_name}"))

    def test_create_customer(self):
        """
        test create_customer method from Reservation class
        """
        # Ensure create_customer method creates a customer file
        self.reservation.create_customer()
        name = self.reservation.name
        last_name = self.reservation.last_name
        self.assertTrue(os.path.exists(f"cust_{name}_{last_name}"))

    def test_nonexistent_hotel(self):
        """
        test non existent hotel within Reservation class
        """
        reservation = Reservation("John", "Doe", "Nonexistent Hotel", 5)
        # Creating reservation for a nonexistent hotel should raise an error
        with self.assertRaises(FileNotFoundError):
            reservation.create_reservation()

    def test_reservation_acceptance(self):
        """
        test that reservation status gets updated within class
        """
        self.reservation.create_reservation()
        self.assertEqual(self.reservation.status, "Accepted")

    def test_reservation_cancellation(self):
        """
        test that reservation status gets updated within class
        """
        self.reservation.cancel_reservation()
        self.assertEqual(self.reservation.status, "Cancelled")

    def test_invalid_room_number_reservation(self):
        """
        Test reservation for an invalid room number in Reservation class
        """
        reservation = Reservation("John", "Doe", "Test Hotel", 15)
        # Attempting to reserve a room that doesn't exist should raise an error
        with self.assertRaises(KeyError):
            reservation.create_reservation()


if __name__ == '__main__':
    unittest.main()
