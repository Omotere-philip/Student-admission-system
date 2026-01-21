admissions = []

def admit_student():
    name = input("Enter student name: ")
    program = input("Enter program: ")
    admissions.append({"name": name, "program": program})
    print("Student admitted successfully")

def view_admissions():
    if not admissions:
        print("No admissions available")
    else:
        for student in admissions:
            print(student["name"], "- Program:", student["program"])

def main():
    while True:
        print("1. Admit Student")
        print("2. View Admissions")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            admit_student()
        elif choice == "2":
            view_admissions()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
