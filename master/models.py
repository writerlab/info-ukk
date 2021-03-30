from django.db import models

# KELAS
class Kelas(models.Model):
  JURUSAN_CHOICES = (
    ("TKJ", "TKJ"),
    ("RPL", "RPL"),
    ("TBSM", "TBSM"),
  )
  KETERANGAN_CHOICES = (
    ("Teknik Komputer dan Jaringan", "Teknik Komputer dan Jaringan"),
    ("Rekayasa Perangkat Lunak", "Rekayasa Perangkat Lunak"),
    ("Teknik Bisnis dan Sepeda Motor", "Teknik Bisnis dan Sepeda Motor"),
  )
  NAMA_CHOICES = (
    ("X", "X"),
    ("XI", "XI"),
    ("XII", "XII"),
  )
  NOMOR_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
  )
  nama       = models.CharField(max_length=10, choices=NAMA_CHOICES)
  jurusan    = models.CharField(max_length=30, choices=JURUSAN_CHOICES)
  nomor      = models.CharField(max_length=1, choices=NOMOR_CHOICES, null=True)
  keterangan = models.CharField(max_length=30, choices=KETERANGAN_CHOICES)

  def __str__(self):
    return self.nama


# SISWA
class Siswa(models.Model):
  JK_CHOICES = (
    ("L", "L"),
    ("P", "P"),
  )
  nis   = models.CharField(max_length=10)
  nama  = models.CharField(max_length=50)
  jk    = models.CharField(max_length=1, choices=JK_CHOICES)
  kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
  in_kelompok  = models.BooleanField(default=False)

  def __str__(self):
    return self.nama


# ASESOR
class Asesor(models.Model):
  nama = models.CharField(max_length=40)

  def __str__(self):
    return self.nama

# KELOMPOK PRAKTIK
class Kelompok(models.Model):
  RUANG_CHOICES = (
    ("Lab. 1", "Lab. 1"),
    ("Lab. 2", "Lab. 2")
  )
  siswa   = models.ForeignKey(Siswa, on_delete=models.CASCADE)
  ruangan = models.CharField(max_length=6, choices=RUANG_CHOICES)
  no_pc   = models.IntegerField()
  tanggal = models.DateTimeField()
  asesor  = models.ForeignKey(Asesor, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.siswa.nama