# setting a PLACEHOLDER which will be used to replace the '[name]' placeholder in messages
PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as start:
    names=start.readlines() # get list of names. readlines() returns a list with each line being an item
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents=letter.read() # read starting letter's content
    for name in names: # loop through the list of names
        stripped_name=name.strip() # strip the name
        # replace '[name]' with the name in the letter
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        # Create a file and write within it with the file carrying the name's value
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", "w") as personalized_letter:
            personalized_letter.write(new_letter)



