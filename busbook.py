class Bus:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_seat(self, num_seats):
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            print(f"Booked {num_seats} seat(s). {self.available_seats} seat(s) remaining.")
        else:
            print("Sorry, there are not enough available seats.")

    def display_available_seats(self):
        print(f"There are {self.available_seats} seat(s) available out of {self.total_seats} total seats.")


def main():
    total_seats = 50  # You can change this to the total number of seats on the bus.
    bus = Bus(total_seats)

    while True:
        print("\n1. Book a seat")
        print("2. Display available seats")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            num_seats = int(input("Enter the number of seats to book: "))
            bus.book_seat(num_seats)
        elif choice == '2':
            bus.display_available_seats()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
