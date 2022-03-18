<template>
    <section>
         <div class="navbar menu" id="nav">
             <a class="home-link"
                ><router-link to="/">
                    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
                        <path fill-rule="evenodd" d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"/>
                    </svg>
                </router-link>
            </a>
             <a class="preference-link">
                 <router-link to="/preference">
                    <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-gear-fill" viewBox="0 0 16 16">
                        <path d="M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z"/>
                    </svg>
                 </router-link>
            </a>
            <a v-if="!isLogin" class="connexion-link">
                <router-link to="/connexion">
                    Connexion
                    <!-- <svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
                        <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>
                        <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>
                    </svg> -->
                </router-link>
            </a>
             <a v-if="isLogin" class="connexion-link" @click="logout()">
                <router-link to="/">
                    Deconnexion
                </router-link>
            </a>
        </div>
    </section>
</template>

<script>
export default {
    name: "Menu",
    data(){
        return {
            isLogin :false
        }
    },
    mounted(){
        if(localStorage.name){
            this.isLogin=true;
        }
    },
    methods:{
        logout(){
            localStorage.removeItem('name');
            console.log("localstorage",localStorage);
            this.$router.push('/');
            this.$router.go();
        }
    }
}
</script>

<style scoped lang="scss">
    .menu{
        background-color: black;
        justify-content:space-between;
        position:fixed;
        z-index: 6;
        width:100%;
        i{
            color:white;
        }
        
        a{
            color:white;
            text-decoration: none;
            font-size:18px;
        }
        a:hover{
            text-decoration: underline;
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