# Face Recognition

## Pembukaan dan Penjelasan

Program ini adalah backend dari sistem pengenalan wajah berbasis AI. Backend bertanggung jawab untuk memproses data, menjalankan algoritma pengenalan wajah, serta menyediakan API yang dapat diakses oleh aplikasi frontend atau sistem lain untuk melakukan identifikasi dan verifikasi identitas melalui gambar. Saya telah mencari model dan libary yang cocok untuk dapat digunakan dalam aplikasi ini, saya menanyakan 3 AI chat, seperti ChatGpt, Gemini, dan Claude. Model yang saya gunakan untuk feature extractor menggunakan **ARCFace R100** sebuah model pretrained dari insightface yang memiliki akurasi yang cukup untuk feature extarctor, untuk face detection saya menggunakan MTCNN yang ringan dan cukup bagus untuk deteksi.

model, library, database yang digunakan:
- **Model Extract Feature:** ARCFace R100.
- **Face Detection:** MTCNN.
- **Api Framework:** Fastapi.
- **Database:** PostgreSQL.

Gambar flow: https://drive.google.com/file/d/1TpSHYGyxR4xM_fwtYAahqYUAtKg1F-ox/view?usp=sharing

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

Wajib menggunakan aplikasi untuk request api seperti **Postman**.</br>
Jika belum punya postman bisa lihat swagger di /docs.

**Penting**: Swagger saya allow karena untuk kepentingan development. jika sudah masuk production wajib dimatikan.

### Register ###
access: http://127.0.0.1:8000/api/face/register

Jika mau mendaftarkan wajah. siapkan foto untuk di save, di rekomendasi kan foto yang tegap dan mata menghadap kamera dan jangan membelakangi cahaya. 

Untuk memasukan data gunakan tipe form di kolomn body, isi key dengan 'name' dan masukan nama yang akan di daftar, dan tambah baris lagi isi key dengan 'file' dan masukan gambar, extensi gambar yang disupport png dan jpg.

response dari backend jika berhasil:
```bash
{
    "message": "Face registered successfully"
}
```
jika error akan muncul pesan tergantung error nya.

### Recognition ###
access: http://127.0.0.1:8000/api/face/recognition

Jika mau melakukan pencocokan wajah dengan database, siapkan foto yang mau di cocok. rekomendasi foto hampir sama dengan Register.

Untuk memasukan data gunakan tipe form di kolomn body, isi key dengan 'file' dan masukan gambar, extensi gambar yang disupport png dan jpg.

response dari backend jika berhasil:
```bash
{
    "match": true, #berhasil di temukan
    "name": "Rangga2", #nama wajah
    "id_face": "f7b9a525-b024-4e7d-a7b3-0adf63c4d4e4", #id wajah
    "score": 0.7245 #kecocokan dengan wajah yang ada di database
}
```
jika error akan muncul pesan tergantung error nya.

### Delete
access: http://127.0.0.1:8000/api/face/recognition/id-yang-mau-di-delete

jika mau menghapus gambar wajah dari database bisa menggunakan delete. cara menggunakanya ambil id_face dan paste di akhir endpoints.

response dari backend jika berhasil:
```bash
{
    "message": "Face with ID 52d697c0-f7da-42bc-b18a-5e31c0badf89 has been deleted successfully"
}
```

### Get ALL Face
access: http://127.0.0.1:8000/api/face/

method: get

jika mau melihat dan data apa saja yang ada di database bisa langsung get saja.

response dari backend jika berhasil:
```bash
[
    {
        "id_face": "8aed58c1-3a84-4145-9f7d-0d4488a21f66",
        "name": "Jack",
        "image": "Base64 Image" #gambar yang di save adalah base64 bukan untuk recognition emg untuk di tampilkan.
    },
    {
        "id_face": "f7b9a525-b024-4e7d-a7b3-0adf63c4d4e4",
        "name": "Rangga2",
        "image": "Base64 Image"
    },
    {
        "id_face": "bcd81e1a-cfcf-4685-8698-5b409cf39ed1",
        "name": "Alex",
        "image": "Base64 Image"
    }
]
```

## Penutup
Terima kasih telah melihat code aplikasi saya. 