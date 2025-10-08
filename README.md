
# Framework Programming - Kelurahan App (23201276)

Project ini merupakan hasil praktikum mata kuliah **Framework Programming**, menggunakan **Django Framework**.  
Repository ini mencakup hasil pengerjaan dari **Modul 1 sampai Modul 4** dengan satu proyek utama.

---

## 👤 Identitas Mahasiswa
- **Nama:** Fredi Irawan  
- **NIM:** 23201276  
- **Mata Kuliah:** Framework Programming  
- **Dosen Pengampu:** Achmad Noercholis, S.Kom., M.Kom

---

## 📂 Struktur Repository
```
framework-programming-kelurahan-23201276/
├─ modul-1/
│  ├─ warga/
│  ├─ templates/
│  ├─ db.sqlite3
│  └─ README.md
├─ modul-2/
├─ modul-3/
├─ modul-4/
├─ docs/
└─ README.md
```

---

## 📖 Deskripsi Project
Aplikasi ini dibuat untuk mendata **warga di suatu kelurahan**, menampilkan data melalui konsep **Model–View–Template (MVT)** dengan framework **Django**.  
Setiap modul menambahkan fitur baru sesuai panduan dosen.

| Modul | Fitur Utama | Status |
|--------|--------------|---------|
| 1 | Inisialisasi project + CBV ListView + DetailView | ✅ |
| 2 | [Akan diisi setelah modul 2] | ⏳ |
| 3 | [Akan diisi setelah modul 3] | ⏳ |
| 4 | [Akan diisi setelah modul 4] | ⏳ |

---

## ⚙️ Cara Menjalankan Project
1. Clone repository ini  
   ```bash
   git clone https://github.com/<username>/framework-programming-kelurahan-23201276.git
   cd framework-programming-kelurahan-23201276/modul-1
   ```

2. Aktifkan virtual environment  
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # atau
   source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies  
   ```bash
   pip install django
   ```

4. Jalankan server  
   ```bash
   python manage.py runserver
   ```

5. Buka di browser  
   [http://127.0.0.1:8000/warga/](http://127.0.0.1:8000/warga/)

---

## 🧾 Pola Commit & Push (Contoh)
| Waktu | Commit | Keterangan |
|--------|---------|-------------|
| 09:00 | `Modul 1: init Django project data_kelurahan + app warga` | Inisialisasi project |
| 10:00 | `Modul 1: add model Warga + initial migrations` | Tambah model |
| 11:00 | `Modul 1: register Warga di admin; input data` | Setup admin |
| 13:30 | `Modul 1: implement ListView + template warga_list` | Tampilan daftar |
| 15:00 | `Modul 1: tambah DetailView + link dari daftar` | Halaman detail |
| 15:45 | `Modul 1: docs - tambah screenshot dan panduan` | Dokumentasi |

---

## 🏁 Catatan
- Setiap modul dikerjakan dalam **folder tersendiri**, tetapi tetap satu repository.  
- Commit dilakukan **bertahap dan konsisten** agar riwayat kerja mudah dibaca di GitHub.  
- Link repository dikumpulkan di grup kelas sesuai instruksi dosen.  
- Nama repository menggunakan format unik:  
  ```
  framework-programming-kelurahan-23201276
  ```

---

## 🔗 Informasi Tambahan
- Framework: **Django 5.x (LTS)**
- Bahasa: **Python 3.10+**
- Database: **SQLite3 (default Django)**
- Struktur MVT (Model–View–Template)

---

> 💬 *"Progress lebih penting dari kecepatan. Commit kecil tapi konsisten akan menunjukkan dedikasi kamu dalam belajar."*  
> — *Achmad Noercholis (disarikan dari panduan dosen)*
