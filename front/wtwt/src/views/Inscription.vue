
<template>
<div class="inscription">
  <div class="form-group">
    <div v-if="numPage==1" class="step-1">
      <h2 class="title">Inscrivez vous !</h2>
      <div>
        <label for="name">nom</label>
        <input class="form-control" type="text" v-model="name" id="name">
        <div v-if="!isNameExists()" class="invalid"> Entrez un nom !</div>
      </div>
      <div>
        <label for="password">mot de passe</label>
        <input class="form-control" type="password" v-model="password" id="password">
      </div>
      <div>
        <label for="password">confirmer le mot de passe</label>
        <input class="form-control" type="password" v-model="password2" id="password2">
      </div>
    </div>

    <div v-if="numPage==2" class="step-2">
      <h2 class="title">Vos préférences !</h2>
      <div>
        <label for="name">test</label>
        <input class="form-control" type="text" v-model="name" id="name">
      </div>
      <div>
        <label for="password">test</label>
        <input class="form-control" type="password" v-model="password" id="password">
      </div>
      <div>
        <label for="password">test</label>
        <input class="form-control" type="password" v-model="password2" id="password2">
      </div>
    </div>
    <button v-if="numPage==1" type="submit" class="btn btn-primary" :disabled="!isForm2Valid()" @click="numPage++">Continuer</button>
     <button v-else type="submit" class="btn btn-primary" :disabled="!isForm2Valid()" @click="subscribe()">S'inscrire</button>
    <p>Déja inscrit ? <a class="link"><router-link to="/connexion">Se connecter</router-link></a> </p>
    <div v-if="!isPasswordsEqual() && password && password2" class="alert alert-danger" role="alert"> Les mots de passes ne correspondent pas !</div>
  </div>

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
export default {
    name: "Inscription",
    components :{
    },
    data(){
        return {
            name: '',
            password: '',
            password2: '',
            numPage:1,
        }
    },
    methods:{
        isNotEmpty(){
            return this.name && this.password && this.password2;
        },
        isPasswordsEqual(){
            return this.password == this.password2;
        },
        isNameExists(){
            return true;
            // on parcourt l'ensemble des noms de la bdd et on regarde si le nom est identique à l'un d'entre eux
        },
        isForm1Valid(){
            return this.isNotEmpty() && this.isPasswordsEqual() && this.isNameExists();
        },
        isForm2Valid(){
            return true;
        },
        subscribe(){
        }
    }
}
</script>

<style lang="scss">

.form-group{
  width:400px;
  margin-top:150px !important;
  margin-right:auto;
  margin-left:auto;
  .title{
    text-align:center;
    margin-bottom:20px;
  }
  p{
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