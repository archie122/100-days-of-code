# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", mode="r") as f:
    letter = f.readlines()

with open("./Input/Names/invited_names.txt", mode="r") as f:
    invited_names = f.readlines()

print(letter)

for name in invited_names:
    new_letter = letter[0].replace("[name]", name.strip())
    for i in range(1, len(letter)):
        new_letter += letter[i]
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
        f.write(new_letter)