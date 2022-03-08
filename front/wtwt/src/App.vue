<template>
<div id="app">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <v-app>
    <div id="nav">
        <router-link to="/">Home</router-link> |
        <router-link to="/info">Info</router-link>
    </div>
    <router-view></router-view>
    <v-main>
      
      <v-pagination :lengt='20' :value="1"></v-pagination>
    </v-main>
  </v-app>
</div>
</template>

<script>
</script>
