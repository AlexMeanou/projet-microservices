<template class="vertical-menu">
     <nav class="side-nav">
      <div class="wrapper">
        <div class="three-dots-container">
          <div class="dot d1"></div>
          <div class="dot d2"></div>
          <div class="dot d3"></div>
        </div>

        <div class="nav-bloc langue">
          <div class="form-group" id="form-group">
            <label class="form-label" for="form-group">langues</label>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="langues" v-bind:value="Enum.langue.FRANCAIS" @change="$emit('langues',langues)"> francais
            </div>
             <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="langues" v-bind:value="Enum.langue.ANGLAIS" @change="$emit('langues',langues)"> Anglais
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="langues" v-bind:value="Enum.langue.ESPAGNOL" @change="$emit('langues',langues)"> Espagnol
            </div>
          </div>
        </div>
        <div class="nav-bloc langue">
          <div class="form-group checkbox">
            <label class="form-label" for="form-group">acteurs</label>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.DICAPRIO" @change="$emit('acteurs',acteurs)"> Leonardo Dicaprio
            </div>
              <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.BRAD_PITT" @change="$emit('acteurs',acteurs)"> Brad Pitt
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.JOHNNY_DEPP" @change="$emit('acteurs',acteurs)"> Johnny Depp
            </div>
            {{showDialog}}
            <a class="nav-link" @click="showDialog = true">Tous afficher</a>
             <actors-modal v-if="showDialog" :showDialog="showDialog" :Enum="Enum"/>
          </div>
        </div>
      </div>
     
    </nav>
</template>

<script>
import ActorsModal from '../components/ActorsModal.vue';
export default {
  components: { 
    ActorsModal 
  },
    name: "VerticalMenu",
    data(){
        return {
          langues:[],
          acteurs:[],
          Enum:this.$parent.Enum,
          showDialog : false,
        }
    },
    mounted(){
    },
    methods:{
      openActorsDialog(){
        console.log("open dialog",this.acteurs);
      }
    }

}
</script>

<style scoped lang="scss">

.side-nav {
  position: fixed;
  top:125px;
  left:0;
  z-index:30;
}

/* To hide the sub-nav */
.wrapper {
  color:white;
  background:black;
  height: 100vh;
  width: auto;
  padding-right:20px;
  padding-left:20px;
}

.three-dots-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60px;
}

.dot {
  flex-shrink: 0;
  margin: 10px 3px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: black;
}

.d1 {background: crimson;}

.d2 {background: yellow;}

.d3 {background: lightgreen;}

.nav-bloc {
  padding: 10px 0;
  display: flex;
  justify-content: center;
  cursor: pointer;
  border-bottom: 1px solid black;
  .form-group{
    margin-top:5px !important;
     width:90%;
     .form-title{
       text-align:center;
     }
     .form-label{
       font-weight:500;
     }
     .nav-link{
       color:white;
     }
     .nav-link:hover{
       text-decoration: underline;
     }
  }
  .form-group.checkbox{
    height:50px;
  }
}

</style>
