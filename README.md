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

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena model tersebut berfungsi sebagai jembatan antara basis data relasional dan bahasa pemrograman berorientasi objek (seperti Python). 

- Mapping Database ke Object Python: Django ORM memetakan tabel database ke class Python, sehingga setiap baris dalam tabel database diwakili oleh objek Python dan Setiap kolom dalam tabel diwakili oleh atribut pada class.

- Menghindari SQL Langsung: Developer tidak perlu menulis query SQL langsung. Django ORM memungkinkan developer untuk berinteraksi dengan database menggunakan kode Python, sementara query SQL dibangun di belakang layar.

- Abstraksi: Django ORM menyediakan abstraksi tinggi di mana developer dapat melakukan operasi database tanpa memikirkan detail implementasi dari setiap query SQL.






tugas 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? 
Data delivery diperlukan karena memungkinkan berbagai komponen dalam platform untuk bertukar informasi secara efisien. Hal ini mendukung fitur-fitur seperti pembaruan data secara real-time, rendering, dan interaksi antara user dan server. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON biasanya dianggap lebih baik. Hal ini karena beberapa hal:
- JSON menggunakan format yang lebih ringkas.
- JSON menggunakan struktur yang lebih sederhana dan mudah dipahami 
- JSON sebenarnya adalah format text

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form memenuhi semua syarat validasi yang telah ditentukan. Ini penting untuk memastikan bahwa data yang diterima dan disimpan ke dalam database adalah data yang benar dan sesuai dengan aturan yang ditetapkan

4.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF (Cross Site Request Forgery). CSRF adalah jenis serangan di mana penyerang memanfaatkan sesi pengguna yang valid untuk melakukan tindakan yang tidak diinginkan tanpa sepengetahuan pengguna. Dengan menambahkan csrf_token, server memastikan bahwa setiap form yang dikirim berasal dari pengguna yang sah dan bukan dari sumber eksternal. Jika csrf_token tidak digunakan, penyerang dapat memanfaatkan sesi aktif pengguna untuk mengirimkan permintaan tanpa otorisasi, seperti mengubah data atau melakukan transaksi ilegal.

