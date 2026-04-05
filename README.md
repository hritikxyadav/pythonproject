# 🩸 Blood Donation Finder

A web application built with **Python** and **Streamlit** that helps people find compatible blood donors in their city quickly and easily.

---

## 📌 About the Project

Blood Donation Finder is a simple yet powerful tool that connects blood donors with those in need. Users can register as donors, search for compatible donors by blood group and city, and view all registered donors — all through a clean web interface.

---

## ✨ Features

- **Register as a Donor** — Submit your name, age, blood group, city, phone number, and last donation date
- **Smart Blood Compatibility Search** — Automatically finds donors whose blood group is compatible with the recipient's blood group
- **Availability Check** — Marks donors as available only if their last donation was 90+ days ago
- **View All Donors** — Browse the complete list of registered donors
- **Local Database** — All donor data is stored locally using SQLite

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web UI framework |
| SQLite | Local database for donor records |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed. Then install the required libraries:

```bash
pip install streamlit
```

### Run the App

```bash
streamlit run pro.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🩺 Blood Compatibility Chart

| Recipient | Compatible Donors |
|---|---|
| O- | O- |
| O+ | O-, O+ |
| A- | O-, A- |
| A+ | O-, O+, A-, A+ |
| B- | O-, B- |
| B+ | O-, O+, B-, B+ |
| AB- | O-, A-, B-, AB- |
| AB+ | All blood groups |

---

## 📁 Project Structure

```
pythonproject/
│
├── pro.py               # Main application file
├── blood_donation.db    # SQLite database (auto-created on first run)
└── README.md            # Project documentation
```

---

## 👤 Author

**Hritik Yadav**  
GitHub: [@hritikxyadav](https://github.com/hritikxyadav)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
