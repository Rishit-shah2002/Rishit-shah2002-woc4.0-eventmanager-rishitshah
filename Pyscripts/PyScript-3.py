class contact:
    def __init__(self, name, contactNo):
        self.name = name
        self.contactNos = [contactNo]


def get_name(self):
    return self.name


print("Enter a number for what you want to do: ")
print("1. Make new contact")
print("2. Add another mobile number to an existing contact")
print("3. Search a contact")
print("4. View all contacts")
print("5 Exit")

contactList = []

while(1):
    action = input("Enter a number between 1-5: ")
    if int(action) == 1:
        name = input("Name: ")
        contactNo = input("Contact Number: ")
        if(len(contactNo) != 10):
            print("Please enter 10 digit mobile number")
            continue
        obj = contact(name, int(contactNo))
        contactList.append(obj)
        contactList = sorted(contactList, key=get_name)
    elif int(action) == 2:
        name = input("Name: ")
        flag = 0
        for obj in contactList:
            if obj.name == name:
                contactNo = input("Contact Number: ")
                obj.contactNos.append(int(contactNo))
                flag = 1
                break
        if flag == 0:
            print("Contact name does not exist")
    elif int(action) == 3:
        subString = input("Enter contact name you want to search: ")
        count = 0
        c = []
        for obj in contactList:
            if subString in obj.name:
                c.append(obj)
                print(obj.name)
                count = count + 1
        if count==1:
            print(f"{obj.name}: {obj.contactNos}")
        elif count > 0:
            index = input(
                "Choose out of the given contacts(enter the index of the contact): ")
            print(c[int(index)].name,
                  c[int(index)].contactNos)
        else:
            print("The given substring was not found in your existing contacts")
    elif int(action) == 4:
        for i in contactList:
            print(f"Name: {i.name} Contact Number: {i.contactNos}")
    elif int(action)==5:
        break
    else:
        print("Please enter any number only from the above options available")
        continue

for obj in contactList:
    print(obj.name, obj.contactNos)
