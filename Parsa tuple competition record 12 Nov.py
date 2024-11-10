
"""In your class, there are five groups that participated and won prizes in 
different competitions held at various schools. Your class teacher has asked for your 
help to record all the details. Write a program using Python that stores 
each record as a tuple. The program should ask the user to enter details such 
as group_name, size_of_the_group, date_of_the_competition, venue, and type_of_medal, 
and store each record as a tuple."""

# An empty list called competition_records where we will store 
# all the competition records.
competition_records = []  

# funtion to add a new record
def add_record():
    #ask for details of the competiton
    group_name = input("Enter the group name: ")
    size_of_group = int(input("Enter the size of the group: "))
    date_of_competition = input("Enter the date of the competition: ")
    venue = input("Enter name of venue (school name): ")
    type_of_medal = input("Enter the type of medal (Gold/Silver/Bronze): ")

    # create a tuple with all the details
    record = (group_name, size_of_group, date_of_competition, venue, type_of_medal) 

    # add the record to the list of records
    competition_records.append(record)  

    print("Record added successfully!\n")

#function to display all records
def display_records():
    print("\nCompetition records:")

    if not competition_records:
        print("No records found.")
        return

    # go through each record in a list one by one
    for number in range(len(competition_records)):
        record = competition_records[number]  

        # print details of the current record (Q:line 43??)
        print(f"{number + 1}. Group: {record[0]}, Size: {record[1]}, Date: {record[2]}, Venue: {record[3]}, Medal: {record[4]}")

# mmain loop for interaction
while True:  
    print("Choose an option:")
    print("1 - Add a record")
    print("2 - Display all records")
    print("3 - Exit")

    choice = input("Enter your choice (1/2/3): ")  # Fixed missing closing parenthesis
    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.\n")



