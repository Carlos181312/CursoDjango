lists_numbers = [1, 2, 3, 4, 5, 2, 2, 2, 2]
lists_letters = ["a", "b", "c"]
lists_mix = [2, "z", True, [1, 2, 3], 5.5]

shopping_cart = ["Laptop", "Silla Gamer", "Café"]

print(type(lists_mix))

# Métodos

# append
print(lists_numbers)
lists_numbers.append(100)
lists_numbers.append(200)
print(lists_numbers)

# remove
lists_numbers.remove(4)
lists_numbers.remove(100)
print(lists_numbers)

# count
print(lists_numbers.count(2))

# .copy()
# .sort()