# Write your code below this line 👇

while True:
    user_input = input("Are you an idiot? (yes/no): ").strip().lower()
    if user_input in ['yes', 'y', 'true', '1']:
        is_idiot = True
        break
    elif user_input in ['no', 'n', 'false', '0']:
        is_idiot = False
        break
    else:
        print("Invalid input. Please answer yes or no.")

if is_idiot:
    print("Idiot admires complexity")
else:
    print("Genius admires simplicity")
