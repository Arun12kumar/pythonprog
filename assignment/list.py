def copy_fruits_with_e(fruits):
    e_fruits = []
    for fruit in fruits:
        if 'e' in fruit:
            e_fruits.append(fruit)
    return e_fruits


fruits = ['apple', 'banana', 'orange', 'kiwi', 'pear', 'grape']


e_fruits = copy_fruits_with_e(fruits)


print("Original list of fruits:", fruits)
print("Fruits with the letter 'e':", e_fruits)
