class UserInteraction:
    def get_menu_choice(self):
        print("1. Create\n2. Read (Search)\n3. Edit\n4. Delete\n5. Quit")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def handle_exceptions(self):
        try:
            raise ValueError("This is a sample exception in the UI module")
        except ValueError as ve:
            print(f"Error: {ve}")
