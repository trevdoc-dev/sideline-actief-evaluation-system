To clone your Django project repository on a Windows 10 machine and set it up, follow these steps:

---

### **1. Install Required Tools**

Ensure the following are installed on your Windows machine:

1. **Python:** Download and install the latest Python version from [python.org](https://www.python.org/).
   - During installation, check the box to **Add Python to PATH**.
2. **Git:** Download and install Git from [git-scm.com](https://git-scm.com/).
3. **Virtual Environment (venv):** Included with Python.

---

### **2. Clone the Repository**

1. Open **Command Prompt** or **PowerShell**.
2. Clone your repository:
   ```bash
   git clone https://github.com/dcatindoy/explore-django.git
   cd explore-django
   ```

---

### **3. Set Up a Virtual Environment**

1. Create a virtual environment:
   ```bash
   python -m venv env
   ```
2. Activate the virtual environment:
   - For **Command Prompt**:
     ```bash
     env\Scripts\activate
     ```

---

### **3. Install Django**

After activating the virtual environment, install Django and other dependencies:

```bash
pip install django
```

---

### **4. Verify Installation**

Check if Django is installed correctly:

```bash
python -m django --version
```

---

---

### **5. Run the Development Server**

Start the Django development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/` in your browser.

---
