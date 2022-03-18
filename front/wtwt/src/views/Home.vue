
<template>
  <div id="home">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
          <ul class="navbar-nav">
            <li class="nav-item"> <a class="nav-link" @onclick="filterAction()">Action</a> </li>
            <li class="item"><a class="nav-link" @onclick="filterComedie()">Commédie</a></li>
            <li class="nav-item"><a class="nav-link" @onclick="filterAnime()">Anime</a></li>
            <li class="nav-item"> <a class="nav-link"  @onclick="filterRomantique()">Romantique</a> </li>
            <li class="nav-item"><a class="nav-link" @onclick="filterScienceFiction()">Science Fiction</a> </li>
            <li class="nav-item"><select class="nav-link" aria-label="genre" @change="changeGenre()">
                <option selected>Tous les genres</option>
                <option value="action">Action</option>
                <option value="comedie">Comedie</option>
                <option value="anime">Anime</option>
                <option value="anime">Romantique</option>
                <option value="sf">Science Fiction</option>
              </select>
            </li>
            <li>
              <form style="margin-left:10px" class="d-flex">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn" type="submit">Search</button>
              </form>
            </li>
          </ul>
      </div>
    </nav>

    <div class="main-container">
      <vertical-menu/>
      <div class="grid-container">
        <film-grid :page="page" :movies="movies"/>
        <v-pagination color="#e4872c" v-model="page" :length="20" :value="page" @click="changePage()"></v-pagination>
      </div>
    </div>
  </div>
</template>

<script> 
import FilmGrid from '../components/FilmGrid.vue';
import movies from '../assets/data/movies'
import VerticalMenu from '../components/VerticalMenu.vue';
export default{
  name:'Home',
  components : {
    FilmGrid,
    VerticalMenu,
  },  
  data : function(){
    return {
      filterLangage: '',
      filterGenre: '',
      filterSearch : '',
      page : 1,
      movies,
    }
  },
  mounted(){
  },
  methods: {
    filter() {
      // on envoit les differents filtres et le numero de page pour chercher dans l'api les n premiers films correspondant à la langue
      console.log("filtre langue :",this.filterLangage);
      console.log("filtre genre",this.filterGenre);
      console.log("page numero",this.page);
    },
    filterAction(){
      console.log(" on renvoit un json de film triés par action");
    },
    filterComedie(){
         console.log(" on renvoit un json de film triés par comédie");
    },
    filterAnime(){
        console.log(" on renvoit un json de film triés par anime");
    },
    filterRomantique(){
        console.log(" on renvoit un json de film triés par romantique");
    },
    filterScienceFiction(){
        console.log(" on renvoit un json de film triés par science fiction");
    },
    search() {
      console.log("recherche :",this.filterSearch);
    },
    changePage(){
      console.log("page numero",this.page);
    }
  }
}
</script>

<style scoped lang="scss">
  .navbar{
    position:fixed !important;
    padding-top:70px;
    background-color: black;
    width:100%;
  }
  .nav-link{
    color:white !important;
  }
  .nav-link:hover{
    text-decoration: underline;
  }

  .btn{
    color:white;
    border-color:white;
  }
  .btn:hover{
    font-weight: 450;
    color:white;
  }
  .main-container{
    display:flex;
    justify-content: space-evenly;
  }
  
</style>


