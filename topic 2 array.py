class Room:
    def __init__(self, room_number, room_type, price, availability=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type} - ${self.price} - {'Available' if self.availability else 'Booked'}"

class Booking:
    def __init__(self, guest_name, room, payment_status="Pending"):
        self.guest_name = guest_name
        self.room = room
        self.payment_status = payment_status

    def make_payment(self, amount):
        if amount >= self.room.price:
            self.payment_status = "Paid"
            self.room.availability = False
            return True
        return False

    def __str__(self):
        return f"Booking for {self.guest_name}, Room {self.room.room_number}, Payment Status: {self.payment_status}"

class Hotel:
    def __init__(self, num_rooms):
        self.rooms = [None] * num_rooms
        self.bookings = []

    def add_room(self, room, index):
        if index < len(self.rooms):
            self.rooms[index] = room
        else:
            print("Index out of bounds.")

    def book_room(self, guest_name, room_number):
        for room in self.rooms:
            if room and room.room_number == room_number and room.availability:
                booking = Booking(guest_name, room)
                self.bookings.append(booking)
                return booking
        return None  

    def display_rooms(self):
        for room in self.rooms:
            if room:
                print(room)

    def display_bookings(self):
        for booking in self.bookings:
            print(booking)


hotel = Hotel(5)
hotel.add_room(Room(101, "Single", 100), 0)
hotel.add_room(Room(102, "Double", 150), 1)
hotel.add_room(Room(103, "Suite", 300), 2)

hotel.display_rooms()

booking1 = hotel.book_room("John Doe", 101)
if booking1:
    print("Booking Created:", booking1)
    if booking1.make_payment(100):
        print("Payment successful:", booking1)
    else:
        print("Payment failed:", booking1)

hotel.display_bookings()
