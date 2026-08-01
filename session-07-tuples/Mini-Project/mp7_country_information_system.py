countries_tuple = ("Pakistan", "India", "Bangladesh", "Afghanistan", "China", "Iran")

def features():
    print("====== COUNTRY INFORMATION SYSTEM ======")
    print("1. Display All Countries")
    print("2. Search Country")
    print("3. Show Statistics")
    print("4. Exit")

    option = int(input("Select the appropriate option: "))
    return option

option = features()

while option != 4:
    if option == 1:
        print("===== ALL COUNTRIES =====")

        for country in countries_tuple:
            print(str(countries_tuple.index(country) + 1) + ". " + country)

    elif option == 2:
        print("===== SEARCH COUNTRY =====")

        search = input("Enter country name to search: ")
        
        if search in countries_tuple:
            print(search + " Found Successfully!")
            print("Position:", countries_tuple.index(search) + 1)
        else:
            print(search +" Not Found!")

    elif option == 3:

        if len(countries_tuple)== 0:
            print("There are no countries available.")

        else:
            print("===== COUNTRY STATISTICS =====")
            print("Total Countries: " + str(len(countries_tuple)))
            print("First Country: " + countries_tuple[0])
            print("Last Country: " + countries_tuple[len(countries_tuple) - 1])

    else:
        print("Invalid Option Selected!")

    option = features()

print("Exiting...")
print("Thank You!")