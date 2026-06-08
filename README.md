# Machine Learning Workflow CI - Retraining & Model Packaging

Repositori ini berisi implementasi pipeline **Continuous Integration (CI)** untuk melatih ulang (retraining) model machine learning secara otomatis dan mengemasnya menjadi kontainer Docker siap pakai. Proyek ini dibangun sebagai bagian dari Kriteria 3 Proyek Akhir kelas **Membangun Sistem Machine Learning** (Dicoding).

## Anggota Tim / Siswa
- **Nama**: dzakwanalifi

## Struktur Repositori
```text
Workflow-CI
├── .github/workflows/
│   └── ci.yml                          # GitHub Actions ML CI/CD Pipeline
├── MLProject/
│   ├── MLProject                       # MLflow Project configuration
│   ├── conda.yaml                      # Conda runtime dependencies
│   ├── modelling.py                    # Script training / retraining
│   └── mamikos_preprocessing_dataset.csv # Dataset untuk training
└── docker_hub.txt                      # Link ke repositori Docker Hub publik
```

## Deskripsi Alur CI Pipeline
Setiap kali Anda melakukan `git push` ke cabang utama (`main`/`master`), GitHub Actions secara otomatis memicu tahapan:
1. **Checkout Code**: Mengunduh kode sumber terbaru.
2. **Environment Setup**: Mengonfigurasi Python 3.12.7 dan memasang dependencies pendukung (`mlflow`, `scikit-learn`, `xgboost`).
3. **MLflow Retraining**: Menjalankan paket MLflow Project menggunakan perintah `mlflow run MLProject` untuk melatih ulang model dengan parameter data input terbaru.
4. **Docker Packaging**: Memaketkan model yang dihasilkan menjadi sebuah kontainer Docker menggunakan fungsi `mlflow models build-docker`.
5. **Push to Registry**: Mendorong (push) Docker Image tersebut ke **Docker Hub** untuk siap didistribusikan ke server monitoring (FastAPI serving).

## Konfigurasi GitHub Secrets
Agar workflow dapat melakukan push ke Docker Hub, pastikan Anda menambahkan dua rahasia (*Secrets*) berikut pada konfigurasi repository GitHub Anda:
- `DOCKERHUB_USERNAME`: Username akun Docker Hub Anda.
- `DOCKERHUB_TOKEN`: Access Token atau Password akun Docker Hub Anda.
