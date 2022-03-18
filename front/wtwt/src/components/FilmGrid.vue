<template>
    <v-layout >
        <v-flex v-for="movie in movies" :key="movie._id">
            <v-card  class="ma-3" >
                 <v-card-title>{{movie.title}}</v-card-title>
                <div class="card-text"><b>genres : {{movie.genres}}</b></div>
                <v-img :src="movie.image" ></v-img>
               
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
    z-index:-1 !important;
    margin-top:30px;
    margin-left:100px;
    flex-wrap:wrap;
    justify-content: space-evenly;
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
