
# dentro de este script se señalan las 5 pruebas negativas realizadas

"""
    def test_delete_nonexistent_hotel(self):
        """
        Test delete non existent hotel from Hotel calss
        """
        hotel = Hotel("Nonexistent Hotel", "Nonexistent Location", 5)
        # Deleting a nonexistent hotel should not raise an error
        self.assertFalse(os.path.exists(f"hotel_{hotel.name}"))
        hotel.delete_hotel()  # This should not raise FileNotFoundError


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

    def test_nonexistent_hotel(self):
        """
        test non existent hotel within Reservation class
        """
        reservation = Reservation("John", "Doe", "Nonexistent Hotel", 5)
        # Creating reservation for a nonexistent hotel should raise an error
        with self.assertRaises(FileNotFoundError):
            reservation.create_reservation()

    def test_invalid_room_number_reservation(self):
        """
        Test reservation for an invalid room number in Reservation class
        """
        reservation = Reservation("John", "Doe", "Test Hotel", 15)
        # Attempting to reserve a room that doesn't exist should raise an error
        with self.assertRaises(KeyError):
            reservation.create_reservation()

"""