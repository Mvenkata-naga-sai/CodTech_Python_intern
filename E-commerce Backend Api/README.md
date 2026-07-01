# 🛒 E-Commerce Backend API (FastAPI)

🚀 A modern and scalable **E-Commerce Backend API** built using **FastAPI**, designed with clean architecture and ready for real-world applications.

---

## 📌 Features

* 🔐 User Authentication (JWT-based)
* 👤 User Registration & Login
* 📦 Product Management (Create & View)
* 🛒 Order Management
* ⚡ FastAPI high-performance backend
* 🗄️ SQLite Database (can upgrade to PostgreSQL)
* 📄 Auto-generated API Docs (Swagger UI)

---

## 🏗️ Project Structure

```
ecommerce-backend/
│
├── app/
│   ├── main.py          # Entry point
│   ├── db.py            # Database connection
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── auth.py          # Authentication logic
│   ├── routes/
│   │   ├── user.py      # User APIs
│   │   ├── product.py   # Product APIs
│   │   ├── order.py     # Order APIs
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-backend.git
cd ecommerce-backend
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Documentation

After running the server, open:

👉 http://127.0.0.1:8000/docs

FastAPI provides an interactive Swagger UI to test APIs.

---

## 🔐 Authentication

* Register a new user using `/auth/register`
* Login using `/auth/login`
* Receive a JWT token for secure access

---

## 📦 API Endpoints

### 👤 User

* `POST /auth/register` → Register user
* `POST /auth/login` → Login user

### 📦 Products

* `POST /products/` → Create product
* `GET /products/` → Get all products

### 🛒 Orders

* `POST /orders/` → Place order

---

## 🧪 Example Request

### Create Product

```json
{
  "name": "Laptop",
  "price": 50000,
  "stock": 10
}
```

---

## 🚀 Future Enhancements

* ✅ JWT Protected Routes
* 🛍️ Cart & Wishlist System
* 💳 Payment Integration (Stripe/Razorpay)
* 🐳 Docker Support
* 🗄️ PostgreSQL Database
* 🔍 Search & Filtering
* 📊 Admin Dashboard
* ⚡ Redis Caching

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author
m venkata naga sai

Intern Id: CITS4390

computer science engineering

---

# 📌 Conclusion

This E-Commerce Backend API demonstrates the core functionalities required to build a scalable and efficient online shopping platform using FastAPI. It covers essential features such as user authentication, product management, and order processing while following a clean and modular architecture.

The project serves as a strong foundation for real-world applications and can be further enhanced with advanced features like payment integration, role-based access control, caching, and deployment strategies.

Overall, this project highlights modern backend development practices and showcases the power and performance of FastAPI in building high-quality APIs.


---

⭐ If you like this project, give it a star on GitHub!
