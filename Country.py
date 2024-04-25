#Marty Wallace CIS261 Country
def menu():
    print("Command Menu")
    print("view --> View country name")
    print("add --> Add a country")
    print("delete --> Delete a country")
    print("exit --> Exit the program")
    print()
    
def initiate_dict():
    global country_dict
    country_dict = {"AF":"Afghanistan","DE":"Germany","US":"United States"}

def command():
    print()
    selection = input("COMMAND: ")
    if selection.lower() == "view":
        view(country_dict)
    elif selection.lower() == "add":
        add()
    elif selection.lower() == "delete":
        delete()
    elif selection.lower() == "exit":
        end()
    else:
        print("Please enter a valid selection from menu")
        print()
    command()

def view(countries):
    codes = " ".join(countries.keys())
    print(codes)
    code = input("Enter country code: ").upper()
    if code in country_dict:
        print(country_dict[code])
    else:
        print("Please enter valid country code")
        print()
        view(countries)
    command()

def add():
    while True:
        code = input("Enter country code: ").upper()
        if len(code) == 2 and code.isalpha() and code not in country_dict:
            name = input("Enter country name: ").capitalize()
            country_dict[code] = name
            break
        else:
            print("Please enter valid country code")
            add()
    command()
    
def delete():
    code = input("Enter country code: ").upper()
    if len(code) == 2 and code.isalpha() and code in country_dict:
        country_dict.pop(code)
        command()
    else:
        print("Please enter valid country code")
        print()
        delete()

def end():    
    print("Bye!")
    exit()
    
if __name__ == "__main__":
    initiate_dict()
    menu()
    command()