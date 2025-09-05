📝 Blog API
Selamat datang di Blog API! Ini adalah backend RESTful yang tangguh dan aman untuk platform blog, dibangun menggunakan Flask, SQLAlchemy, dan diautentikasi dengan JWT (JSON Web Tokens).

API ini menyediakan fungsionalitas penuh untuk mengelola post, kategori, dan komentar, lengkap dengan sistem otorisasi berbasis peran (Admin vs. Pengguna biasa).

✨ Fitur Utama
** manajemen Post:** Operasi CRUD (Create, Read, Update, Delete) penuh untuk postingan blog.

** manajemen Kategori:** Admin dapat membuat, memperbarui, dan menghapus kategori.

** Sistem Komentar:** Pengguna dapat berkomentar pada postingan dan menghapus komentar mereka sendiri.

🔐 Autentikasi & Otorisasi:

Menggunakan JWT untuk mengamankan endpoint.

Peran pengguna dibedakan (Admin dan Pengguna biasa).

Hanya admin yang bisa mengelola kategori.

Hanya penulis post/komentar atau admin yang bisa mengubah/menghapusnya.

** Database:** Menggunakan SQLAlchemy ORM untuk interaksi database yang efisien.

🚀 Teknologi yang Digunakan
Backend: Flask

ORM: SQLAlchemy

Autentikasi: Flask-JWT-Extended

Database: (Dapat dikonfigurasi, misal: PostgreSQL, SQLite)

🛠️ Cara Menjalankan Proyek
Untuk menjalankan proyek ini di mesin lokal Anda, ikuti langkah-langkah berikut:

1. Clone Repositori

git clone [https://github.com/viktoryglory/blog-API.git](https://github.com/viktoryglory/blog-API.git)
cd blog-API

2. Buat dan Aktifkan Virtual Environment

Windows:

python -m venv venv
.\venv\Scripts\activate

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Ketergantungan (Dependencies)
Pastikan Anda memiliki file requirements.txt.

pip install -r requirements.txt

4. Konfigurasi Environment Variables
Buat file .env di direktori root dan isi dengan konfigurasi yang diperlukan.

# Contoh .env
DATABASE_URL="postgresql://user:password@host:port/dbname"
JWT_SECRET_KEY="super-secret-key-kamu"

5. Inisialisasi Database
(Asumsi menggunakan Flask-Migrate)

flask db init
flask db migrate -m "Initial migration."
flask db upgrade

6. Jalankan Aplikasi

flask run

API akan berjalan di http://127.0.0.1:5000.

📚 Dokumentasi API Endpoint
Berikut adalah daftar endpoint yang tersedia.

Keterangan:

🔓 Publik: Tidak memerlukan autentikasi.

👤 Pengguna: Memerlukan token JWT dari pengguna yang sudah login.

👑 Admin: Memerlukan token JWT dari pengguna dengan hak akses admin.

🏠 Umum
Metode

Endpoint

Deskripsi

Akses

GET

/

Cek status API.

🔓

📰 Postingan (Posts)
Metode

Endpoint

Deskripsi

Akses

GET

/posts

Mendapatkan semua postingan.

🔓

GET

/posts/<id>

Mendapatkan detail satu postingan.

🔓

POST

/posts

Membuat postingan baru.

👤

PUT

/posts/<id>

Memperbarui postingan (oleh penulis/admin).

👤

DELETE

/posts/<id>

Menghapus postingan (oleh penulis/admin).

👤

Contoh POST /posts Body:

{
    "title": "Judul Post Baru Saya",
    "content": "Ini adalah isi dari post yang sangat menarik.",
    "category_id": 1
}

🏷️ Kategori (Categories)
Metode

Endpoint

Deskripsi

Akses

GET

/categories

Mendapatkan semua kategori.

🔓

POST

/categories

Membuat kategori baru.

👑

PUT

/categories/<id>

Memperbarui nama/deskripsi kategori.

👑

DELETE

/categories/<id>

Menghapus kategori (jika tidak ada post).

👑

Contoh POST /categories Body:

{
    "name": "Teknologi",
    "description": "Semua tentang perkembangan teknologi."
}

💬 Komentar (Comments)
Metode

Endpoint

Deskripsi

Akses

GET

/posts/<id>/comments

Mendapatkan semua komentar di sebuah post.

🔓

POST

/posts/<id>/comments

Menambahkan komentar baru di sebuah post.

👤

DELETE

/comments/<id>

Menghapus komentar (oleh penulis/admin).

👤

Contoh POST /posts/<id>/comments Body:

{
    "content": "Komentar yang sangat membangun!"
}

🤝 Berkontribusi
Kontribusi sangat kami harapkan! Jika Anda ingin berkontribusi, silakan buat fork dari repositori ini dan ajukan Pull Request.