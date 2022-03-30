

<template>
    <div>
        <div class="grid" v-if="filterMovies.length==movies.length">
            <div v-for="movie in movies" :key="movie._id">
                <v-card  class="ma-3">
                    <v-card-title>{{movie.title}}</v-card-title>
                    <div class="card-text"><b>genres : {{movie.genres}}</b></div>
                    {{showModal}}
                    <router-link :to="{path: '/film/'+movie._id}"><v-img :src="movie.image"></v-img></router-link>
                </v-card>
            </div>
        </div>
        <div class="grid" v-else>
            <div v-for="movie in filterMovies" :key="movie._id">
                <v-card  class="ma-3" >
                    <v-card-title>{{movie.title}}</v-card-title>
                    <div class="card-text"><b>genres : {{movie.genres}}</b></div>
                    <router-link :to="{path: '/film/'+movie._id}"><v-img :src="movie.image"></v-img></router-link>
                </v-card>
            </div>
        </div>
    </div>
</template>



<script>
export default {
    components :{
    },
    name: 'FilmGrid',
    props : ['movies','filterMovies'],
    data(){
        return {
            showDialog:false,
        }
    },
    mounted(){
        console.log("coucou", this.movies)
    }, 
    methods:{
       goToFilm(){
           let url = '/film/';
           this.$router.push(url);
       }
    }
}
</script>

<style scoped>

.grid{
    overflow:hidden;
    margin-top:120px;
    margin-left:100px;
    z-index:-1;
    display: flex;
    flex-wrap:wrap;
    justify-content:center start;

    width:100%;

}
 .v-card{
     width:300px;
     height: 500px;;
     position:relative;
    
 }
 .card-text{
     color: rgba(var(--v-theme-on-surface), var(--v-medium-emphasis-opacity));
    font-size: 0.875rem;
    font-weight: 400;
    letter-spacing: 0.0178571429em;
    padding:1rem;
    text-transform: none;
    transition: inherit;
    transition-property: color, opacity;
 }
 .v-card-title{
 }
.v-img{
    margin:0;
    padding:0;
    width: 100%;
    height: auto; 
}
.v-img:hover{
    cursor:pointer;
}
</style>
