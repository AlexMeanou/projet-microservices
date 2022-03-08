<template>
    <v-layout row wrap>
        <v-flex  v-for="movie in movies" :key="movie.id">
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
    props : [],
    data(){
        return {
            movies:[
                {
                    id:'1',
                    nom:'James Bond',
                    genre : 'action',
                    url :"https://m.media-amazon.com/images/I/51GSe7yqQ-L._AC_.jpg"
                },
                {
                    id:'2',
                    nom:'Peter Pan',
                    genre : 'aventure',
                    url :"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz1_902QZeJ_I_wVR-b9cN9Webts5BS0pbbBELKOMP4ply0hTB1DF8gBDyjs3AlWOZmMQ&usqp=CAU"
                },
                 {
                    id:'3',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
                {
                    id:'4',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
                 {
                    id:'3',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
                 {
                    id:'5',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
                 {
                    id:'6',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
                 {
                    id:'7',
                    nom:'Pirates des Caraibes',
                    genre : 'aventure',
                    url :"https://fr.web.img4.acsta.net/medias/nmedia/18/35/07/46/affiche2.jpg"
                },
            ]
        }
    }
}
</script>

<style scoped>
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
