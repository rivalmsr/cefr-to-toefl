# TOEFL — Pool tema kanonik (rotasi `/toefl`)

Daftar tema **tetap** per subtype berteks. Dipakai `scripts/toefl_themes.py` untuk memilih tema
yang **belum pernah / paling lama tidak** dipakai (LRU atas seluruh baris `TOEFL` di
`progress/history.md`). `scripts/check-kb.py` menolak label di luar daftar ini.

- **Tambah tema = tambah di tabel ini** (ID huruf kecil, kata dipisah `-`), bukan di skill.
- ID = **bidang/situasi**, bukan topik spesifik. Topik spesifik (mis. *lebah*) ditulis dalam
  kurung di history: `RD-words=biologi-hewan (lebah)`. Variasi tetap di detail (tokoh, tempat,
  angka), **bukan** dengan mengganti tema.
- `LS-response` dan `WR-build` tidak punya tema (1 kalimat per soal) → bebas, tapi variasikan.
- Alasan: proyek Jepang (`/jlpt`) membuktikan tema yang dipilih model sendiri ping-pong di 2–3
  topik dan label bebas menyamarkan pengulangan (lihat `docs/perbaikan-kb.md` 2026-11-09).

| Subtype | Tema (ID kanonik) |
|---|---|
| `RD-words` | `biologi-hewan` · `biologi-tumbuhan` · `ekologi` · `geologi` · `astronomi` · `kimia` · `fisika` · `kesehatan-kedokteran` · `psikologi` · `sosiologi` · `sejarah` · `arkeologi` · `ekonomi` · `linguistik` · `seni-musik` · `arsitektur` · `teknologi` · `pertanian` · `iklim-cuaca` · `oseanografi` |
| `RD-daily` | `email-dosen` · `pengumuman-kampus` · `menu-kantin` · `jadwal-transport` · `iklan-kamar` · `jam-buka` · `poster-acara` · `aturan-asrama` · `chat-teman` · `formulir-pendaftaran` · `brosur-klub` · `fasilitas-olahraga` |
| `RD-academic` | `biologi-hewan` · `biologi-tumbuhan` · `ekologi` · `geologi` · `astronomi` · `kimia` · `fisika` · `kesehatan-kedokteran` · `psikologi` · `sosiologi` · `sejarah` · `arkeologi` · `ekonomi` · `linguistik` · `seni-musik` · `arsitektur` · `teknologi` · `pertanian` · `iklim-cuaca` · `oseanografi` |
| `LS-conversation` | `perpustakaan` · `registrasi-kuliah` · `kantor-dosen` · `laboratorium` · `asrama` · `kafetaria` · `toko-buku` · `beasiswa` · `magang` · `kelompok-belajar` · `layanan-kesehatan` · `pusat-karier` · `klub-mahasiswa` |
| `LS-announcement` | `perubahan-jadwal` · `asrama` · `acara-kampus` · `aturan-perpustakaan` · `perbaikan-gedung` · `transport-kampus` · `pendaftaran` · `keselamatan` · `fasilitas-olahraga` · `kafetaria` |
| `LS-talk` | `biologi-hewan` · `biologi-tumbuhan` · `ekologi` · `geologi` · `astronomi` · `kimia` · `fisika` · `kesehatan-kedokteran` · `psikologi` · `sosiologi` · `sejarah` · `arkeologi` · `ekonomi` · `linguistik` · `seni-musik` · `arsitektur` · `teknologi` · `pertanian` · `iklim-cuaca` · `oseanografi` |
| `WR-email` | `minta-perpanjangan` · `keluhan-layanan` · `undangan` · `minta-informasi` · `minta-maaf` · `minta-rekomendasi` · `ganti-jadwal` · `terima-kasih` |
| `WR-discussion` | `teknologi-pendidikan` · `lingkungan` · `kerja-jarak-jauh` · `media-sosial` · `transportasi-kota` · `kesehatan-publik` · `konsumsi-belanja` · `budaya-pariwisata` · `kebijakan-kampus` |
| `SP-interview` | `kebiasaan-belajar` · `kota-asal` · `teknologi-sehari-hari` · `hobi` · `makanan` · `perjalanan` · `pekerjaan-masa-depan` · `lingkungan` · `pertemanan` |
