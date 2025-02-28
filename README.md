# Django Spreadsheet Web Application

## 📌 Project Overview

This project is a **spreadsheet web application** built using **Django** and **MySQL**. It provides functionalities similar to Google Sheets, including:

- **Arithmetic functions**: SUM, AVERAGE, COUNT, MAX, MIN
- **Data quality functions**: TRIM, UPPER, LOWER, FIND & REPLACE
- **Formula support** (e.g., `=SUM(A1:A5)`)
- **Drag functionality** to extend formulas and values

## 🚀 Technologies Used

- **Backend**: Django (Python), Django REST Framework (DRF)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Libraries**: jQuery (for dynamic UI functionality)

## 📂 Project Structure

```
spreadsheet/
│── spreadsheetapp/
│   │── migrations/
│   │── static/
│   │── templates/
│   │   │── spreadsheet/
│   │   │   │── index.html  # UI for the spreadsheet
│   │── views.py   # Business logic for spreadsheet
│   │── models.py  # Database models
│   │── urls.py    # API endpoints
│   │── serializers.py # DRF serializers
│── manage.py  # Django project manager
│── requirements.txt  # Dependencies
```

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/yourusername/spreadsheet-app.git
cd spreadsheet-app
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)

```sh
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

Update `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spreadsheet_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5️⃣ Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Development Server

```sh
python manage.py runserver
```

Visit **`http://127.0.0.1:8000/`** in your browser.

## 📊 Features & Usage

### 📝 Saving & Loading Spreadsheets

- **Save a spreadsheet**: Uses a REST API to store spreadsheet data in the database.
- **Load a spreadsheet**: Fetches data from the database and displays it dynamically.

### 🔢 Using Formulas

- Type a formula into any cell (e.g., `=SUM(A1:A5)`) and press `Enter` to compute results.
- Supports **SUM, COUNT, AVERAGE, MAX, MIN**.

### 🎨 Drag and Drop Functionality

- Click and drag the bottom right corner of a cell to apply formulas dynamically to adjacent cells.

## 🛠 Troubleshooting

### MySQL Connection Issues

If you face errors connecting to MySQL, ensure the MySQL server is running:

```sh
udo service mysql start  # Linux/macOS
net start mysql  # Windowss
```

Or check database credentials in `settings.py`.

### Django Not Recognizing Migrations

```sh
python manage.py migrate --run-syncdb
```

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📜 License

MIT License. See `LICENSE` for details.

