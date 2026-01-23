# Zadanie 2

## SSTI

Wprowadzono podatność SSTI polegającą na

To run app

```shell
docker build -t task1-python .
docker run -p 5000:5000 task1-python
```

# 📚 Book Library App 📚

- Python Flask full stack book library application with full modularity.
- Each entity has its own files seperated (forms.py, models.py, views.py, HTML, CSS, JavaScript).
- Database will be generated and updated automatically.


## 🚀 Features 🚀

- **Dashboard:**
  - Read, add, edit, and delete books.
  - Read, add, edit, and delete customers.
  - Read, add and delete loans.

- **Search Functionality:**
  - Easily search for books by name.
  - Easily search for customers by name.
  - Easily search for loans by name.

- **Responsive Design:**
  - Provides a seamless user experience across various devices.

## 🛠️ Technologies Used 🛠️

- **Frontend:**
  - HTML
  - CSS
  - Bootstrap
  - JavaScript
  - Axios

- **Backend:**
  - Python
  - Flask
  - JSON

- **Database:**
  - SQL
  - SQLAlchemy


## 🔧 Installation 🔧

1. Clone the repository:
   git clone (https://github.com/MohammadSatel/Flask_Book_Library.git)

2. Create a virtual enviroment:
   py -m venv (virtual enviroment name)
   
3. Activate the virtual enviroment:
   (virtual enviroment name)\Scripts\activate

4. Install needed packages: 
   pip install -r requirements.txt

5. run the main app:
   py app.py (your path/Flask_Book_Library/app.py)

6. Connect to the server:
   Running on (http://127.0.0.1:5000)

7. Enjoy the full stack book library app with CRUD and DB.
