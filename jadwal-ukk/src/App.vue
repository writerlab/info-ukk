<template>
  <div id="app">
    <!-- <router-link to="lab1">Lab. 1</router-link> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  background-color: #ffffff;
  font-family: 'Quicksand', sans-serif;
  font-size: 17px;
}

.fong-quicksand {
  font-family: 'Quicksand', sans-serif;
}

h1 {
  font-size: 3.9em;
}

/* .container {
  min-width: 75%;
} */
</style>
