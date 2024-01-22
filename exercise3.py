# define a function with a parameter of string
def printing_even_index_on_str(word):
    print(f"Orginal String is {word}")
    print("Printing only even index chars")
# inside a function, we loop using range based on the length of the string
    word_length = len(word)
    for i in range(0, word_length, 2):
        # only print every after 2 index (provide a third arguement to the for loop)
        print(word[i])

# Ask user for a word, then run the function
user_input = input("Whats the word? ")
printing_even_index_on_str(user_input)



