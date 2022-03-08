<template>
  <div id="home">
    <div class="search">
       <div class="form-floating">
        <select id="select-langue" class="form-select" aria-label="filtre par langue" v-model="filtreLangue">
          <option value="francais">Francais</option>
          <option value="anglais">Anglais</option>
          <option value="espagnol">Espagnol</option>
        </select>
        <label for="select-langue">Filtre par langue</label>
      </div>
      <div class="form-floating">
        <select id="select-genre" class="form-select" aria-label="filtre par genre" v-model="filtreGenre">
          <option value="action">Action</option>
          <option value="romantique">Romantique</option>
          <option value="sf">Science Fiction</option>
        </select>
        <label for="select-genre">Filtre par genre</label>
      </div>
      <input class="form-control" type="text" v-model="search" placeholder="rechercher film"/>
        <button button type="button" class="btn-primary" @click=" init()">Rechercher</button>
    </div>
    <!-- test v-text-field-->
     <!-- <v-text-field style="width:30%; margin:auto;" hint="Merci de confirmer votre recherche." filled v-model="search" color="#e4872c"
      label="Chercher" placeholder="Film, Series, Artistes ..." outlined></v-text-field>
    <v-btn small color="#e4872c" class=" mx-3 mt-3" @click=" init()">
      <div class="caption">CONFIRMER LA RECHERCHE</div>
    </v-btn> -->
    <v-sheet class="pa-3">
      <v-skeleton-loader class="mx-auto" max-width="300px" type="card"></v-skeleton-loader>
     <film-grid/>
    </v-sheet>
    <v-pagination color="#e4872c" v-model="page" :length="20" :value="page"></v-pagination>
  </div>
</template>

<script>
import FilmGrid from '@/components/FilmGrid.vue';
export default{
  components : {
    FilmGrid
  },  
  data : function(){
    return {
      filtreLangue: '',
      filtreGenre: '',
      search : '',
      page : 1
    }
  },
  methods: {
    init() {
      console.log("recherche :",this.search);
      console.log("filtreFilm",this.filtreGenre);
      console.log("filtreLangue",this.filtreLangue)
    }
  }
}
</script>

<style scoped lang="scss">
  .search{
    margin:auto;
    display:flex;
    justify-content: center;
    .form-select{
      margin-left:10px;
      width:200px;
    }
    .form-control{
      margin-left:10px;
      width:30%; 
      background-color:"#e4872c";
    }
    button{
       margin-left:10px;
    }
    
  }
  
</style>


