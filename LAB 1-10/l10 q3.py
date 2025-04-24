# Name: Heet Ghiya, Roll Number: 24BCH085 - Question 3 Solution
# Program to create vCard from user input

name = input("Enter contact name: ")
phone = input("Enter phone number: ")
email = input("Enter email address: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD"""

with open(f"{name.replace(' ', '_')}.vcf", 'w') as file:
    file.write(vcard)

print(f"vCard for {name} created successfully!")