'''
total siswa: 100 orang
total day: 5 days
split siswa menjadi 5 kelompok.
20 siswa per hari.

20 Maret 2021
Zul Hilmi <zulx@smkn4-tsm.sch.id>
'''

HARI = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat')
LAB1, LAB2 = 10, 10

try:
  with open("siswa") as f:
    with open("jadwal", "w") as output:
      siswa = []
      for nama in f:
        siswa.append(nama.strip())

      kelompok = []
      total_kelompok = len(HARI)
      total_slot = LAB1 + LAB2
      i = 0 # index untuk urutan siswa dari 100
      for k in range(total_kelompok):
        kelompok.append([]) # buat list kosong didalam kelompok
        for j in range(len(siswa)):
          if j < total_slot: # cek ketersediaan slot (20)
            kelompok[k].append(siswa[i])
            i += 1

      no_pc = 0
      nomor_urut = 0
      for i in range(total_kelompok):
        output.write("#\n")
        output.write("KELOMPOK " + str(i+1) + ", HARI: " + HARI[i] + "\n")
        output.write("-----------------------------------------------\n")
        output.write("NO. | NAMA LENGKAP | NO.PC\n")
        output.write("-----------------------------------------------\n")
        for j in range(total_slot):
          if no_pc < total_slot / 2:
            no_pc += 1
          else:
            no_pc = 1
          nomor_urut += 1
          output.write(str(j+1) + ". " + kelompok[i][j] + " - PC: " + str(no_pc) + "\n")
except IOError as e:
  print(e)
