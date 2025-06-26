# Face Recognition

Program ini adalah backend dari sistem pengenalan wajah berbasis AI. Backend bertanggung jawab untuk memproses data, menjalankan algoritma pengenalan wajah, serta menyediakan API yang dapat diakses oleh aplikasi frontend atau sistem lain untuk melakukan identifikasi dan verifikasi identitas melalui gambar atau video. Program ini tidak memiliki antarmuka pengguna langsung, melainkan berfungsi sebagai server yang menangani permintaan dari klien.

fitur yang ada di aplikasi ini:
- **Deteksi Wajah Otomatis:** Mengidentifikasi wajah secara real-time dari kamera atau gambar yang diunggah.
- **Pengenalan Individu:** Mencocokkan wajah dengan database untuk verifikasi identitas.
- **Antarmuka Pengguna Sederhana:** Mudah digunakan oleh pengguna tanpa keahlian teknis.
- **Keamanan Data:** Data wajah disimpan dan diproses dengan memperhatikan privasi dan keamanan.

Aplikasi ini cocok digunakan untuk absensi, sistem keamanan, atau kebutuhan identifikasi lainnya.

**Penting**: Jangan lupa import database dari repo ini. Jangan lupa ubah password dan nama user nya di /apps/config.py. Saya menggunakan RDBMS PostgreSQL 17.

## Cara Menjalankan Code Ini di Docker(Sangat di sarankan)

Build docker image nya terlebih dahulu :

**Penting** : Cek kembali link database nya di /app/config.py.

```bash
docker build -t face-re .
```

jika sudah build, langsung run docker image nya:

```bash
docker run -it --rm -p 8000:8000 face-re
```
## Cara Menjalankan Code Ini di Metal/Langsung

Disaran kan menggunakan enviroment python.</br>
**Penting** : Jangan lupa ubah host.docker.internal menjadi localhost/ip/domain database kalian.

**install semua libray yang di butuhkan.**

windows:
```bash
pip install -r requirements.txt
```

linux:
```bash
pip3 install -r requirements.txt
```
**Jalankan run.py.**

```bash
python run.py
```
### fix jika terjadi error ###

Jarang terjadi tapi kadang muncul, link database nya tidak terbaca, jika mengalami itu pergi ke **/app/db_model/database.py** dan ubah:

```bash
SQLALCHEMY_DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI #hapus ini

engine = create_engine('ganti dengan link database mu')
```

## Cara Menggunakan Code Ini ##