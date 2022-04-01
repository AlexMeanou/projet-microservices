

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
      <div>Nom du group que vous souhaiter rejoindre ou créer à l'inscription</div>
      <input type="text" v-model="userRegister.group">
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
import AppVue from "@/App.vue";
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
        group: '',
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
        return (this.userRegister.username && this.userRegister.password && this.userRegister.group) != ""
    },
    login() {
      this.$store.dispatch('login', {
        user : {
          username : this.userLogin.username,
          password : this.userLogin.password
        }
      }).then(() => {
        // AppVue.computed.key.set()
        this.$router.push({name:"Home"})
      }).catch(
        (err) => {
          this.errorAtLogin = {
            code : err.code,
            message : err.message
          }
        }
      )
    },
    register() {
      if (this.isFormValid()){
        this.$store.dispatch('register', {
          user : {
            username : this.userRegister.username,
            password : this.userRegister.password,
            group: this.userRegister.group
          }
        }).then((result) => {
          console.log(result);
          if (result.error?.code) {
            this.errorAtRegister = {
              code : result.error.code,
              message : result.error.message
            }
          } else {
            this.registerBool = true
            AppVue.methods.forceRerender()
          }
        });
      } else {
        console.log("pas valide");
        this.errorAtRegister = {
          code : 400,
          message : "Le formulaire n'est pas valide"
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