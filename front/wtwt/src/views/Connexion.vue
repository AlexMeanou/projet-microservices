

<template>
<div class="connexion">
  <div class="form-group">
    <h2 class="title">Connectez vous !</h2>
    <div>
      <label for="name">nom</label>
      <input class="form-control" type="text" v-model="name" id="name">
    </div>
    <div class="invalid"> Please provide a valid city </div>
    <div>
      <label for="password">mot de passe</label>
      <input class="form-control" type="password" v-model="password" id="password">
    </div>
    <button type="submit" class="btn btn-primary" :disabled="!isValid()" @click="connect()">Se connecter</button>
    <p>Pas encore inscrit ? <a class="link"><router-link to="/inscription">S'inscrire</router-link></a> </p>
  </div>
  <font-awesome-icon icon="fa-solid fa-user-secret"/>
</div>

<!-- <div class="form-floating">
        <select id="select-genre" class="form-select" aria-label="filtre par genre" v-model="filterGenre" @change="filter()">
          <option value="action">Action</option>
          <option value="romantique">Romantique</option>
          <option value="sf">Science Fiction</option>
        </select>
        <label for="select-genre">Filtre par genre</label>
  </div> -->
</template>

<script>
/* import the fontawesome core */
import users from '../assets/data/users'
export default {
  name: "Connexion",
  components :{
  },
  data(){
    return {
        name: '',
        password: '',
        users,
    }
  },
  methods:{
    isLoginCorrect(){
      // On check si le nom d'utilisetur et le mdp crrecspondent
      return this.users.find(x=>x.name==this.name && x.password==this.password);
    },
    isNotEmpty(){
      return this.name && this.password;
    },
    isValid(){
      return this.isNotEmpty() && this.isLoginCorrect();
    }
  }
}
</script>

<style lang="scss">

.form-group{
  width:400px;
   margin-top:40px;
  margin-right:auto;
  margin-left:auto;
  .title{
    text-align:center;
    margin-bottom:20px;
  }
  p{
    margin-top:10px;
    text-align:center;
    .link{
      margin-left:10px;
      color:blue;
      text-decoration: none;
    }
  }
  
  .link:hover{
    text-decoration:underline;
  }
  .form-control{
    margin-bottom:10px;
  }
}


</style>