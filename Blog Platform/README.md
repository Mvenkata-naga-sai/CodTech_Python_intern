# 📝 Blog Platform Backend (Django)

🚀 A scalable and modular **Blog Platform Backend** built using **Django** and **Django REST Framework (DRF)**. This project provides APIs for managing blog posts, users, comments, and likes, making it a solid foundation for modern web applications.

---

## 📌 Features

* 👤 Custom User Model
* 📝 Create & Manage Blog Posts
* 💬 Comment System
* ❤️ Like System
* ⚡ RESTful APIs using Django REST Framework
* 🗄️ SQLite Database (Upgradeable to PostgreSQL)
* 📄 Clean and Modular Project Structure

---

## 🏗️ Project Structure

```bash id="1k3n9a"
blog-platform/
│
├── blog_platform/        # Main project settings
│   ├── settings.py
│   ├── urls.py
│
├── apps/
│   ├── users/            # User model
│   ├── posts/            # Blog posts
│   ├── comments/         # Comments system
│   ├── likes/            # Like system
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash id="vxv3np"
git clone https://github.com/your-username/blog-platform.git
cd blog-platform
```

### 2️⃣ Install Dependencies

```bash id="0n4f7s"
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations

```bash id="4d82jx"
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Run the Server

```bash id="7w9g5p"
python manage.py runserver
```

---

## 🌐 API Endpoints

### 📝 Posts

* `GET /api/posts/` → Get all posts
* `POST /api/posts/` → Create a new post

### 💬 Comments

* (Model available – API can be extended)

### ❤️ Likes

* (Model available – API can be extended)

---

## 📄 API Documentation

After running the server, access:

👉 http://127.0.0.1:8000/api/posts/

---

## 🧪 Example Request

### Create Post

```json id="5m7l2s"
{
  "title": "My First Blog",
  "content": "This is my blog content"
}
```

---

## 🚀 Future Enhancements

* 🔐 JWT Authentication (Login & Signup APIs)
* 👥 Follow / Unfollow Users
* ❤️ Like & Unlike APIs
* 💬 Full Comment CRUD APIs
* 🔍 Search & Filtering
* 📄 Pagination
* 🐳 Docker Support
* 🗄️ PostgreSQL Database
* ☁️ Deployment (AWS / Render)

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

# 📌 Conclusion

This Blog Platform Backend built with Django and Django REST Framework demonstrates the fundamental concepts required to develop a scalable and maintainable web application. It provides core functionalities such as post management, user handling, and interaction features like comments and likes, all structured in a modular and organized architecture.

The project serves as a strong foundation for building real-world blogging platforms and can be further enhanced with advanced features such as authentication, search, caching, and deployment strategies. Overall, it reflects modern backend development practices and showcases the efficiency and flexibility of Django in creating robust APIs.

---

⭐ If you like this project, give it a star on GitHub!
