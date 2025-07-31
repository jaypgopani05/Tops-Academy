# Dictionary to store ticket details with ticket ID as key
tickets = {}

# Dictionary to store seat count per route
seat_count = {}

# List of predefined routes with fixed prices
routes = {
    "1": {"route": "Mumbai to Pune", "price": 500},
    "2": {"route": "Delhi to Jaipur", "price": 600},
    "3": {"route": "Bangalore to Hyderabad", "price": 700},
    "4": {"route": "Chennai to Coimbatore", "price": 450}
}

# Maximum number of seats per route
MAX_SEATS = 40

# Function to display available routes
def show_routes():
    print("\nAvailable Routes:")
    for key, value in routes.items():
        print(f"{key}. {value['route']} - ₹{value['price']}")

# Function to generate a unique ticket ID
def generate_ticket_id():
    return f"TKT{1000 + len(tickets) + 1}"

# Function to get the next seat number for a route
def get_next_seat(route):
    if route not in seat_count:
        seat_count[route] = 0
    seat_count[route] += 1
    return seat_count[route]

# Function to check for duplicate booking
def is_duplicate(name, age, mobile, route):
    for ticket in tickets.values():
        if (ticket['name'] == name and
            ticket['age'] == age and
            ticket['mobile'] == mobile and
            ticket['route'] == route):
            return True
    return False

# Function to book a ticket
def book_ticket():
    while True:
        name = input("Enter passenger name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break

    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0 or age > 120:
                print("Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Please enter a numeric value for age.")

    while True:
        mobile = input("Enter 10-digit mobile number: ").strip()
        if not (mobile.isdigit() and len(mobile) == 10):
            print("Mobile number must be 10 digits.")
            continue
        break

    while True:
        show_routes()
        route_choice = input("Select route number: ").strip()
        if route_choice not in routes:
            print("Invalid route selection. Try again.")
            continue
        route = routes[route_choice]['route']
        break

    # Check seat availability
    current_seats = seat_count.get(route, 0)
    if current_seats >= MAX_SEATS:
        print("Sorry, no more seats available for this route.")
        return

    # Check for duplicate booking
    if is_duplicate(name, age, mobile, route):
        print("\nDuplicate booking detected!")
        print("You have already booked the same route.")
        print("1. Book for someone else")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            book_ticket()  # Retry with new details
            return
        else:
            return

    # Assign seat and generate ticket
    seat_number = get_next_seat(route)
    ticket_id = generate_ticket_id()

    # Save ticket details
    tickets[ticket_id] = {
        "name": name,
        "age": age,
        "mobile": mobile,
        "route": route,
        "seat": seat_number
    }

    # Show booking confirmation
    print("\nTicket Booked Successfully!")
    print(f"Ticket ID : {ticket_id}")
    print(f"Name      : {name}")
    print(f"Age       : {age}")
    print(f"Mobile    : {mobile}")
    print(f"Route     : {route}")
    print(f"Seat No   : {seat_number}")
    print(f"Price     : ₹{routes[route_choice]['price']}")

# Function to view all tickets for a given mobile number
def view_ticket():
    mobile = input("Enter your mobile number: ").strip()

    # Validate mobile number
    if not (mobile.isdigit() and len(mobile) == 10):
        print("Invalid mobile number.")
        return

    found = False

    # Search for tickets with the same mobile number
    for ticket_id, ticket in tickets.items():
        if ticket['mobile'] == mobile:
            print("\n--------------------------")
            print(f"Ticket ID : {ticket_id}")
            print(f"Name      : {ticket['name']}")
            print(f"Age       : {ticket['age']}")
            print(f"Route     : {ticket['route']}")
            print(f"Seat No   : {ticket['seat']}")
            print("--------------------------")
            found = True

    if not found:
        print("No tickets found for this number.")

# Function to cancel a ticket using ticket ID
def cancel_ticket():
    ticket_id = input("Enter ticket ID to cancel: ").strip()
    if ticket_id in tickets:
        route = tickets[ticket_id]['route']
        seat_count[route] -= 1  # Decrement seat count
        del tickets[ticket_id]  # Remove ticket
        print("Ticket cancelled successfully.")
    else:
        print("Ticket ID not found.")

# Function to display the main menu
def main_menu():
    while True:
        print("\n===== Bus Ticket Booking System =====")
        print("1. Show Available Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            show_routes()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main menu
main_menu()
