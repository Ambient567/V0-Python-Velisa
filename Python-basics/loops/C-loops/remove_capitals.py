# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):
    result = ""
    for char in text:
        if not char.isupper():
            result += char
    return result


# Example:
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'

