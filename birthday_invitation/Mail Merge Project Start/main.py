PLACEHOLDER="[name]"

with open("Mail Merge Project Start//Input//Names//invited_names.txt") as N_file:
    names_file=N_file.readlines()
    print(names_file)

with open("Mail Merge Project Start//Input//Letters//starting_letter.txt") as L_file:
    letter_file=L_file.read()
    for name in names_file:
        stripped_name=name.strip()
        letter_content=letter_file.replace(PLACEHOLDER,stripped_name)
        with open(f"Mail Merge Project Start//Output//ReadyToSend//send to {stripped_name}","w") as completed_letter:
            completed_letter.write(letter_content)
            
   





    

