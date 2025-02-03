# Number Classification API 🚀

This is a FastAPI-based **Number Classification API** that takes a number and returns its mathematical properties along with a fun fact.

---

## 📌 Features
- Checks if a number is **Prime, Perfect, Armstrong**.
- Identifies if the number is **Even or Odd**.
- Calculates the **digit sum** of the number.
- Fetches a **fun fact** from the [Numbers API](http://numbersapi.com/).
- Returns responses in **JSON format**.
- Handles **invalid inputs gracefully**.

---

## 🔧 Technology Stack
- **FastAPI** (Python framework for building APIs)
- **Uvicorn** (ASGI server to run FastAPI)
- **Requests** (For calling the Numbers API)
- **Postman** (For API testing)

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/levoski1/hng12-stage1.git
cd hng12-stage1

python3 -m venv venv

- Windows: venv\Scripts\activate
- Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
- The API will be available at http://127.0.0.1:8000/
```

### **2️⃣ Clone the Repository**
- URL: https://hng12-stage1.onrender.com/

- Response Format (200 OK)

    {
        "number": "-153",
        "is_prime": false,
        "is_perfect": false,
        "properties": [
        "armstrong",
        "odd"
        ],
        "digit_sum": 9,
        "fun_fact": "-153 is a boring number."
    }

🔗 Related Resources
Looking to hire skilled Python Developers? Check out:
👉[Hire Python Developers](https://hng.tech/hire/python-developers)

📜 License: 
This project is licensed under the MIT License.

👨‍💻 Author:
Levi Ugwoke

[Linkdln](https:www.linkedin.com/in/levi-soromto)