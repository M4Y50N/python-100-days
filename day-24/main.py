PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as invites_file:
    invites = invites_file.readlines()

with open("./Input/Letters/starting_letter.txt") as base_letter:
    new_letter = base_letter.read()

    # Create invites
    for invite in invites:
        stripped_invite = invite.strip()
        with open(f"./Output/ReadyToSend/{stripped_invite.lower().replace(" ", "_")}_invite.txt",
                  mode="w") as new_invite:
            new_invite.write(new_letter.replace(PLACEHOLDER, stripped_invite))


