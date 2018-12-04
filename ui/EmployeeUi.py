
class EmployeeUi():
    def __init__(self):
        pass
    def startPageMenu(self):
        action = True
        while action:
            startPageMenuPrint()
            action = startPageMenuAction()

        
def startPageMenuPrint():
    print("--------Start-Page--------")
    print("1. Show all available cars.")
    print("2. Show rented out cars.")
    print("3. Register customer.")
    print("4. Car rental registration.")
    print("5. Find a customer.")
    print("6. Look up an order.")
    print("7. Calculate direct costs")
    print("8. Return a car.")
    print("9. Edit/Update previous order.")
    print("10. Edit/Update previous order.")
    print("11. show all recent changes.")
    print("12. Quit")

def startPageMenuAction():
    action = input("User Action: ")
    if action == '1':
        print("picked 1")
    elif action == '3':
        print ("picked 3")
    elif action == '12':
        print("Exiting program")
        return False
    return True

