from rest_framework import serializers
from master.models import Kelompok

class Lab1Serializer(serializers.ModelSerializer):
  siswa = serializers.CharField(source='siswa.nama')
  siswa_nis = serializers.CharField(source='siswa.nis')
  asesor = serializers.CharField(source='asesor.nama')
  kelas_nama = serializers.CharField(source='siswa.kelas.nama')
  kelas_jurusan = serializers.CharField(source='siswa.kelas.jurusan')
  kelas_nomor = serializers.CharField(source='siswa.kelas.nomor')
  class Meta:
    model = Kelompok
    fields = [
      'id', 'siswa', 'siswa_nis', 
      'ruangan', 'no_pc', 'tanggal', 'asesor',
      'kelas_nama', 'kelas_jurusan', 'kelas_nomor'
    ]

class Lab2Serializer(serializers.ModelSerializer):
  siswa = serializers.CharField(source='siswa.nama')
  siswa_nis = serializers.CharField(source='siswa.nis')
  asesor = serializers.CharField(source='asesor.nama')
  kelas_nama = serializers.CharField(source='siswa.kelas.nama')
  kelas_jurusan = serializers.CharField(source='siswa.kelas.jurusan')
  kelas_nomor = serializers.CharField(source='siswa.kelas.nomor')
  class Meta:
    model = Kelompok
    fields = [
      'id', 'siswa', 'siswa_nis', 
      'ruangan', 'no_pc', 'tanggal', 'asesor',
      'kelas_nama', 'kelas_jurusan', 'kelas_nomor'
    ]