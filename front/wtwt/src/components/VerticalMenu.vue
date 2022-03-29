<template class="vertical-menu">
     <nav class="side-nav">
      <div class="wrapper">
        <!-- <div class="three-dots-container">
          <div class="dot d1"></div>
          <div class="dot d2"></div>
          <div class="dot d3"></div>
         </div> -->

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
        <div class="nav-bloc isAdult">
          <div class="form-group" id="form-group">
            <label class="form-label" for="form-group">Pour adulte</label>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="isAdult" v-bind:value="isAdult" @change="$emit('isAdult',isAdult)">
            </div>
          </div>
        </div>
        <div class="nav-bloc langue">
          <div class="form-group">
            <label class="form-label" for="form-group">acteurs</label>
        
              <input type="text" class="form-control search" placeholder="acteur"/>
        
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.DICAPRIO" @change="$emit('acteurs',acteurs)"> Leonardo Dicaprio
            </div>
              <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.BRAD_PITT" @change="$emit('acteurs',acteurs)"> Brad Pitt
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox" v-model="acteurs" v-bind:value="Enum.acteur.JOHNNY_DEPP" @change="$emit('acteurs',acteurs)"> Johnny Depp
            </div>
          </div>
        </div>

        <div class="nav-bloc note">
          <div class="form-group" id="form-group">
            <label class="form-label" for="form-group">Notes</label>
            <div class="form-check" v-for="n in 5" :key="n" style="display:flex">
              <input class="form-check-input" type="checkbox" v-model="notes" v-bind:value=n @change="$emit('notes',notes)"> 
              <v-img v-for="i in n" :key="i" class="star" max-width=20 src="../assets/data/images/star.png"></v-img>
            </div>
          </div>
        </div>

        <div class="nav-bloc nb-vote">
          <div class="form-group" id="form-group">
            <label class="form-label" for="form-group">Nombre de votes</label>
            <v-slider v-model="nbVotes" thumb-color="white" thumb-label="always" :max="255" class="align-center" style="margin-top:1.8rem" @click="$emit('nbVotes',nbVotes)"> </v-slider>
          </div>
        </div>

      </div>
    </nav>
</template>

<script>
export default {
  components: { 
  },
    name: "VerticalMenu",
    data(){
        return {
          langues:[],
          acteurs:[],
          notes:[],
          Enum:this.$parent.Enum,
          isAdult : false,
          nbVotes : 0,
        }
    },
    mounted(){
    },
    methods:{
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
  width: 70%;
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
      .search{
        border:none;
        padding-top:0.05rem !important;
        padding-bottom:0.05rem !important;
        width:70%;
      }
       .search:focus{
       outline: none;
       border:none;
     }
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
     .form-check{
       .form-check-input{
         margin-right:1rem;
       }
     }
     .input-vote{
       width:40%;
       background-color: white;
     }
  }
  .form-group.checkbox{
    height:50px;
  }
 
}

</style>
