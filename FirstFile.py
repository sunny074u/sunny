Password = "Sunny074u"
Trial = ""
Trial_count = 0
Trial_limit = 3
Fail_password = False

while Trial != Password and not(Fail_password):
    if Trial_count < Trial_limit:
        Trial = input("Enter Trial:")
        Trial_count += 1
    else:
        Fail_passwords = True
if Fail_password:
    print("Fail_password, unsuccessful")
else:
    print("successful")

