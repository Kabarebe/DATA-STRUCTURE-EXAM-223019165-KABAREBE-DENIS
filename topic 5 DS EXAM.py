class RoomBooking:
    def __init__(self, room_number, guest_name, check_in, check_out):
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out
        self.payment_status = "Unpaid"  
        self.next = None  


class SinglyLinkedList:
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
        print(f"Room {room_number} booked successfully for {guest_name}.")

    def remove_booking(self, room_number):
        
        current = self.head
        previous = None

        while current:
            if current.room_number == room_number:
                
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Booking for room {room_number} removed.")
                return
            previous = current
            current = current.next

        print(f"Booking for room {room_number} not found.")

    def process_payment(self, room_number):
        
        current = self.head
        while current:
            if current.room_number == room_number:
                
                print(f"Processing payment for room {room_number}...")
                current.payment_status = "Paid"
                print(f"Payment successful for room {room_number}.")
                return
            current = current.next

        print(f"Booking for room {room_number} not found.")

    def display_bookings(self):
        
        current = self.head
        if not current:
            print("No bookings available.")
            return
        print("Current Room Bookings:")
        while current:
            print(f"Room: {current.room_number}, Guest: {current.guest_name}, "
                  f"Check-in: {current.check_in}, Check-out: {current.check_out}, "
                  f"Payment Status: {current.payment_status}")
            current = current.next


class Hotel:
    def __init__(self):
        self.booking_list = SinglyLinkedList()

    def book_room(self, room_number, guest_name, check_in, check_out):
        
        self.booking_list.add_booking(room_number, guest_name, check_in, check_out)

    def cancel_booking(self, room_number):
        
        self.booking_list.remove_booking(room_number)

    def process_payment(self, room_number):
        
        self.booking_list.process_payment(room_number)

    def show_bookings(self):
        
        self.booking_list.display_bookings()




hotel = Hotel()


hotel.book_room(101, "Alice", "2025-01-10", "2025-01-15")
hotel.book_room(102, "Bob", "2025-01-12", "2025-01-18")
hotel.book_room(103, "Charlie", "2025-01-14", "2025-01-20")


hotel.show_bookings()


hotel.process_payment(101)


hotel.show_bookings()


hotel.cancel_booking(102)


hotel.show_bookings()


hotel.process_payment(104)
