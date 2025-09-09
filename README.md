Link pws: https://jovian-felix-pacilstore.pbp.cs.ui.ac.id/

Jawaban : 
1. Cara saya untuk menyelesaikan checklist tersebut step by step yaitu dengan mereview kembali tutorial dan memahami tiap langkah-langkahnya. 
   Berikut uraiannya : 
   - Checklist 1 : Pertama, saya siapkan dulu dengan membuat repositori baru di github dan juga direktori lokal yang akan menjadi tempat proyeknya. Direktori lokal tersebut kemudian di inisiasi dengan git dan dihubungkan ke repositori yang sudah dibuat tadi. Lalu, saya mengaktifkan virtual environment di direktori lokal tadi, dan download semua requirements yang dibutuhkan. Setelah selesai download, saya bisa mulai buat sebuah projek django. Di sini, saya juga melakukan konfigurasi dasar untuk proyek ini.
   - Checklist 2 : Membuat aplikasi main dengan menjalankan perintah di terminal. Di dalam aplikasi main, saya juga menyiapkan beberapa template html yang akan digunakan nantinya.
   - Checklist 3 : Pada file urls.py di level proyek, saya menambahkan fungsi include untuk menghubungkan proyek dengan aplikasi main. Dengan begitu, semua routing yang ada di aplikasi main dapat dikenali di proyek utama.
   - Checklist 4 : Membuat blueprint desain tabel database di models.py sesuai ketentuan yang diminta. Tapi ini hanya blueprint, database aslinya baru terbentuk setelah kita melakukan proses migrasi.
   - Checklist 5 : Buka views.py dan menambah fungsi-fungsi yang menerima parameter request. Fungsi-fungsi ini nantinya akan return sebuah fungsi render dengan berkas html yang sesuai. 
   - Checklist 6 : Menambah path untuk fungsi view di bagian list urlpatterns di urls.py pada level aplikasi main. Sehingga, setiap URL yang dipanggil bisa diarahkan ke view yang tepat, lalu ditampilkan dengan template yang sesuai.
   - Checklist 7 : Terakhir, buka web https://pbp.cs.ui.ac.id/ dan create new project. Di sana, kita nanti akan push semua perubahan pada proyek kita. Kita juga harus push ke repositori github agar semua perubahan tercatat.

2. Link gambar : https://web-cms.biznetgio.com/uploads/django_77d5263d13.jpg
   Alur : Pertama, client akan mengirimkan request ke server. Setelah django menerima request tersebut, ia langsung ke urls.py untuk melihat pola URL dan menentukan fungsi mana di views.py yang akan dijalankan. Di sini, fungsi view bisa mengambil data dari models.py dan mengirim data ke template. Jadi bisa dibilang proses view ini adalah otak dari aplikasi yang memutuskan apa yang harus dilakukan pada setiap request. Setelah view mendapat data dari model, ia langsung memilih template HTML mana untuk ditampilkan ke client. Nah setelah itu semua, baru django akan mengirim hasilnya sebagai response ke client.

3. Peran settings.py dalam django cukup penting. Bisa dibilang, settings.py seperti buku aturan untuk proyek django kita. Di sini, kita yang     
   mengatur bagaimana keseluruhan projek kita akan berjalan. Beberapa tugas setting.py yaitu :
   - Konfigurasi dasar proyek. Di sini, kita bisa menyimpan beberapa konfigurasi untuk proyek kita seperti zona waktu dan bahasa.
   - Menyimpan daftar aplikasi mana saja yang aktif dalam proyek kita. Daftar aplikasi ini bisa kita temukan di bagian INSTALLED_APPS.
   - Konfigurasi database yang kita gunakan (menentukan database mana yang kita gunakan).
   - Menyimpan pengaturan keamanan (security dan credential).
   - Menentukan middleware mana saja yang digunakan.
   - Mengatur bagaimana django mencari file-file html (template).

4. Saat kita membuat model di models.py, sebenarnya kita hanya membuat semacam blueprint tabel, tapi belum benar-benar ada di databasenya.  
   Blueprint tersebut akan dicatat dalam sebuah file migrasi saat kita menjalankan perintah makemigrations. Setelah itu, melalui perintah migrate, django akan mengeksekusi file migrasi tersebut sehingga tabel dan kolom benar-benar dibuat di database. Jadi, ketika kita membuat perubahan di models.py, kita harus melakukan migrasi agar perubahan tersebut dicatat dan diterapkan ke database asli.

5. Menurut saya, Framework django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sifatnya yang mudah dan lengkap. 
   Django sendiri sudah dilengkapi berbagai fitur bawaan yang mempermudah pembelajaran seperti ORM untuk database. Django juga terstruktur dengan menerapkan konsep seperti MVT (Model View Template), yang membuat alur kerja lebih terorganisir dan jelas. Terakhir, django menggunakan salah satu bahasa pemrograman yang relatif lebih mudah dibanding kebanyakan bahasa lainnya yaitu python. Hal-hal inilah yang membuat django menjadi pilihan yang tepat untuk pembelajaran pengembangan perangkat lunak pertama kali.

6. Sejauh ini, semua tutorial yang saya kerjakan berjalan dengan lancar. Semua panduan dan instruksi di tutorial tersebut dapat dipahami dengan 
   mudah. Para asdos juga selalu stand by di discord jika ada pertanyaan.