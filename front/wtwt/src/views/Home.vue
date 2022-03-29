
<template>
  <div id="home">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
          <ul class="navbar-nav">
            <li class="nav-item"> <a class="nav-link" @click="clickOnGenre(Enum.genre.ACTION)">Action</a> </li>
            <li class="item"><a class="nav-link" @click="clickOnGenre(Enum.genre.COMEDIE)">Commédie</a></li>
            <li class="nav-item"><a class="nav-link" @click="clickOnGenre(Enum.genre.ANIME)">Anime</a></li>
            <li class="nav-item"> <a class="nav-link"  @click="clickOnGenre(Enum.genre.ROMANTIQUE)">Romantique</a> </li>
            <li class="nav-item"><a class="nav-link" @click="clickOnGenre(Enum.genre.SCIENCEFICTION)">Science Fiction</a> </li>
            <li class="nav-item">
              <select class="nav-link selected-genre" aria-label="genre" v-model="selectedGenre" @change="selectGenre()">
                <option v-bind:value="Enum.genre.TOUS" selected>Tous les genres</option>
                <option v-bind:value="Enum.genre.ACTION">Action</option>
                <option v-bind:value="Enum.genre.COMEDIE">Comedie</option>
                <option v-bind:value="Enum.genre.ANIME">Anime</option>
                <option v-bind:value="Enum.genre.ROMANTIQUE">Romantique</option>
                <option v-bind:value="Enum.genre.SCIENCEFICTION">Science Fiction</option>
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

    <div class="container">
      <vertical-menu class="col" 
        @langues="selectLangues($event)"
        @acteurs="selectActeurs($event)"
        @isAdult="selectAdult($event)"
        @notes="selectNotes($event)"
        @nbVotes="selectVotes($event)"/>

      <div class="grid-container col">
        <film-grid :movies="movies" :filterMovies="filterMovies"/>
        <v-pagination color="#e4872c" v-model="page" :length="20" :value="page" @click="changePage()"></v-pagination>
      </div>
    </div>
  </div>
</template>

<script> 
import FilmGrid from '../components/FilmGrid.vue';
import movies from '../assets/data/movies'
import VerticalMenu from '../components/VerticalMenu.vue';
import Enum from "../utils/enum"
export default{
  name:'Home',
  components : {
    FilmGrid,
    VerticalMenu,
  },  
  data : function(){
    return {
      Enum,
      filterList : {
        genre : 0,
        langues : [],
        acteurs : [],
        isAdult:false,
        notes : [],
        nbVotes : 0,
      },
      page : 1,
      movies,
      filterMovies:movies,
      selectedGenre : "",
    }
  },
  mounted(){
  },
  methods: {
    clickOnGenre(genreId) {
      this.filterList.genre=genreId;
    
       this.filter();
    },
    selectGenre(){
      this.filterList.genre=this.selectedGenre;
       this.filter();
    },
    search() {
      console.log("recherche :",this.filterSearch);
    },
    selectLangues(langues){
      this.filterList.langues=langues;
      this.filter();
    },
    selectActeurs(acteurs){
      this.filterList.acteurs=acteurs; 
      this.filter();
    },
    selectNotes(notes){
      this.filterList.notes=notes; 
      this.filter();
    },
    selectVotes(nbVotes){
      this.filterList.nbVotes=nbVotes; 
      this.filter();
    },
    selectAdult(isAdult){
      this.filterList.isAdult=isAdult; 
      this.filter();
    },
    filter(){
      console.log("filter",this.filterList);
      this.filterMovies = this.movies.filter(x=>{
        if (this.filterList.genre!==Enum.genre.TOUS){
            return x.genres==this.filterList.genre
        }
        else{
          return true;
        }
      });
      
      this.filterMovies=this.filterMovies.filter(x=>
          this.filterList.langues.every(l=>{
            return x.languages.includes(l);
      }));
      
    },
    filterGenre(){

    },
    changePage(){
      console.log("filerList",this.filterList);
      this.axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
      console.log("page numero",this.page);
       this.axios.get('http://127.0.0.1:51414/movies/' + this.page)
      .then(response =>{
        this.movies = response.data
        console.log(this.movies)
      } );
    }
  }
}
</script>

<style scoped lang="scss">
  .navbar{
    position:fixed !important;
    padding-top:70px;
    padding-bottom:20px;
    background-color: black;
    width:100%;
    z-index:30;
  }
  .nav-link{
    color:white !important;
  }
  .select-genre{
    text-decoration : none !important;
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
  
</style>


