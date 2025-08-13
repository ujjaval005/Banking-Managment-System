<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Banking Management System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 40px;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2 {
      color: #005f73;
    }
    code {
      background-color: #eee;
      padding: 2px 6px;
      border-radius: 4px;
    }
    pre {
      background-color: #eee;
      padding: 10px;
      border-radius: 6px;
      overflow-x: auto;
    }
    ul {
      list-style-type: square;
    }
  </style>
</head>
<body>

  <h1>🏦 Banking Management System</h1>
  <p>A simple command-line banking management system built in Python. It allows users to create accounts, deposit and withdraw money, view details, update information, and delete accounts. Data is stored persistently using a JSON file.</p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Create a new bank account with validation</li>
    <li>Deposit money (limit: ₹0–₹10,000)</li>
    <li>Withdraw money with balance check</li>
    <li>View account details securely</li>
    <li>Update name, email, or PIN</li>
    <li>Delete account with confirmation</li>
    <li>PIN-based authentication</li>
    <li>Persistent storage using <code>data.json</code></li>
  </ul>

  <h2>🛠️ Technologies Used</h2>
  <ul>
    <li>Python 3.x</li>
    <li>JSON for data storage</li>
    <li>Git for version control</li>
  </ul>

  <h2>📦 Project Structure</h2>
  <pre>
Banking-Managment-System/
├── main.py         # Main application logic
├── data.json       # Stores user account data
└── README.html     # Project documentation
  </pre>

  <h2>🧑‍💻 How to Run</h2>
  <ol>
    <li>Clone the repository:<br>
      <code>git clone https://github.com/ujjaval005/Banking-Managment-System.git</code><br>
      <code>cd Banking-Managment-System</code>
    </li>
    <li>Run the script:<br>
      <code>python main.py</code>
    </li>
    <li>Follow the on-screen menu to interact with the system.</li>
  </ol>

  <h2>🔐 Security Notes</h2>
  <ul>
    <li>PINs are stored in plain text for simplicity. Consider hashing for production use.</li>
    <li>Email format is not validated—can be improved with regex.</li>
    <li><code>data.json</code> is not encrypted. Avoid storing sensitive data.</li>
  </ul>

  <h2>📈 Future Improvements</h2>
  <ul>
    <li>Add transaction history and timestamps</li>
    <li>Implement PIN hashing and email validation</li>
    <li>Create a GUI using Tkinter or PyQt</li>
    <li>Add unit tests for core functions</li>
  </ul>

  <h2>📬 Contact</h2>
  <p>Made with ❤️ by <a href="https://github.com/ujjaval005" target="_blank">Ujjaval</a><br>
  Feel free to fork, contribute, or raise issues!</p>

</body>
</html>
