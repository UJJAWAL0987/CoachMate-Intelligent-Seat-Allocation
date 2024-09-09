class TrainCoach:
    def __init__(self):
        # Initialize the seating arrangement: 10 rows of 7 seats and 1 row of 3 seats
        self.seats = [[0] * 7 for _ in range(10)] + [[0] * 3]
        self.total_seats = 80
        self.booked_seats = 0
        self.seat_map = self.generate_seat_map()

    def generate_seat_map(self):
        """Generate a seat map with human-readable seat numbers."""
        seat_map = []
        seat_number = 1
        for row in range(len(self.seats)):
            seat_map.append([seat_number + i for i in range(len(self.seats[row]))])
            seat_number += len(self.seats[row])
        return seat_map

    def display_seats(self):
        """Display the current seating arrangement with color-coded availability."""
        print("\nCurrent Seat Availability (🟢 = Available, 🔴 = Booked):")
        for i, row in enumerate(self.seats):
            display_row = ["🟢" if seat == 0 else "🔴" for seat in row]  # 🟢 = Available, 🔴 = Booked
            print(f"Row {i + 1}: {display_row}")
        print("\n")

    def find_consecutive_seats(self, seats_needed):
        """Find consecutive available seats in the same row."""
        for i, row in enumerate(self.seats):
            consecutive_seats = 0
            temp_seats = []
            for j, seat in enumerate(row):
                if seat == 0:
                    consecutive_seats += 1
                    temp_seats.append((i, j))
                    if consecutive_seats == seats_needed:
                        return temp_seats
                else:
                    consecutive_seats = 0
                    temp_seats = []
        return None

    def find_nearby_seats(self, seats_needed):
        """Find nearby available seats if consecutive seats are not available."""
        booked_seats = []
        for i, row in enumerate(self.seats):
            for j, seat in enumerate(row):
                if seat == 0:
                    booked_seats.append((i, j))
                    if len(booked_seats) == seats_needed:
                        return booked_seats
        return booked_seats

    def book_seats(self, seats_needed):
        """Book the required number of seats."""
        if seats_needed > (self.total_seats - self.booked_seats):
            print(f"Sorry, only {self.total_seats - self.booked_seats} seats are available.")
            return

        # First try to book consecutive seats
        seats_to_book = self.find_consecutive_seats(seats_needed)
        # If consecutive seats are not available, book nearby seats
        if not seats_to_book:
            seats_to_book = self.find_nearby_seats(seats_needed)

        # Mark seats as booked
        for row, col in seats_to_book:
            self.seats[row][col] = 1

        # Update booked seat count
        self.booked_seats += seats_needed

        # Convert seat positions to human-readable seat numbers
        booked_seat_numbers = [self.seat_map[row][col] for row, col in seats_to_book]

        # Output the result
        print(f"\nSuccessfully booked seats: {booked_seat_numbers}")
        self.display_seats()

    def start_booking(self):
        """Initiate seat booking process until the coach is fully booked."""
        while self.booked_seats < self.total_seats:
            try:
                seats_needed = int(input("Enter the number of seats you want to book (1-7): "))
                if seats_needed < 1 or seats_needed > 7:
                    print("Invalid input. You can only book between 1 and 7 seats.")
                    continue
                self.book_seats(seats_needed)
            except ValueError:
                print("Please enter a valid number.")
                continue


# Create an instance of the TrainCoach
train_coach = TrainCoach()
train_coach.display_seats()

# Start the booking process
train_coach.start_booking()
