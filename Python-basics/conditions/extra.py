num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd")

password = "Code123"

if len(password) < 4:
    print("too short")
elif password.isalpha():
    print("weak")
elif password.isalnum():
    print("medium")
else:
    print("strong")


temp = 32

if temp < 0:
    print("freezing")
elif temp < 20:
    print("cold")
elif temp < 30:
    print("warm")
else:
    print("hot")

ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")

ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")

