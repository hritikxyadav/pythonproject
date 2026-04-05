import streamlit as st
import sqlite3
from datetime import datetime

# ---------------- DATABASE ----------------
conn = sqlite3.connect("blood_donation.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    blood_group TEXT,
    city TEXT,
    phone TEXT UNIQUE,
    last_donation TEXT
)
""")
conn.commit()

# ---------------- BLOOD COMPATIBILITY ----------------
# Maps each blood group to the groups it CAN RECEIVE FROM (compatible donors)
compatibility = {
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "A+":  ["O-", "O+", "A-", "A+"],
    "A-":  ["O-", "A-"],
    "B+":  ["O-", "O+", "B-", "B+"],
    "B-":  ["O-", "B-"],
    "O+":  ["O-", "O+"],
    "O-":  ["O-"],
}

# ---------------- FUNCTIONS ----------------
def check_availability(last_date_str):
    """Returns True if the donor's last donation was 90+ days ago."""
    try:
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
        return (datetime.now() - last_date).days >= 90
    except Exception:
        return False

# ---------------- UI ----------------
st.title("🩸 Blood Donation Finder")

menu = st.sidebar.selectbox("Menu", ["Register Donor", "Search Donor", "View All Donors"])

# ---------------- REGISTER ----------------
if menu == "Register Donor":
    st.header("Register as Donor")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=18, max_value=65)
    blood = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    city = st.text_input("City")
    phone = st.text_input("Phone Number")
    last_donation = st.date_input("Last Donation Date")

    if st.button("Register"):
        if not name or not city or not phone:
            st.error("All fields are required!")

        elif len(phone) != 10 or not phone.isdigit():
            st.error("Enter a valid 10-digit phone number.")

        else:
            try:
                cursor.execute(
                    "INSERT INTO donors (name, age, blood_group, city, phone, last_donation) VALUES (?, ?, ?, ?, ?, ?)",
                    (name, age, blood, city.strip().lower(), phone, last_donation.isoformat())
                )
                conn.commit()
                st.success("Donor Registered Successfully!")

            except sqlite3.IntegrityError:
                st.warning("This phone number is already registered!")

# ---------------- SEARCH ----------------
elif menu == "Search Donor":
    st.header("Find Blood Donor")

    blood_needed = st.selectbox("Blood Group Needed", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    city = st.text_input("Enter City")

    if st.button("Search"):
        if not city:
            st.error("Please enter a city.")
        else:
            cursor.execute(
                "SELECT * FROM donors WHERE LOWER(city) = ?",
                (city.strip().lower(),)
            )
            donors = cursor.fetchall()

            # compatible_donors = blood groups that blood_needed can receive from
            compatible_donors = compatibility.get(blood_needed, [])

            results = []
            for donor in donors:
                donor_blood = donor[3]

                if donor_blood in compatible_donors:
                    available = check_availability(donor[6])
                    results.append({
                        "Name": donor[1],
                        "Blood Group": donor_blood,
                        "City": donor[4],
                        "Phone": donor[5],
                        "Available": "Yes" if available else "No"
                    })

            # Sort: available donors ("Yes") appear first
            results.sort(key=lambda x: x["Available"] == "Yes", reverse=True)

            if results:
                st.table(results)
            else:
                st.warning("No matching donors found.")

# ---------------- VIEW ALL ----------------
elif menu == "View All Donors":
    st.header("All Registered Donors")

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    data = [
        {
            "Name": donor[1],
            "Age": donor[2],
            "Blood Group": donor[3],
            "City": donor[4],
            "Phone": donor[5],
        }
        for donor in donors
    ]

    if data:
        st.table(data)
    else:
        st.info("No donors registered yet.")