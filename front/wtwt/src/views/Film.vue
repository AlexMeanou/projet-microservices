<template style="color:white">
<div class="film">
    <v-card  class="ma-3">
        <v-card-title>{{movie.title}}</v-card-title>
        <div class="card-text"><b>genres : {{movie.genres}}</b></div>  
        <v-img :src="movie.image"></v-img>             
    </v-card>
    <div class="description">
        <h5>Synopsis</h5>
       <p>
         gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
        </p>
        <div class="notation">
            <v-img v-for="n in 5" :key="n" class="star" src="../assets/data/images/star.png"></v-img>
        </div>
          <div class="note">
                <p>note moyenne : 3.5</p>
                <p>nombre de vote : 500</p>
        </div>
    </div>
    <v-list class="actors">
        <h5>Liste des acteurs :</h5>
        <v-list-item v-for="actor in actors" :key="actor.value">
            {{actor.text}}
        </v-list-item>
    </v-list>
</div>
</template>

<script>
import movies from '../assets/data/movies'
export default {
    components :{
    },
    name: 'Film',
    data(){
        return {
            id:0,
            movie : null,
            actors :[
                {text:"Leonardo Decaprio",value:1},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2},
                {text:"Brad Pitt",value:2}, 
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
                {text:"Brad Pitt",value:2},  
            ]
        }
    },
     created(){
        this.id=this.$route.params.id;
        this.movie= movies.find(x=>x._id==this.id);
    },
    mounted(){
    }
    ,
    methods:{
    }

}
</script>
<style scoped lang="scss">
.film{
    display: flex;
    gap:30px;
    justify-content: center;
    margin-top:70px;
    align-items:flex-start;
}
.v-card{
   
     width:500px;
     height: 700px;
     position:relative;
    .v-img{
        margin:0;
        padding:0;
        width: 100%;
        height: auto; 
    }
     .card-text{
        font-weight: 400;
        letter-spacing: 0.0178571429em;
        padding:1rem;
    }
 }
 .description{
    font-weight: 400;
    margin-left:2rem;
    letter-spacing: 0.0178571429em;
    padding:1rem;
    max-width:500px;
    min-width:100px;
    h5{
    }
    p{
        margin-top:10%;
        word-wrap: break-word;

    }
    .notation{
        display:flex;
        justify-content: flex-start;
        align-items:center;
        width:50%;
        margin-top:50%;
        .star{
        }
        
    }
    .note{
        p{
            margin-top:15px;
            text-align: left;
            font-size:20px;
        }
        
    }
    .actors{
        margin-left:6rem;
        h5{
        
        }
    }
 }
 
 </style>