

<template>
<div>
  <div style="margin-top:5em;"> Se connecter 
    <form @submit.prevent="login">
      <div>Username</div>
      <input type="text" v-model="userLogin.username">
      <div>password</div>
      <input type="password" v-model="userLogin.password">
      <div v-if="errorAtLogin.code !== 200">
        <p>{{ errorAtLogin.message }}</p>
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
  </div>

  <div style="margin-top:5em;"> S'enregistrer
    <form @submit.prevent="register">
      <div>Username</div>
      <input type="text" v-model="userRegister.username">
      <div>password</div>
      <input type="password" v-model="userRegister.password">
      <div v-if="errorAtRegister.code !== 200">
        <p>{{ errorAtRegister.message }}</p>
      </div>
      <div>
        <button type="submit">Register</button>
      </div>
    </form>
  </div>
</div>

</template>

<script>
export default {
  name: "Login",
  components :{
  },
  data(){
    return {
      userLogin: {
        username:'',
        password: '',
      },
      userRegister: {
        username:'',
        password: '',
      },
      loginError: false,
      registerBool: false,
      errorAtLogin: {
        code: 200,
        message: ""
      },
      errorAtRegister: {
        code: 200,
        message: ""
      }
    }
  },
  computed: {
    isLogged() {
      return this.$store.getters.isLogged;
    }
  },
  methods:{
    isFormValid() {
        return true // TODO : Vérifier si il y a bien un pwd et un username dans l'input
    },
    login() {
      this.$store.dispatch('login', {
        user : {
          username : this.userLogin.username,
          password : this.userLogin.password
        }
      }).then((result) => {
        console.log("result : ",result.error);
        if (result.error?.code === 403)
          this.errorAtLogin = {
            code : result.status,
            message : result.message
          }
        else 
          this.$router.push({name:"Home"})
      })
    },
    register() {
      this.$store.dispatch('register', {
        user : {
          username : this.userRegister.username,
          password : this.userRegister.password
        }
      }).then((result) => {
        if (result.status === 200) {
          this.registerBool = true
        } else {
          this.errorRegister = {
            code : result.status,
            message : result.message
          }
        }
      });
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