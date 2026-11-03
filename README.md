# Melihat Dampak Media Sosial

Proyek UAS Python dengan menu untuk mengeksplorasi dataset dampak media sosial terhadap kehidupan user.

## Link Youtube 

https://youtu.be/SrJ9_P8d-e8

## Dataset

File: 'Social_media_impact_on_life.csv' (4.500 baris, sumber: Kaggle)

Kolom yang digunakan:
- 'Age' — usia pengguna
- 'Primary_Platform' — aplikasi media sosial utama
- 'Daily_Usage_Hours' — durasi penggunaan per hari (jam)
- 'Sleep_Duration_Hours' — durasi tidur per hari (jam)
- 'Sleep_Quality_Score' — skor kualitas tidur (1–5)
- 'Late_Night_Usage' — apakah menggunakan media sosial malam hari
- 'Overall_Impact' — dampak keseluruhan (Beneficial / Neutral / Negative)

## Struktur File

```
.
├── main.py          # Menu utama program
├── models.py        # Class Record dan konstanta
├── data_loader.py   # Memuat dan mem-parsing data CSV
├── analysis.py      # Fungsi analisis dan pencarian data
├── text_utils.py    # Fungsi utilitas input dan string
├── test_project.py  # Unittest Python
└── Social_media_impact_on_life.csv
```

## Cara Menjalankan

Tidak memerlukan library eksternal, hanya Python 3.

```bash
python main.py
```

Pilihan menu:
- `[1]` Cari berdasarkan aplikasi (Instagram, TikTok, YouTube, dll.)
- `[2]` Filter berdasarkan dampak (Beneficial, Neutral, Negative)
- `[3]` Ringkasan dampak semua data
- `[0]` Keluar

## Cara Menjalankan Test

```bash
python -m unittest test_project -v
```

7 test tersebar di 5 test class: `TestModels`, `TestTextUtils`, `TestDataLoader`, `TestAnalysis`, `TestMain`.

## Konsep Pemrograman yang Digunakan

| Konsep | Contoh Lokasi |
|---|---|
| Variables | Semua file |
| Input / Output | `main.py`, `text_utils.py`, `analysis.py` |
| Operators | `models.py` (`sleep_deficit`), `analysis.py` |
| Conditionals | `models.py` (`usage_category`), `main.py`, `data_loader.py` |
| Loops | `analysis.py` (bubble sort), `main.py` (menu loop) |
| Functions | Semua file |
| Lists | `analysis.py`, `main.py`, `data_loader.py` |
| Strings | `text_utils.py` (`clean`), semua f-string |
| OOP (bonus) | `models.py` — class `Record` dengan 3 method |
