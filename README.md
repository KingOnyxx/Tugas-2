# 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Menginstall env dengan python.
2. Menginstall dependencies.
3. Membuat aplikasi baru dan mendaftarkan ke dalam `settings.py`.
4. Membuat template dasar menggunakan html.
5. Membuat implementasi di `models.py`.
6. Membuat implementasi di `views.py`.
7. Mengonfiguarsi routing URL di `urls.py` direktori aplikasi main dan routing URL di `urls.py`di direktori utama.
# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara *`urls.py`*, *`views.py`*, *`models.py`*, dan berkas html.
\
\
![Bagan Django](https://cdn.discordapp.com/attachments/1013790676296683592/1149595864315199529/Bagan_django.png)
Client akan request ke `urls.py`. Lalu, `urls.py`akan memilih view dari `views.py`. Setelah itu, `views.py` akan mengirimkan query ke `models.py` dan mengembalikan data. Selanjutnya akan memilih berkas HTML dan HTML akan menampilkan halaman web kembali ke client.

# 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? 
- Virtual environment digunakan untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer local. 
- Kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya kita tidak dapat mengisolasi project untuk mencegah terjadinya konfilk antar project.

# 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- Model View Controller (MVC) adalah sebuah metode untuk membuat sebuah aplikasi dengan memisahkan data (Model) dari tampilan (View) dan cara bagaimana memprosesnya (Controller)
- Model View Template (MVT) adalah sebuah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. 
- Model View ViewModel (MVVM) adalah salah satu arsitektur pembuatan aplikasi berbasis GUI yang berfokus pada pemisahan antara kode untuk logika bisnis dan tampilan aplikasi.