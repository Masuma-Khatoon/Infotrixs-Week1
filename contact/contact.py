import re

filename = "contact_data.csv"

class ContactSystem:
    def __init__(self, user_id=0, name='', mobile_no=0):
        self.user_id = user_id
        self.name = name
        self.mobile_no = mobile_no

    def load_contacts(self):
        try:
            with open(filename, 'r') as f:
                main_data = f.read().split('\n')
                main_data = list(filter(None, main_data))
            return main_data
        except FileNotFoundError:
            return []

    def write_file(self, list_data):
        try:
            with open(filename, "w") as f:
                all_data = '\n'.join(list_data)
                f.write(all_data)
            return True
        except IOError:
            print("An error occurred while writing to the file.")
            return False

    def show_contact(self):
        main_data = self.load_contacts()
        if not main_data:
            print("Contact list is empty.")
        else:
            for data in main_data:
                split_data = data.split(',')
                print("User ID:", split_data[0])
                print("Name:", split_data[1])
                print("Mobile_no:", split_data[2])
                print()

    def add_contact(self):
        user_id = input("Create User ID: ")
        name = input("Enter Name: ")
        mobile_no = input("Enter Mobile_no: ")
        data = f"{user_id},{name},{mobile_no}"
        main_data = self.load_contacts()
        main_data.append(data)
        if self.write_file(main_data):
            print("Contact added successfully.")
        else:
            print("Failed to add contact.")

    def edit_contact(self, no):
        main_data = self.load_contacts()
        for i, data in enumerate(main_data):
            split_data = data.split(',')
            if no == split_data[0]:
                name = input("Enter Name: ")
                mobile_no = input("Enter Mobile_no: ")
                new_value = f"{no},{name},{mobile_no}"
                main_data[i] = new_value
                if self.write_file(main_data):
                    print("Successfully updated.")
                else:
                    print("Failed to update contact.")
                return
        print("User ID not found.")

    def remove_contact(self, no):
        main_data = self.load_contacts()
        for data in main_data:
            split_data = data.split(',')
            if no == split_data[0]:
                main_data.remove(data)
                if self.write_file(main_data):
                    print("Successfully deleted contact.")
                else:
                    print("Failed to delete contact.")
                return
        print("User ID not found.")

    def search_id(self, no):
        main_data = self.load_contacts()
        for data in main_data:
            split_data = data.split(',')
            if no == split_data[0]:
                return True
        return False

class Main:
    @staticmethod
    def menu():
        my_class = ContactSystem()
        while True:
            print("\nCREATE/ADD CONTACT\n"
                  "1. Contact List\n"
                  "2. Add Contact\n"
                  "3. Update Contact\n"
                  "4. Remove Contact\n"
                  "5. Exit\n")

            try:
                user_input = int(input("Please enter an option from above (1-5): "))
            except ValueError:
                print("Enter a valid option.")
                continue

            print()

            if user_input == 1:
                my_class.show_contact()
            elif user_input == 2:
                my_class.add_contact()
            elif user_input == 3:
                num = input("Enter User ID for edit: ")
                if my_class.search_id(num):
                    my_class.edit_contact(num)
                else:
                    print("Incorrect User ID!")
            elif user_input == 4:
                num1 = input("Enter User ID for delete: ")
                if my_class.search_id(num1):
                    my_class.remove_contact(num1)
                else:
                    print("Incorrect User ID!")
            elif user_input == 5:
                print("DONE")
                break
            else:
                print("Invalid Input!")

if __name__ == "__main__":
    Main.menu()
