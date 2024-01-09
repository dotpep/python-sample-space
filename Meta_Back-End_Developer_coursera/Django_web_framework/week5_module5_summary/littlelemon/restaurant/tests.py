from django.test import TestCase
from .models import Booking, Menu

class BookingTestCase(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            first_name="John",
            last_name="Doe",
            guest_number=2,
            comment="I want more Cheese in my Pizza"
        )
    
    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John Doe")
        
    def test_booking_fields(self):
        self.assertEqual(self.booking.first_name, "John")
        self.assertEqual(self.booking.last_name, "Doe")
        self.assertEqual(self.booking.guest_number, 2)
        self.assertEqual(self.booking.comment, "I want more Cheese in my Pizza")
        
class MenuTestCase(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            name="Pizza",
            price=10,
            description="Cheese and tomato"
        )
        
    def test_menu_str(self):
        self.assertEqual(str(self.menu), "Pizza")
        
    def test_menu_fields(self):
        self.assertEqual(self.menu.name, "Pizza")
        self.assertEqual(self.menu.price, 10)
        self.assertEqual(self.menu.description, "Cheese and tomato")
