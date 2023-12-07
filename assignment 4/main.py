from user_interaction import UserInteraction
from resource_manager import ResourceManager
from data_persistence import DataPersistence
from resource import Book

with open("assignment 4/assignment.txt", "r") as file:
    user_interaction = UserInteraction()
    resource_manager = ResourceManager()
    data_persistence = DataPersistence()

    resource_manager.books = [Book.from_dict(book) for book in data_persistence.load_data()]

    while True:
        try:
            choice = user_interaction.get_menu_choice()

            if choice == 1:
                resource_manager.create_resource()
            elif choice == 2:
                search_criteria = input("Enter search criteria: ")
                matching_books = resource_manager.search_resources(search_criteria)
                for book in matching_books:
                    print(book)
            elif choice == 3:
                resource_manager.edit_resource()
            elif choice == 4:
                resource_manager.delete_resource()
            elif choice == 5:
                break

        except Exception as e:
            print(f"An error occurred: {e}")

    data_persistence.save_data(resource_manager.get_all_resources())

