# remove the vowels from the sentence uaoie

phrase = input("enter your phrase to remove its vowels: ")



def remove_vowels(phrase):
    vowels = "aAuUoOiIeE"
    for v in vowels :
     phrase = phrase.replace(v, "")
    return phrase


print(remove_vowels(phrase))


