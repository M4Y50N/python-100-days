
# with open("./input/letters/starting_letter.txt", "r") as file:
#     print(file)

base_letter = open("./Input/Letters/starting_letter.txt", "r")
invites = open("./Input/Names/invited_names.txt", "r").read().split("\n")

new_letter = []
for line in base_letter:
    new_letter.append(line.strip().split(" ")) if line.strip().split(" ")[0] != '' else ''

# Create invites
for invite in invites:
    new_letter[0][1] = invite

    with open(f"./Output/ReadyToSend/{invite.lower()}_invite.txt", mode="w") as new_invite:
        for line in new_letter:
            new_invite.write(f"{" ".join(line)}\n\n")
