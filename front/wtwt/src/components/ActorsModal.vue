
<template>
  <div id="app">
    <button @click="dialogModel=true">test</button>
    <v-dialog
        v-model="dialogModel"
        scrollable
        max-width="300px"
    >
      <v-card>
        <v-card-title>Tous les acteurs</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;layout:scroll">
          <div class="form-check" v-for="actor in allActors" v-bind:key="actor.value">
          <input v-bind:key="actor.value" :value="actor.value" class="form-check-input" type="checkbox" v-model="selectedActors" @click="test()"/> {{actor.text}}
        </div>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
            @click="dialogModel = false"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="dialogModel = false"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
      </v-dialog>  
  </div>
</template>
<script>
  export default {
    props:['showDialog','Enum'],
    data () {
      return {
       dialogModel: false,
      selectedActors : [],
        allActors :[
          {text:"Leonardo Decaprio",value:1},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},
          {text:"Brad Pitt",value:2},  
        ]
      }
    },
     methods:{
       test(){
         console.log("parent",this.Enum)
       }
    }
  }
</script>

<style scoped>
v-dialog {
  color:white;
}
v-card{

}
</style>