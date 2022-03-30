

<template>
<div>
    <div>Username</div>
    <input type="text" (value)="username">
    <div>password</div>
    <input type="passwword" (value)="password">
</div>

</template>

<script>
export default {
  name: "Login",
  components :{
  },
  data(){
    return {
        username:"toto",
        password: 'tata',
        loginError: false
    }
  },
  methods:{
    isFormValid() {
        return true // TODO : Vérifier si il y a bien un pwd et un username dans l'input
    },
    login(){
      if(this.isFormValid()){
          this.$storage.user
        if(this.isLoginCorrect()){
          console.log("connexion reussie");
          localStorage.name=this.name;
          this.$router.push('/');
          this.$router.go();
        }
        else{
          this.loginError=true;
        }
      }
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