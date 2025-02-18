def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents


book = main()

def count_strings(text):
    words = text.split()
    num_of_w = len(words)
    return num_of_w

num_of_words = count_strings(book)

def count_chars(text):
    chars = {}
    lower_text = text.lower()
    for char in lower_text:
        chars[char] = chars.get(char, 0) + 1
    return(chars)

count_chars(book)


chars_dict = count_chars(book)



# Create a list to hold dictionaries for alphabetic characters
data = []

# Loop through the key-value pairs in char_counts
for char, count in chars_dict.items():
    # Check if the character is alphabetic
    if char.isalpha():
        # Create a dictionary for this character
        data.append({"name": char, "num": count})

# Now the `data` list contains all valid dictionaries
def sort_on(dict):
    return dict["num"]

data.sort(reverse=True, key=sort_on)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{num_of_words} words found in the document\n")

for item in data:
    char = item["name"]
    count = item["num"]
    print(f"The '{char}' character was found {count} times")

print("--- End report ---")