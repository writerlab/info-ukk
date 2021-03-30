<template>
  <div id="lab1">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="mb-3">
            <h1 class="text-center m-4 font-prototype">{{ ruangan }}</h1>
            <h3 class="text-muted">{{ hari }}, {{ bulan }} / {{ pukul }}</h3>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="card shadow-lg">
            <div class="card-header bg-success text-white">
              <h3>Asesor: {{ asesor }}</h3>
            </div>
            <div class="card-body">
              <table class="table table-striped table-hover table-bordered">
                <thead>
                  <tr>
                    <th width="150">NIS</th>
                    <th>NAMA</th>
                    <th width="150">NOMOR PC</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(s, id) in siswa" :key="id">
                    <td>{{ s.siswa_nis }}</td>
                    <td>{{ s.siswa }}</td>
                    <td align="center">{{ s.no_pc }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div class="card-footer">
              Total: {{ siswa.length }} peserta
            </div>
          </div>
        </div>

        <!-- <div class="col-7">
          <div class="card">
            <div class="card-header">
              Denah PC
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col">1</div>
                <div class="col"></div>
                <div class="col">2</div>
              </div>
            </div>
          </div>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Lab1",
  data() {
    return {
      ruangan: "",
      siswa: "",
      asesor: "",
      hari: "",
      bulan: "",
      pukul: "",
    };
  },
  mounted() {
    let url = "http://127.0.0.1:8000/api/lab1/";
    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        this.siswa = data
        this.asesor = data[0].asesor
        this.ruangan = data[0].ruangan
      });
  },
  created() {
    setInterval(this.waktuSekarang, 1000);
  },
  methods: {
    waktuSekarang: function () {
      const hari = ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jum`at', 'Sabtu']
      const bulan = [
        "Januari", "Februari", "Maret", "April"
      ]
      const today = new Date();
      const day = hari[today.getDay()]
      const date = today.getDate() + " " + (bulan[today.getMonth()]) + " " + today.getFullYear();
      const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      this.hari = day;
      this.bulan = date;
      this.pukul = time
    },
  },
};
</script>

<style scoped>
.bg-success {
  background-color: rgb(44, 131, 126) !important;
}

.table {
  font-size: 17px;
}

.table thead th {
  font-weight: bolder;
  text-align: center;
}
</style>
