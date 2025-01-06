class RoomBooking:
    def __init__(self, room_number, guest_name, check_in, check_out):
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out
        self.payment_status = "Unpaid"  

    def process_payment(self):
        
        self.payment_status = "Paid"
        print(f"Payment processed for room {self.room_number}. Status: Paid")

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.booking = None  
        self.next = None  

    def book_room(self, guest_name, check_in, check_out):
        self.booking = RoomBooking(self.room_number, guest_name, check_in, check_out)
        print(f"Room {self.room_number} booked successfully for {guest_name}.")

    def show_booking(self):
        if self.booking:
            print(f"Room: {self.room_number}, Guest: {self.booking.guest_name}, "
                  f"Check-in: {self.booking.check_in}, Check-out: {self.booking.check_out}, "
                  f"Payment Status: {self.booking.payment_status}")
        else:
            print(f"Room {self.room_number} is not booked yet.")

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.rooms = []  

    def add_room(self, room_number):
        room = Room(room_number)
        self.rooms.append(room)

    def show_rooms(self):
        print(f"Floor {self.floor_number}:")
        for room in self.rooms:
            room.show_booking()

class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.floors = {}  

    def add_floor(self, floor_number):
        if floor_number not in self.floors:
            self.floors[floor_number] = Floor(floor_number)
            print(f"Floor {floor_number} added.")
        else:
            print(f"Floor {floor_number} already exists.")

    def add_room(self, floor_number, room_number):
        if floor_number in self.floors:
            self.floors[floor_number].add_room(room_number)
            print(f"Room {room_number} added to Floor {floor_number}.")
        else:
            print(f"Floor {floor_number} does not exist. Please add the floor first.")

    def show_rooms(self):
        print(f"Hotel: {self.hotel_name}")
        for floor in self.floors.values():
            floor.show_rooms()

    def process_payment(self, floor_number, room_number):
        if floor_number in self.floors:
            for room in self.floors[floor_number].rooms:
                if room.room_number == room_number and room.booking:
                    room.booking.process_payment()
                    return
            print(f"Room {room_number} not found on Floor {floor_number} or not booked.")
        else:
            print(f"Floor {floor_number} not found.")




hotel = Hotel("Grand Plaza")


hotel.add_floor(1)
hotel.add_floor(2)


hotel.add_room(1, 101)
hotel.add_room(1, 102)
hotel.add_room(2, 201)
hotel.add_room(2, 202)


hotel.floors[1].rooms[0].book_room("Alice", "2025-01-10", "2025-01-15")
hotel.floors[1].rooms[1].book_room("Bob", "2025-01-12", "2025-01-18")
hotel.floors[2].rooms[0].book_room("Charlie", "2025-01-14", "2025-01-20")


hotel.show_rooms()


hotel.process_payment(1, 101)


hotel.show_rooms()


hotel.process_payment(1, 103)
