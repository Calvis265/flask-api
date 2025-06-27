🦸‍♂️ Flask Superheroes API
This is a simple Flask-based RESTful API for managing superheroes, their powers, and relationships. It uses SQLite and SQLAlchemy for data persistence and ORM.

🚀 Features
Add, view, update, and delete superheroes

Assign powers to heroes

View hero-power relationships

JSON API responses

Simple, clean project structure

 Project Structure
 
flask-superheroes/
│
├── app.py                  # Main application entry point
├── models/
│   ├── __init__.py         # Initializes db and imports models
│   ├── hero.py             # Hero model
│   ├── power.py            # Power model
│   └── hero_power.py       # HeroPower model (many-to-many)
├── seed.py                 # Seed script for populating initial data
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/calvis265/flask-superheroes.git
cd flask-superheroes
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Seed the Database
bash
Copy
Edit
python seed.py
5. Run the Server
bash
Copy
Edit
flask run
Flask will run on http://127.0.0.1:5000.

📬 Sample Endpoints
GET / – Check if the API is running

GET /heroes – List all heroes

POST /heroes – Create a new hero

GET /powers – List all powers

PATCH /powers/<id> – Update a power

POST /hero_powers – Assign a power to a hero

🧪 Testing with Postman
You can use Postman or curl to test the API. Here's an example:

http
Copy
Edit
POST /heroes
Content-Type: application/json

{
  "name": "Clark Kent",
  "super_name": "Superman"
}
📌 Requirements
Python 3.12+

Flask

Flask-SQLAlchemy

SQLite (default with Python)

 
