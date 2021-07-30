#TODO: Create a letter using starting_letter.rtf
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("Input/Names/invited_names.txt", mode = "r") as invited_names:
    #invited_people = invited_names.read().splitlines()
    invited_people = invited_names.readlines()
invited_people = [x.rstrip() for x in invited_people]

n = 0
with open("Input/Letters/starting_letter.rtf") as starting_letter:
    start = starting_letter.read()
    for inv in invited_people:
        message = start.replace("[name]", f"{inv}")
        with open(f"Output/ReadyToSend/letter_for_{inv}.rtf", mode="w") as toSendMessage:
            toSendMessage.write(message)
            print(message)




