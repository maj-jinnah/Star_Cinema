class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.entry_hall(self)    

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [
            [0 for i in range(self._cols)] for j in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in [show[0] for show in self._show_list]:
            print("Invalid show ID.")
            return

        for row, col in seat_list:
            if row not in self._seats or col < 0 or col >= self._cols or self._seats[row][col] == 1:
                print(f"Invalid seat ({row}, {col}).")
                continue
            self._seats[row][col] = 1
            print(f"Seat ({row}, {col}) booked for show {id}")

    def view_show_list(self):
        print("\nToday's Show List")
        for show in self._show_list:
            print(f"Anime Name: {show[1]}\tShow ID: {show[0]}\tTime: {show[2]}")

    def view_available_seats(self, id):
        if id not in [show[0] for show in self._show_list]:
            print("Invalid show ID.")
            return

        print("Available Seats: ")
        for row in self._seats:
            print(self._seats[row])

    def run_star_cinema(self):
        while True:
            print("\n1. VIEW ALL SHOW TODAY")
            print("2. VIEW AVAILABLE SEATS")
            print("3. BOOK TICKET")
            print("4. EXIT")

            option = int(input("Enter Option: "))

            if option == 1:
                self.view_show_list()
            elif option == 2:
                show_id = input("Please, Enter Show ID: ")
                self.view_available_seats(show_id)
            elif option == 3:
                show_id = input("Please, Enter Show ID: ")
                num_tickets = int(input("Number of Ticket: "))
                seat_list = []
                for i in range(num_tickets):
                    row = int(input("Enter Seat Row: "))
                    col = int(input("Enter Seat Col: "))
                    seat_list.append((row, col))
                self.book_seats(show_id, seat_list)
            elif option == 4:
                break
            else:
                print("Invalid. Please try again.")


cinema_hall101 = Hall(7, 7, 101)

cinema_hall101.entry_show("11", "One Piece", "09/10/2023 2:00 PM")
cinema_hall101.entry_show("22", "Naruto", "09/10/2023 3:00 PM")
cinema_hall101.entry_show("33", "Attack on Titan", "09/10/2023 4:00 PM")
cinema_hall101.entry_show("44", "Jujutsu Kaisen", "09/10/2023 5:00 PM")

cinema_hall101.run_star_cinema()

