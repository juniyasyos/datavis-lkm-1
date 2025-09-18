# Analisis Data Visualisasi Superstore - LKM 1

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-orange.svg)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-Latest-purple.svg)](https://seaborn.pydata.org)

## 📊 Deskripsi Proyek

Proyek ini merupakan implementasi Lembar Kerja Mahasiswa (LKM) 1 untuk mata kuliah Visualisasi Data. Analisis dilakukan terhadap dataset Superstore dari Kaggle dengan fokus pada tiga aspek utama:

1. **Rata-rata rating kepuasan pelanggan per kota**
2. **Jumlah penjualan per produk**  
3. **Hubungan antara penjualan dan rating kepuasan pelanggan**

## 🗂️ Struktur Proyek

```
datavis/
├── data/                     # Dataset Superstore CSV
│   └── Sample - Superstore.csv
├── notebooks/               # Notebook analisis utama  
│   └── superstore_analysis.ipynb
├── src/                     # Script Python modular
│   ├── download_data.py     # Script download dataset
│   └── data_loader.py       # Utilitas loading data
├── visualizations/          # Output visualisasi
│   ├── sales_by_category.png
│   ├── profit_trend.png
│   ├── satisfaction_by_city.png
│   ├── sales_by_product.png
│   ├── sales_vs_satisfaction.png
│   └── satisfaction_by_category.png
├── docs/                    # Dokumentasi hasil analisis
│   └── hasil_analisis.md
└── README.md               # Dokumentasi utama
```

## 📈 Hasil Analisis Utama

### Key Metrics
- **Total Sales**: $2,297,201
- **Total Profit**: $286,397  
- **Total Orders**: 5,009
- **Dataset Size**: 9,994 rows × 21 columns

### Kategori Penjualan
| Kategori | Total Sales | Persentase |
|----------|-------------|------------|
| Technology | $836,154 | 36.4% |
| Furniture | $741,999 | 32.3% |
| Office Supplies | $719,047 | 31.3% |

## 🎯 Hasil Analisis LKM

### 1. Rating Kepuasan Pelanggan per Kota
- **Top 5 Kota** dengan rating tertinggi (5.0): Andover, Yucaipa, Aberdeen, Antioch, Macon
- Simulasi rating berdasarkan profit margin menunjukkan 59% pelanggan memiliki kepuasan tinggi (rating 5)

### 2. Produk Terlaris
| Rank | Produk | Sales |
|------|--------|-------|
| 1 | Canon imageCLASS 2200 Advanced Copier | $61,599.82 |
| 2 | Fellowes PB500 Electric Binding Machine | $27,453.38 |
| 3 | Cisco TelePresence System EX90 | $22,638.48 |

### 3. Korelasi Penjualan vs Kepuasan
- **Korelasi**: -0.052 (sangat lemah negatif)
- **Insight**: Penjualan tinggi tidak berkorelasi dengan kepuasan pelanggan
- Distribusi kepuasan relatif merata di semua kategori

## 🚀 Cara Menjalankan

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn kagglehub
```

### Setup Environment
```bash
# Clone repository
git clone <repository-url>
cd datavis

# Download dataset
python src/download_data.py

# Jalankan notebook
jupyter notebook notebooks/superstore_analysis.ipynb
```

## 📋 Dependencies

- **Python 3.12+**
- **pandas**: Data manipulation dan analisis
- **numpy**: Operasi numerik
- **matplotlib**: Visualisasi dasar
- **seaborn**: Visualisasi statistik
- **kagglehub**: Download dataset dari Kaggle

## 📝 Metodologi

1. **Data Collection**: Download dataset Superstore menggunakan Kaggle API
2. **Data Preprocessing**: Cleaning, encoding handling, duplikasi removal
3. **Feature Engineering**: Simulasi rating kepuasan berdasarkan profit margin
4. **Exploratory Data Analysis**: Analisis distribusi dan trend
5. **Visualization**: Pembuatan grafik sesuai requirements LKM
6. **Insight Generation**: Ekstraksi business insights dari analisis

## 📊 Visualisasi

Semua visualisasi tersimpan dalam folder `visualizations/` dengan format PNG resolusi tinggi:

- `sales_by_category.png` - Penjualan per kategori
- `profit_trend.png` - Trend profit bulanan
- `satisfaction_by_city.png` - Rating kepuasan per kota
- `sales_by_product.png` - Top produk terlaris
- `sales_vs_satisfaction.png` - Scatter plot korelasi
- `satisfaction_by_category.png` - Box plot distribusi kepuasan

## 🔍 Insight Bisnis

1. **Technology dominates**: Kategori teknologi memiliki penjualan tertinggi
2. **Seasonal patterns**: Profit menunjukkan pola musiman dengan puncak akhir tahun
3. **Product concentration**: 10 produk teratas menyumbang porsi signifikan dari total sales
4. **Satisfaction paradox**: Produk dengan penjualan tinggi tidak selalu memiliki kepuasan tinggi

## 👨‍💻 Kontributor

- **Nama**: [Nama Mahasiswa]
- **NIM**: [NIM]
- **Mata Kuliah**: Visualisasi Data
- **Institution**: [Nama Universitas]

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik dalam rangka penyelesaian LKM Visualisasi Data.

---

📚 **Dokumentasi lengkap**: Lihat [hasil_analisis.md](docs/hasil_analisis.md) untuk pembahasan detail dengan visualisasi.