from django.test import TestCase

# Create your tests here.
from .models import Reservation_2
from datetime import datetime

class ReservationTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.reservation = Reservation_2.objects.create(
            first_name = "John", 
            last_name = "McDonald"
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.first_name, str)
        self.assertIsInstance(self.reservation.last_name, int)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.booking_time, datetime)



#class ReservationTestCase(TestCase):
#    def createReservation(self):
#        Reservation.objects.create(name = "John", seat_count = 4, time_entry = "10:10")

#    def test_seat_count(self):
#        self.createReservation()
#        reservation = Reservation.objects.get(name = "John")
#        expected_count = 4
#        actual_count = reservation.seat_count
#        self.assertEqual(expected_count, actual_count)