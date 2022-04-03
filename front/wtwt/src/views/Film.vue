<template style="color:white">
<div class="film" v-if="is_load">
    <v-card  class="ma-3">
        <v-card-title>{{movie.title}}</v-card-title>
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
export default {
    components :{
    },
    name: 'Film',
    data(){
        return {
            id:0,
            is_load : false,
            movie : null,
            
        }
    },
    computed() {
        this.id=this.$route.params.id;
        this.movie = this.$store.getters.getMovie
        this.reloadMovie()
        this.is_load = true
    },
    created(){
    }

    ,
    methods:{
        reloadMovie() {
        this.$store.dispatch('getMovie', {
                id: this.id,
                
            }).then(() => {
                this.movie = this.$store.getters.getMovie
                
            }).catch(
                (err) => {
                    this.errorAtLogin = {
                        code: err.code,
                        message: err.message
                    }
                }
            )
        }
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