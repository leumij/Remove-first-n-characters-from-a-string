# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Pseudocode

# Remove characters from a string
def remove_chars(word, n):
    print('Original string:', word)
    characters = word[n:]
    return characters

# Print a new string
print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))