<template>

    <div>
        <div class="grid" v-if="filterMovies.length==movies.length">
            <div v-for="movie in movies" :key="movie._id">
                <v-card  class="ma-3" >
                    <v-card-title>{{movie.title}}</v-card-title>
                    <div class="card-text"><b>genres : {{movie.genres}}</b></div>
                    <div class="card-text"><b>langues : {{movie.languages}}</b></div>
                    <v-img :src="movie.image" ></v-img>    
                </v-card>
            </div>
        </div>
        <div class="grid" v-else>
            <div v-for="movie in filterMovies" :key="movie._id">
                <v-card  class="ma-3" >
                    <v-card-title>{{movie.title}}</v-card-title>
                    <div class="card-text"><b>genres : {{movie.genres}}</b></div>
                    <div class="card-text"><b>langues : {{movie.languages}}</b></div>
                    <v-img :src="movie.image" ></v-img>    
                </v-card>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FilmGrid',
    props : ['movies','filterMovies'],
    data(){
        return {}
    },
    mounted(){
        console.log("filter",this.filterMovies);
    },
    methods:{

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
</style>
