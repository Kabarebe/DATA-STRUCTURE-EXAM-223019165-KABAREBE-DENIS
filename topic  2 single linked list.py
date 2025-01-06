class Room:
    def __init__(self, room_number, room_type, price, availability=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type} - ${self.price} - {'Available' if self.availability else 'Booked'}"

class BookingNode:
    def __init__(self, guest_name, room, payment_status="Pending"):
        self.guest_name = guest_name
        self.room = room
        self.payment_status = payment_status
        self.next = None

    def make_payment(self, amount):
        if amount >= self.room.price:
            self.payment_status = "Paid"
            self.room.availability = False
            return True
        return False

    def __str__(self):
        return f"Booking for {self.guest_name}, Room {self.room.room_number}, Payment Status: {self.payment_status}"

class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookings_head = None  

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, guest_name, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.availability:
                booking_node = BookingNode(guest_name, room)
                if self.bookings_head is None:
                    self.bookings_head = booking_node
                else:
                    current = self.bookings_head
                    while current.next:
                        current = current.next
                    current.next = booking_node
                return booking_node
        return None  # 

    def display_rooms(self):
        for room in self.rooms:
            print(room)

    def display_bookings(self):
        current = self.bookings_head
        while current:
            print(current)
            current = current.next


hotel = Hotel()
hotel.add_room(Room(101, "Single", 100))
hotel.add_room(Room(102, "Double", 150))
hotel.add_room(Room(103, "Suite", 300))

hotel.display_rooms()

booking2 = hotel.book_room("Jane Smith", 102)
if booking2:
    print("Booking Created:", booking2)
    if booking2.make_payment(150):
        print("Payment successful:", booking2)
    else:
        print("Payment failed:", booking2)

hotel.display_bookings()
