<template>
<div id="app">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <v-app >
    <Menu class="menu"/>
    <router-view :key="$route.fullPath" />
  </v-app>
</div>
</template>
<script>
// import { ref } from "vue";
import Menu from "./components/Menu.vue"
export default {
  components : {  
    Menu
  }, 
    data(){
        return {
          // refreshKey: ref(0),
        } 
    },
    mounted(){
      // if (this.$store.getters.isLogged) {
      //   this.forceRerender()
      // }

  },
  // computed: {
  //   key: {
  //     get(){
  //       return this.refreshKey;
  //     },
  //     set(id){
  //       this.refreshKey = id;
  //     }
  //   }
  // },
  methods:{
    forceRerender() {
      this.componentKey += 1;
    }
  }
}
</script>

<style scoped lang="scss">

html{
  background: black;
  }

.menu{
  display: block;
}
</style>
