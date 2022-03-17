

<template>
<div class="connexion">
  <Menu/>
  <div class="form-group">
    <h2 class="title"></h2>
    <div>
      <label for="name">nom</label>
      <input class="form-control" type="text" v-model="name" id="name">
    </div>
    <div>
      <label for="password">mot de passe</label>
      <input class="form-control" type="password" v-model="password" id="password">
    </div>
  </div>
</div>
</template>

<script>
import Menu from "../components/Menu.vue"
export default {
  name: "Connexion",
  components :{
    Menu
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
    margin-bottom:20px;
  }
  .form-control{
    margin-bottom:10px;
  }
}

</style>