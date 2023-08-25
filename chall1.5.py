
stext = input("enter your sentence: ")
def dep_counter(text):
    occcurred = []
    found = []
    counter = 0

    for letter in text :
        if letter.lower() not in occcurred :
            
            occcurred.append(letter.lower())
            
        else :
            if letter.lower() not in found :
                found.append(letter.lower())
                counter += 1
    return "list of deplicate: ", found ,"there is: ", counter ,"deplicates " 

print(dep_counter(stext))