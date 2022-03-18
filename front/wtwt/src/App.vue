<template>
<div id="app">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <v-app>
    <Menu/>
    <router-view></router-view>
  </v-app>
</div>
</template>
<script>
import axios from 'axios';
import Menu from "./components/Menu.vue"
export default {
  components : {  
    Menu
  }, 
    data(){
        return {
          isLogin : false
        } 
    },
    mounted(){
         axios.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))

  },
  methods:{

    }
}
</script>

<style scoped lang="scss">
</style>
