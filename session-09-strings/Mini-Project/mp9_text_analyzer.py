text = input("Enter the text you want to analyze: ")

def features():
    print("====== TEXT ANALYZER ======")
    print("1. Display Text")
    print("2. Text Statistics")
    print("3. Search Word")
    print("4. Replace Word")
    print("5. Exit")

    option = int(input("Select the option you want: "))
    return option

option = features()

while option != 5:
    
    if option == 1:
        print("===== DISPLAY TEXT =====")
        print(text)

    elif option == 2:
        print("===== TEXT STATISTICS =====")
        print("Total Characters : " + str(len(text)))
        print("Total Words : " + str(len(text.split())))
        print("Uppercase : " + text.upper())
        print("Lowercase : " + text.lower())
        print("Title Case : " + text.title())

    elif option == 3:
        print("===== SEARCH WORD =====")
        search = input("Enter the word you want to search: ")

        if search in text:
            print(search + " Found Successfully!")
            print("Occurrences : " + str(text.count(search)))
            print("Position : " + str(text.find(search)))
        else:
            print(search + " Not Found!")

    elif option == 4:
        print("===== REPLACE WORD =====")
        replace = input("Enter the word you want to replace: ")

        if replace in text:
            new_word = input("Enter the new word: ")
            text = text.replace(replace, new_word)
            
            print(replace + " Replaced Successfully!")
            print("Updated Text:")
            print(text)
        else:
            print(replace + " Not Found!")
            
    else:
        print("Invalid Option Selected!")
    option = features()

print("Exiting the Text Analyzer...")
print("Thank You!")