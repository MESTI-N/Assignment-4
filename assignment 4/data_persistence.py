class DataPersistence:
    def save_data(self, data):
        # Save data to a text file
        with open("assignment 4/assignment.txt", "w") as file:
            for item in data:
                file.write(f"{item}\n")

    def load_data(self):
        try:
            # Load data from a text file
            with open("assignment 4/assignment.txt", "r") as file:
                return [eval(line.strip()) for line in file.readlines()]
        except FileNotFoundError:
            # Return an empty list if the file is not found
            return []
