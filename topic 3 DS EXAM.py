class RoomBooking:
    def __init__(self, room_number, guest_name, check_in, check_out):
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out
        self.payment_status = "Unpaid"  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def add_booking(self, room_number, guest_name, check_in, check_out):
        
        new_booking = RoomBooking(room_number, guest_name, check_in, check_out)

        
        if not self.head:
            self.head = new_booking
        else:
            
            current = self.head
            while current.next:
                current = current.next
            
            current.next = new_booking

    def display_bookings(self):
        
        current = self.head
        if current is None:
            print("No bookings found.")
        while current:
            print(f"Room: {current.room_number}, Guest: {current.guest_name}, "
                  f"Check-in: {current.check_in}, Check-out: {current.check_out}, "
                  f"Payment Status: {current.payment_status}")
            current = current.next

    def find_booking(self, room_number):
        
        current = self.head
        while current:
            if current.room_number == room_number:
                return current
            current = current.next
        return None  


class Hotel:
    def __init__(self):
        self.booking_list = LinkedList()

    def book_room(self, room_number, guest_name, check_in, check_out):
        
        self.booking_list.add_booking(room_number, guest_name, check_in, check_out)
        print(f"Room {room_number} booked successfully for {guest_name}.")

    def process_payment(self, room_number):
        
        booking = self.booking_list.find_booking(room_number)
        if booking:
            
            print(f"Processing payment for room {room_number}...")
            
            booking.payment_status = "Paid"
            print(f"Payment successful for room {room_number}.")
        else:
            print("Booking not found.")

    def show_bookings(self):
    
        print("Current Bookings:")
        self.booking_list.display_bookings()



hotel = Hotel()


hotel.book_room(101, "Alice", "2025-01-10", "2025-01-15")
hotel.book_room(102, "Bob", "2025-01-12", "2025-01-18")


hotel.show_bookings()


hotel.process_payment(101)


hotel.show_bookings()


hotel.process_payment(103)
