class RoomBooking:
    def __init__(self, room_number, guest_name, check_in, check_out):
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out
        self.payment_status = "Unpaid"  
        

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, booking):
        if self.is_full():
            print("Queue is full. Replacing the oldest booking...")
            self.dequeue()  

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = booking
        print(f"Booking for room {booking.room_number} added.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No booking to remove.")
            return None

        removed_booking = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  
        else:
            self.front = (self.front + 1) % self.size
        
        return removed_booking

    def display(self):
        if self.is_empty():
            print("No bookings available.")
            return

        print("Current Room Bookings:")
        i = self.front
        while i != self.rear:
            booking = self.queue[i]
            print(f"Room: {booking.room_number}, Guest: {booking.guest_name}, "
                  f"Check-in: {booking.check_in}, Check-out: {booking.check_out}, "
                  f"Payment Status: {booking.payment_status}")
            i = (i + 1) % self.size
        
        booking = self.queue[self.rear]
        print(f"Room: {booking.room_number}, Guest: {booking.guest_name}, "
              f"Check-in: {booking.check_in}, Check-out: {booking.check_out}, "
              f"Payment Status: {booking.payment_status}")


class Hotel:
    def __init__(self, queue_size):
        self.booking_queue = CircularQueue(queue_size)

    def book_room(self, room_number, guest_name, check_in, check_out):
        new_booking = RoomBooking(room_number, guest_name, check_in, check_out)
        self.booking_queue.enqueue(new_booking)

    def process_payment(self, room_number):
        for booking in self.booking_queue.queue:
            if booking and booking.room_number == room_number:
                print(f"Processing payment for room {room_number}...")
                booking.payment_status = "Paid"
                print(f"Payment successful for room {room_number}.")
                return

        print(f"Booking for room {room_number} not found.")

    def show_bookings(self):
        self.booking_queue.display()



hotel = Hotel(queue_size=3)


hotel.book_room(101, "Alice", "2025-01-10", "2025-01-15")
hotel.book_room(102, "Bob", "2025-01-12", "2025-01-18")
hotel.book_room(103, "Charlie", "2025-01-14", "2025-01-20")


hotel.show_bookings()


hotel.book_room(104, "David", "2025-01-15", "2025-01-25")


hotel.show_bookings()


hotel.process_payment(102)


hotel.show_bookings()


hotel.process_payment(105)
