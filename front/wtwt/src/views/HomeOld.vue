
<template>
  <div id="home">
    <nav class="navbar navbar-expand-lg">
      <div class="container-fluid">
          <ul class="navbar-nav">
              <div v-for="genre in this.$store.getters.getGenres" :key="genre" >
                <li class="nav-item"> <a class="nav-link" @click="clickOnGenre(genre)">{{genre}}</a> </li>
            </div>
          </ul>
      </div>
    </nav>
    <div class="row">
      <div class="col">
        <vertical-menu class="col" 
          @langues="selectLangues($event)"
          @acteurs="selectActeurs($event)"
          @isAdult="selectAdult($event)"
          @notes="selectNotes($event)"
          @nbVotes="selectVotes($event)"/>
      </div>
      <div class="grid-container col">
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
      dd<br>
        {{ this.$store.getters.getMovies}}
        <film-grid :movies="movies" :filterMovies="filterMovies"/>
        <v-pagination color="#e4872c" v-model="page" :length="20" :value="page" @click="changePage()"></v-pagination>
      </div>

    </div>
    <div class="container">

    </div>
  </div>
</template>

<script> 
import FilmGrid from '../components/FilmGrid.vue';
// import movies from '../assets/data/movies'
import VerticalMenu from '../components/VerticalMenu.vue';
import Enum from "../utils/enum"
import MenuVue from '@/components/Menu.vue';
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
      movies : [],
      filterMovies: [],
      selectedGenre : "",
    }
  },
  mounted(){
    MenuVue.methods.setAuth()
    this.$store.dispatch('getGenres')
    console.log(this.$store.getters.getGenres)
  },
  methods: {
    changePage() {
      this.$store.dispatch('getMoviesByGenre', {
        page : this.page,
        genre : this.genre,
      }).then(() => {
        console.log("j'en ai marre", this.$store.getters.getMovies)
        // AppVue.computed.key.set()
        // console.log("=================", page, genre)
        this.$router.push({name:"Home"})
      }).catch(
        (err) => {
          this.errorAtLogin = {
            code : err.code,
            message : err.message
          }
        }
      )
    },
    clickOnGenre(genre) {
      console.log(genre)
      this.genre = genre
      // this.filterList.genre=genreId;
    
      //  this.filter(); 
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
      return 0
    },
    // changePage(){
    //   this.movies = 
    //   // console.log("filerList",this.filterList);
    //   // this.axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
    //   // console.log("page numero",this.page);
    //   //  this.axios.get('http://localhost:8585/movies/Short/' + this.page)
    //   // .then(response =>{
    //   //   this.movies = response.data
    //   //   console.log(this.movies)
    //   // } );
    // }
  }
}

</script>

<style scoped lang="scss">
  // .nav-genre{
  //   // height : 100%;
  //   // overflow-x : scroll ;
  // }
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


