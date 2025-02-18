# Django CV Project by Jesse Futerman

This project displays my  resume using a Django web application.  
It is designed for easy local setup and execution.

---

## How to Run the Project

### **1. Clone the Repository**
First, download the project from GitHub:

```bash
git clone git@github.com:jfuterman/Django-CV-Project.git
cd Django-CV-Project

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Imstall Dependencies
pip install -r requirements.txt

# Set up Django
python3 manage.py migrate

# Run the Server
python3 manage.py runserver

# Then open your browser and go to:
http://127.0.0.1:8000/cv/

