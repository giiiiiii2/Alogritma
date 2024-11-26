
# Algoritma
C_Anggita Setiawati_F55123092

# QUIZ 2
<!-- Anggita Stiawati_F55123092 -->

# Hasil analisisnya
Data:
50 bilangan acak dalam rentang [0, 100].
Seed: 40
Metode:
Metode Naive (Bubble Sort)
Metode Conquer (Merge Sort)

# Penjelasan Analisis Best Case:
Metode Naive (Bubble Sort):
Pada kondisi terbaik, array sudah terurut, sehingga algoritma tidak melakukan pertukaran apapun. Proses sorting menjadi lebih cepat karena algoritma dapat menghentikan iterasi lebih awal berkat flag swapped yang tetap False.
Jumlah Perbandingan: 
Hanya diperlukan sebanyak n-1 perbandingan (49 kali jika array terdiri dari 50 elemen).
Jumlah Pertukaran: 
Tidak ada pertukaran yang terjadi (swaps = 0).
# Kompleksitas:
Best Case Time Complexity:
    O(n)Kompleksitas terbaik terjadi ketika array sudah terurut, dan algoritma hanya memerlukan satu iterasi untuk memeriksa data.
Space Complexity:
    O(1) Bubble Sort menggunakan ruang tambahan yang konstan karena hanya membutuhkan beberapa variabel tambahan untuk proses perbandingan dan pertukaran.

# Metode Conquer (Merge Sort):
Pada kondisi terbaik, meskipun data sudah terurut, Merge Sort tetap membagi array menjadi subarray yang lebih kecil dan menggabungkannya kembali. Proses ini tidak tergantung pada urutan data.
Jumlah Perbandingan:
Tetap n log(n) untuk 50 elemen, karena pembagian dan penggabungan tetap terjadi meskipun data sudah terurut.
Jumlah Pertukaran:
Tidak ada pertukaran, karena proses penggabungan elemen dilakukan dengan cara menggabungkan subarray tanpa melakukan pertukaran elemen.
# Kompleksitas:
  Best Case Time Complexity: O(n log n)
    Meskipun data sudah terurut, algoritma tetap melakukan pembagian dan penggabungan, sehingga waktu yang dibutuhkan tetap mengikuti pola O(n log n)
  Space Complexity: O(n)
    Merge Sort membutuhkan ruang tambahan untuk menampung array hasil pembagian dan penggabungan.

