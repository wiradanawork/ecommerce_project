1.Tautan menuju aplikasi yang sudah di deploy

- Melakukan inisiasi git pada direktori utama dengan "git init" 
- Menambahkan konfigurasi user pada git 
- Menambah file.gitignore untuk file yang diabaikan
- Membuat repositori baru pada github bernama meowpedia 
- Membuat branch baru bernama main pada git dan menghubungkan repositori lokal dengan repositori yang telah dibuat pada githun dengan perintah "git remote add origin <link repository>.
- Melakukan add, commit, dan push pada repositori github
- Menginisialisasi project baru pada PWS dengan nama project "meowpedia" dan menyimpan kredensial untuk kedepannya
- Menghubungkan repository saat ini dengan PWS melalui perintah "git remote add pws<pws repository>.
- Menjalankan "python manage.py makemigrations" dan "python manage.py migrate" untuk memperbarui bentuk database 
- lihat project di PWS dan tunggu hingga build selesai




2.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat Main : Saya mulai dengan membuat aplikasi dengan nama main dengan menjalankan sintaks di cmd "python manage.py startapp main"

- Membuat Model: mendefinisikan model produk di models.py, saya ,mendeklarasikan atribut yang dibutuhkan seperti name, price, dan description.

- Membuat Views: Di views.py, saya membuat fungsi product_list yang mengambil produk dari model dan mengirimkan data tersebut ke template melalui context.

- Menghubungkan URL: Pada urls.py, saya menambahkan routing agar request URL diarahkan ke product_list yang ada di views.py.

- Membuat Template: Saya membuat file HTML di folder templates/main (karena kalo saya buatnya di folder templates aja nanti error saya juga kurang tau kenapa). Menggunakan syntax Django Template Language (DTL) untuk looping data produk dan menampilkan detailnya.





3.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html..

ini adalah bagan nya
"Client Request -> Django URLConf (urls.py) -> View (views.py) -> Model (models.py) -> Template (HTML) -> Response"

- Client Request: Ketika pengguna mengakses URL, request akan dikirim ke server.

- URLConf (urls.py): Django memeriksa urls.py untuk mencocokkan URL yang diminta dengan pola yang ada. Jika cocok, request dikirim ke view yang terkait.

- View (views.py): Fungsi view mengambil data (baik dari model, form, atau logic lainnya) dan menyiapkan context untuk template. Data ini kemudian dikirim ke template untuk dirender.

- Model (models.py): Jika view membutuhkan data dari database, dia akan menggunakan model untuk mengambil atau memanipulasi data. Model adalah representasi dari database dalam bentuk Python class.

- Template (HTML): Django template menggunakan data dari context yang dikirim oleh view untuk merender halaman HTML yang akan dikembalikan ke client.

- Response: Setelah HTML dirender, server mengirimkan kembali halaman yang diminta ke browser client sebagai respon

4.Jelaskan fungsi git dalam pengembangan perangkat lunak!

- Git memungkinkan developer untuk melacak perubahan dalam kode, mengembalikan ke versi sebelumnya jika terjadi kesalahan, dan mengelola berbagai versi aplikasi.

- Repositori Git bisa bertindak sebagai cadangan dari kode.

- Git memungkinkan beberapa developer bekerja pada proyek yang sama tanpa bertabrakan




5.Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django menyediakan semua yang dibutuhkan untuk membangun aplikasi web, dari pengelolaan database hingga rendering halaman web, sehingga developer tidak perlu bergantung pada banyak library eksternal.




6.Mengapa model pada Django disebut sebagai ORM?

- Mapping Database ke Object Python: Django ORM memetakan tabel database ke class Python, sehingga setiap baris dalam tabel database diwakili oleh objek Python dan Setiap kolom dalam tabel diwakili oleh atribut pada class.

- Menghindari SQL Langsung: Developer tidak perlu menulis query SQL langsung. Django ORM memungkinkan developer untuk berinteraksi dengan database menggunakan kode Python, sementara query SQL dibangun di belakang layar.

- Abstraksi: Django ORM menyediakan abstraksi tinggi di mana developer dapat melakukan operasi database tanpa memikirkan detail implementasi dari setiap query SQL.


