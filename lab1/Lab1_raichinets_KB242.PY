

students = [
    {"name": "Bob",  "phone": "0631234567", "email": "bob@mail.com",  "group": "KB-242-1"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@mail.com", "group": "KB-242-1"},
    {"name": "Jon",  "phone": "0631234567", "email": "jon@mail.com",  "group": "KB-242-2"},
    {"name": "Zak",  "phone": "0631234567", "email": "zak@mail.com",  "group": "KB-242-2"}
]


def printAllList():
    """Вивід усього списку студентів"""
    if not students:
        print("Список порожній\n")
        return
    for elem in students:
        print(
            f"Name: {elem['name']}, "
            f"Phone: {elem['phone']}, "
            f"Email: {elem['email']}, "
            f"Group: {elem['group']}"
        )
    print()


def addNewElement():
    """Додавання нового студента з урахуванням сортування за ім’ям"""
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    group = input("Enter student group: ")

    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added\n")


def deleteElement():
    """Видалення студента за ім’ям"""
    name = input("Enter name to delete: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print(" Element was not found\n")
    else:
        del students[deletePosition]
        print(" Element has been deleted\n")


def updateElement():
    """Оновлення даних студента"""
    name = input("Enter student name to update: ")
    found = None
    for item in students:
        if item["name"] == name:
            found = item
            break

    if not found:
        print(" Student not found\n")
        return

    print("Leave field empty if you don't want to change it")
    new_name = input(f"New name ({found['name']}): ") or found['name']
    new_phone = input(f"New phone ({found['phone']}): ") or found['phone']
    new_email = input(f"New email ({found['email']}): ") or found['email']
    new_group = input(f"New group ({found['group']}): ") or found['group']

    # Видяємо старі
    students.remove(found)
    updated = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "group": new_group
    }

    
    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, updated)
    print( "Student has been updated\n")


def main():
    """Головне меню"""
    while True:
        choice = input("Choose action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                addNewElement()
            case "U" | "u":
                updateElement()
            case "D" | "d":
                deleteElement()
            case "P" | "p":
                printAllList()
            case "X" | "x":
                print(" Exit program")
                break
            case _:
                print(" Wrong choice\n")


if __name__ == "__main__":
    main()