5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Saya memulai dengan membuat forms.py. Lalu saya membuat sebuah form menggunakan Django ModelForm di forms.py. Form ini digunakan untuk memungkinkan pengguna menambahkan produk baru. Form ini mengambil field name, price, dan description
- Saya kemudian membuat add_product untuk memungkinkan pengguna menambah produk baru. add_product ini juga berfungsi untuk memproses form dan menyimpan produk baru ke dalam database jika form valid.
- Saya juga mengimplementasikan fitur untuk menampilkan data produk dalam format JSON dan XML menggunakan serializer dari Django.
- Di urls.py, saya menambahkan path untuk menghubungkan view dengan URL tertentu. Hal ini memungkinkan pengguna untuk mengakses halaman daftar produk, menambahkan produk baru, dan melihat data produk dalam format JSON atau XML.
- Untuk melindungi aplikasi dari serangan CSRF (Cross Site Request Forgery), saya menambahkan token CSRF di dalam form. Ini dilakukan dengan menyertakan {% csrf_token %} di dalam template add_product.html.
- Di dalam view add_product, saya menggunakan method is_valid() untuk memvalidasi data form. Method ini memeriksa apakah data yang dimasukkan oleh pengguna sesuai dengan aturan di model. Jika valid, data akan disimpan ke dalam database, jika tidak, pengguna diminta untuk memperbaiki input.

  ![Screenshot (4065)](https://github.com/user-attachments/assets/7bb9d558-a5a4-4b7f-a6d3-e19a6ba84273)
  ![Screenshot (4066)](https://github.com/user-attachments/assets/8d99621c-224c-46bf-84e9-7092964f9094)
  ![Screenshot (4068)](https://github.com/user-attachments/assets/45c017c1-cab0-4275-8bf0-cf8e7c8d0f97)
  ![Screenshot (4069)](https://github.com/user-attachments/assets/e42045a4-ab86-442a-9205-ba0b975ab052)

  
Tugas 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
perbedaan utama dari HttpResponseRedirect() dan redirect() adalah perbedaan cara pemanggilan. Keduanya melakukan hal yang sama yaitu redirect ke URL yang kita inginkan. HttpResponseRedirect() harus memanggil URL secara eksplisit menggunakan string path (misalnya, return HttpResponseRedirect('/products/')). redirect() lebih mudah dan simpel untuk digunakan (misalnya, return redirect('product_list'))

2. Jelaskan cara kerja penghubungan model Product dengan User!
- Menambahkan ForeignKey ke Model Product (contoh :(user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)) )
- Menyimpan Produk yang Dihubungkan ke Pengguna (contoh( product.user = request.user))
- Mengambil Data Berdasarkan Pengguna aku ambil nya di views product_list( products = Product.objects.filter(user=request.user))

3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Perbedaan antara authentication dan authorization

Authentication (Autentikasi):
- Apa itu: Proses untuk memverifikasi identitas pengguna. Ini memastikan bahwa pengguna adalah siapa yang mereka klaim. Proses ini biasanya melibatkan pengguna memasukkan kredensial, seperti username dan password, yang kemudian diverifikasi oleh sistem.
- Kapan terjadi: Saat pengguna mencoba masuk (login) ke dalam sistem.
- Contoh: Saat pengguna memasukkan nama pengguna dan kata sandi, sistem memverifikasi apakah kombinasi tersebut benar.

Authorization (Otorisasi):
Apa itu: Proses untuk memeriksa izin atau hak akses pengguna setelah mereka terotentikasi. Authorization memastikan pengguna hanya dapat mengakses fitur atau data yang diizinkan untuk mereka.
Kapan terjadi: Setelah pengguna berhasil login (authenticated), otorisasi digunakan untuk memeriksa apakah pengguna memiliki akses ke sumber daya tertentu, seperti halaman admin atau data sensitif.
Contoh: Setelah login, tidak semua pengguna bisa mengakses halaman admin kecuali mereka memiliki peran yang sesuai (misalnya, superuser atau admin).


Apa yang terjadi saat pengguna login?

Ketika pengguna melakukan login, proses yang terjadi adalah autentikasi. Dibawah ini adalah rincian apa yang terjadi ketika pengguna login
- authenticate() untuk memverifikasi kredensial pengguna
- Jika kredensial benar maka akan memanggil fungsi login() untuk menyimpan informasi pengguna. 



Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut


Authentication
Django menyediakan sistem autentikasi bawaan untuk mengelola login, logout, dan registrasi pengguna. Saya menggunakan login_view untuk mengimplementasikan authentication.

    def login_view(request):
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = redirect('product_list')
                    
                    last_login_time = localtime(user.last_login).strftime('%Y-%m-%d %H:%M:%S')
                    response.set_cookie('last_login', last_login_time)
                    return response
        else:
            form = AuthenticationForm()
        return render(request, 'main/login.html', {'form': form})

Authorization
Setelah authentication, django menggunakan permission system untuk memeriksa apakah pengguna memiliki hak akses ke fitur tertentu. Django juga akan menggunakan @login_required untuk mengecek pengguna, berikut adalah contohnya.

    @login_required
    def product_list(request):




4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login menggunakan session framework. Saat pengguna login, Django membuat session ID dan menyimpannya sebagai cookie di browser pengguna. Setiap kali pengguna mengirim permintaan baru, session ID ini dikirim kembali ke server, sehingga server tahu pengguna mana yang sedang login.




5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Mengimplementasikan Fungsi Registrasi, Login, dan Logout
    Registrasi :
    - Saya membuat form pendaftaran pengguna baru dengan menggunakan UserCreationForm bawaan Django dan meng-custom form tersebut dalam RegisterForm.
    - View untuk registrasi dibuat dalam register view, yang menampilkan form pendaftaran dan menyimpan data pengguna baru ke database jika valid.

    Login :
    - Saya menggunakan AuthenticationForm bawaan Django untuk autentikasi pengguna.
    - Dalam login_view, pengguna akan di-autentikasi menggunakan authenticate(). Jika berhasil, session pengguna dibuat menggunakan login().
    - Cookies last_login juga diterapkan di sini untuk menyimpan waktu login terakhir.

    Logout : 
    - Fungsi logout_view menggunakan logout() bawaan Django untuk menghapus session pengguna, dan mengarahkan mereka ke halaman login setelah keluar.

- Membuat Dua Akun Pengguna dengan Dummy Data
    - Saya membuat dua akun pengguna dengan mendaftarkan dua akun melalui halaman registrasi yang sudah saya implementasikan.
    - Setelah akun dibuat, saya membuat data dummy (produk) untuk masing-masing akun melalui form yang ada di aplikasi.

- Menghubungkan Model Product dengan User
    - Saya menambahkan relasi antara model Product dan User dengan menambahkan ForeignKey ke model Product, sehingga setiap produk yang ditambahkan akan dikaitkan  dengan pengguna yang menambahkannya.(user = models.ForeignKey(User, on_delete=models.CASCADE, null=True))
    - Dalam view untuk menambah produk (add_product), saya memastikan bahwa produk yang ditambahkan disimpan dengan user yang sedang login.
        product = form.save(commit=False)
        product.user = request.user
        product.save()

![Screenshot (4103)](https://github.com/user-attachments/assets/fc977051-bfa3-4f72-905d-b418f05812ba)
![Screenshot (4104)](https://github.com/user-attachments/assets/3f79b28e-6c7d-4a29-a1de-49cdf3e5c7fc)







  



