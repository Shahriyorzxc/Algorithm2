#Argument sifatida roʻyxat va satrni oladigan va indeksini qaytaruvchi funksiya
def find_index(lst, string):
    if string in lst:
        return lst.index(string)
    else:
        return -1

print(find_index(["hi", "edabit", "fgh", "abc"], "fgh"))
print(find_index(["Red", "blue", "Blue", "Green"], "blue"))
print(find_index(["a", "g", "y", "d"], "d"))
print(find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple"))

#-1 sonlar ro'yxatini oladigan va teskarisini qaytaradigan funksiya
def invert_list(lst):
    return [-x for x in lst]

print(invert_list([1, 2, 3, 4, 5]))
print(invert_list([1, -2, 3, -4, 5]))
print(invert_list([]))


