# 🏦 Banking Management System

A simple command-line banking management system built in Python. It allows users to create accounts, deposit and withdraw money, view details, update information, and delete accounts. Data is stored persistently using a JSON file.

---

## 🚀 Features

- ✅ Create a new bank account with validation
- 💰 Deposit money (limit: ₹0–₹10,000)
- 🏧 Withdraw money with balance check
- 📋 View account details securely
- ✏️ Update name, email, or PIN
- 🗑️ Delete account with confirmation
- 🔐 PIN-based authentication
- 🔄 Persistent storage using `data.json`

---

## 🛠️ Technologies Used

- Python 3.x
- JSON for data storage
- Git for version control

---

## 📦 Project Structure
Banking-Managment-System/ ├── main.py         # Main application logic ├── data.json       # Stores user account data └── README.md       # Project documentation

---

## 🧑‍💻 How to Run

1. Clone the repository:
   
git clone https://github.com/ujjaval005/Banking-Managment-System.git cd Banking-Managment-System

2. Run the script:


python main.py

3. Follow the on-screen menu to interact with the system.

---

## 🔐 Security Notes

- PINs are stored in plain text for simplicity. Consider hashing for production use.
- Email format is not validated—can be improved with regex.
- `data.json` is not encrypted. Avoid storing sensitive data.

---

## 📈 Future Improvements

- Add transaction history and timestamps
- Implement PIN hashing and email validation
- Create a GUI using Tkinter or PyQt
- Add unit tests for core functions

---

## 📬 Contact

Made with ❤️ by [Ujjaval](https://github.com/ujjaval005)

Feel free to fork, contribute, or raise issues!








