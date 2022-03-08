<template>
    <v-layout >
        <v-flex v-for="movie in movies" :key="movie.id">
            <v-card  class="ma-3" width="300" height="500" >
                 <v-card-title>{{movie.nom}}</v-card-title>
                <div class="card-text"><b>genre : {{movie.genre}}</b></div>
                <v-img :src="movie.url" ></v-img>
               
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
export default {
    name: 'FilmGrid',
    props : ['page','movies'],
    data(){
        return {}
    },
    mounted(){
        console.log("ok",this.page);
    },
    methods:{

    }
}
</script>

<style scoped>

.v-layout{
    flex-wrap:wrap;
}
 .v-card{
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
