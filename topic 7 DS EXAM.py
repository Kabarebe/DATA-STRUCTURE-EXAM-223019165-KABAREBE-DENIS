from datetime import datetime

class RoomBooking:
    def __init__(self, room_number, guest_name, check_in, check_out, payment_status):
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = datetime.strptime(check_in, "%Y-%m-%d")  
        self.check_out = datetime.strptime(check_out, "%Y-%m-%d")
        self.payment_status = payment_status  

    def __repr__(self):
        return (f"Room {self.room_number}: {self.guest_name}, "
                f"Check-in: {self.check_in.date()}, Check-out: {self.check_out.date()}, "
                f"Payment Status: {self.payment_status}")


def insertion_sort(bookings):
    for i in range(1, len(bookings)):
        key = bookings[i]
        j = i - 1

        
        
    
        while j >= 0 and (bookings[j].payment_status == "Unpaid" and key.payment_status == "Paid" or 
                          (bookings[j].payment_status == key.payment_status and bookings[j].check_in > key.check_in)):
            bookings[j + 1] = bookings[j]
            j -= 1
        bookings[j + 1] = key


if __name__ == "__main__":
    
    bookings = [
        RoomBooking(101, "Alice", "2025-01-10", "2025-01-15", "Unpaid"),
        RoomBooking(102, "Bob", "2025-01-12", "2025-01-18", "Paid"),
        RoomBooking(103, "Charlie", "2025-01-14", "2025-01-20", "Unpaid"),
        RoomBooking(104, "David", "2025-01-08", "2025-01-12", "Paid"),
        RoomBooking(105, "Eva", "2025-01-09", "2025-01-14", "Paid")
    ]

    
    print("Bookings before sorting:")
    for booking in bookings:
        print(booking)

    
    insertion_sort(bookings)

    
    print("\nBookings after sorting based on priority (Payment status and Check-in date):")
    for booking in bookings:
        print(booking)
