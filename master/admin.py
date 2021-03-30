from django.contrib import admin
from .models import Kelas, Siswa, Kelompok, Asesor

class KelasAdmin(admin.ModelAdmin):
  list_display  = ['nama', 'jurusan', 'nomor', 'keterangan']
  
class SiswaAdmin(admin.ModelAdmin):
  list_display  = ['nis', 'nama', 'jk', 'kelas']
  list_filter   = ['kelas', 'kelas__nomor']
  search_fields = ['nis', 'nama']
  list_per_page = 30

class KelompokAdmin(admin.ModelAdmin):
  list_display  = ['siswa', 'ruangan', 'no_pc', 'tanggal', 'asesor']
  list_filter   = ['ruangan', 'tanggal', 'siswa__kelas__nomor', 'asesor']
  search_fields = ['siswa__nis', 'siswa__nama']
  list_per_page = 30

class AsesorAdmin(admin.ModelAdmin):
  list_display  = ['nama']
  list_per_page = 20


admin.site.register(Kelas, KelasAdmin)
admin.site.register(Siswa, SiswaAdmin)
admin.site.register(Kelompok, KelompokAdmin)
admin.site.register(Asesor, AsesorAdmin)