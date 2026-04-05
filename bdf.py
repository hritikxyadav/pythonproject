donors = []

def add_donor():
    name = input("Enter name: ")
    blood = input("Enter blood group: ")
    location = input("Enter location: ")
    contact = input("Enter contact: ")
    
    donors.append({
        "name": name,
        "blood": blood,
        "location": location,
        "contact": contact
    })

def search_donor():
    bg = input("Enter required blood group: ")
    loc = input("Enter location: ")
    
    found = False
    for d in donors:
        if d["blood"] == bg and d["location"] == loc:
            print("\nDonor Found:")
            print(d)
            found = True
    
    if not found:
        print("No donor found")

while True:
    print("\n1. Add Donor\n2. Search Donor\n3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_donor()
    elif choice == '2':
        search_donor()
    else:
        break

    