# File_Storage_using_Cryptography

This project is a secure web-based platform that allows users to **store, encrypt, and retrieve files** using **hybrid cryptography** — combining both symmetric (AES) and asymmetric (RSA) encryption. The application ensures privacy and access control, and features an intelligent assistant for interaction.

---

## Features

- **Hybrid Encryption**: AES (for fast encryption) + RSA (for secure key transfer)
- **User & Owner Roles**: Separate dashboards and permissions
- **Secure File Upload/Download**: Encrypted storage and controlled access
- **AI Assistant**: Interactive chatbot for help and guidance
- **Key Verification & Request Handling**
- **Cloud Data Storage Integration**
- Legal Page and Copyright
- Built with Flask + MySQL + HTML/CSS


---

##  Tech Stack

- **Frontend**: HTML5, CSS3, Font Awesome
- **Backend**: Python (Flask)
- **Database**: MySQL (with PyMySQL connector)
- **Cryptography**: PyCrypto / Cryptography module (AES + RSA)
- **Chatbot**: JavaScript-based Assistant Interface

---

## Installation

1. **Clone the Repository**

    bash
    `git clone https://github.com/Ashwinputhenveettil/File_storage_using_Cryptography.git`
    <br>`cd File_storage_using_Cryptography`

2. **Create Virtual Environment**

      `python -m venv venv` <br>
      `source venv/bin/activate`  # On Windows: venv\Scripts\activate

3. **Install Dependencies** <br>

      `pip install -r requirements.txt`

4. **Set Up MySQL Database** <br>

    Create a database (e.g., securecloud) <br>
    Update DB credentials in database.py  <br>
    conn = pymysql.connect(host="localhost", user="root", password="", database="securecloud")

5. **Run the App**
   
   python app.py <br>
   Then open http://localhost:5000 in your browser.

##  Contributors

| Name | GitHub |
|------|--------|
| A Sai Vara Prasad Reddy | [@AVSPGitHub](https://github.com/ASVPREDDY) | 
| N Paul Prasanna Kumar | [@PaulGitHub](https://github.com/Paul9441) |
| Puthenveettil Prasannan Ashwin | [@AshwinGitHub](https://github.com/yourusername) |








