# Healthcare Backend (Django + DRF + PostgreSQL + JWT)

This is a simple backend project for a healthcare system.

It allows users to:
- register & login (JWT auth)
- manage patients
- manage doctors
- assign doctors to patients

---

## Tech Used

- Django:  for coding the backend logic
- Django REST Framework : for building RESTful APIs
- PostgreSQL: for data storage
- JWT (SimpleJWT): for authentication

---

## Setup Instructions

### 1. Clone / open project

```bash
cd healthcare_backend
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

- Windows (Git Bash):

```bash
source venv/Scripts/activate
```

- Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Create a database:

```sql
CREATE DATABASE healthcare_database;
```

### 5. Configure `.env`

This project loads environment variables using `python-dotenv` (see `load_dotenv()` in `config/settings.py`).

Start by copying `.env.example` to `.env`, then fill in values.

Create a `.env` file in the `healthcare_backend/` folder (same level as `manage.py`) with:

```env
SECRET_KEY=your_secret_key

DB_NAME=healthcare_database
DB_USER=postgres
DB_PASSWORD=your_password
```

> Note: `DB_HOST` and `DB_PORT` are currently hardcoded in `config/settings.py` (`localhost` / `5432`).

### Before pushing to GitHub

- Never commit `.env` (it contains secrets). This repo includes a `.gitignore` that ignores it.
- If you accidentally committed it before, untrack it and commit the removal:

```bash
git rm --cached .env
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run server

```bash
python manage.py runserver
```

---

## Authentication APIs

### Register

`POST /api/auth/register/`

Example:

```json
{
	"username": "nikhil",
	"email": "nikhil@gmail.com",
	"password": "123456"
}
```

### Login

`POST /api/auth/login/`

Response:

```json
{
	"access": "token_here"
}
```

👉 Use this token for all protected APIs:

```text
Authorization: Bearer <token>
```

---

## 👤 Patient APIs

### Add patient

`POST /api/patients/`

```json
{
	"name": "Rahul",
	"age": 25
}
```

### Get all patients (user-specific)

`GET /api/patients/`

### Get single patient

`GET /api/patients/<id>/`

### Update patient

`PUT /api/patients/<id>/`

### Delete patient

`DELETE /api/patients/<id>/`

---

## 👨‍⚕️ Doctor APIs

### Add doctor

`POST /api/doctors/`

```json
{
	"name": "Dr Sharma",
	"specialization": "Cardiology"
}
```

### Get all doctors

`GET /api/doctors/`

### Get single doctor

`GET /api/doctors/<id>/`

### Update doctor

`PUT /api/doctors/<id>/`

### Delete doctor

`DELETE /api/doctors/<id>/`

---

## 🔗 Mapping APIs (Patient ↔ Doctor)

### Assign doctor to patient

`POST /api/mappings/`

```json
{
	"patient": 1,
	"doctor": 1
}
```

### Get all mappings

`GET /api/mappings/`

### Get doctors for a patient

`GET /api/mappings/patient/<patient_id>/`

### Delete mapping

`DELETE /api/mappings/<id>/`

---

## 🧪 Testing

You can test APIs using:

- curl (terminal)
- browser (DRF UI)
- Postman

---

## 🧠 Notes

- Patients are linked to the logged-in user
- JWT is required for all protected endpoints
- Data is stored in PostgreSQL

---

# 🔥 Final result

👉 You now have:
- clean structure  
- proper documentation  
- working backend  
- assignment-ready repo  

---
