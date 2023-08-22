# checking if the first words ends with the seconds word



word1 = "python"
word2 = input('enter a string to test: ')

def ending(word1 , word2) :

    return word1.endswith(word2)



print(ending(word1 , word2))