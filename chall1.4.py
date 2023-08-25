# using reverse 



sentence = input("enter the sentence to be reviersed under condition: ")


def space_reverse(sentence) :

    words = sentence.split(" ")
    words = [word[::-1] if len(word) >= 5 else word for word in words]
    
    return "".join(words) 

print(space_reverse(sentence))