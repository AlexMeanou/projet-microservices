<template>
    <section>
         <div class="navbar" id="nav">
             <a class="home-link"><router-link to="/"> Home</router-link></a>
            <a class="genre-link" @change="filterAction()"> Action</a>
            <a class="genre-link"> Romantique</a>
            <a class="genre-link"> Science Fiction</a>
            <a class="genre-link"> Anime</a>
            <a class="genre-link"> Comedie</a>
            <a class="connexion-link"><router-link to="/connexion">Connexion</router-link></a>
        </div>
    </section>
</template>

<script>
export default {
    name: "Menu",
    data(){
        return {}
    },
    mounted(){
        console.log("ok",this.page);
    },
    methods:{
        filterAction(){
            // component('Home').filterAction();
        }
    }
}
</script>

<style scoped lang="scss">
    .navbar{
        justify-content:space-between;
        a{
            text-decoration: none;
            font-size:18px;
            color:black;
        }
        a:hover{
            color:#cc6600;
        }
        
        .home-link{
            margin-left:10px;
        }
        .connexion-link{
            margin-right:20px;
        }
        .genre-link{
            
        }
        
        
  }
</style>