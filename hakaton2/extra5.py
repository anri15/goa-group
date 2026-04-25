#Instructions:
#Write a program repeat_word(word, times) that repeats a word times times.
#Test Cases:
#assert repeat_word("hi", 3) == "hihihi"
#assert repeat_word("Python", 2) == "PythonPython"
#assert repeat_word("x", 5) == "xxxxx"
def repeat_word(word,times):
    return word * times
text = input("enter text:")
num = int(input("enter num:"))
print(repeat_word(text,num))

