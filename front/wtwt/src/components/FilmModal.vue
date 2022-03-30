
<template>
    <v-dialog v-if="dialogModel"
        v-model="dialogModel"
        scrollable
        max-width="300px"
    >
      <v-card>
        <v-card-title>Tous les acteurs</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;layout:scroll">
          {{dialogModel}}
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
           @click="$emit('showDialog',this.dialogModel=false)"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="$emit('showDialog',this.dialogModel=false)"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
      </v-dialog>  
</template>

<template>
    <v-dialog
        v-model="dialogModel"
        scrollable
        max-width="300px"
    >
      <v-card>
        <v-card-title>Tous les acteurs</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 300px;layout:scroll">
          {{dialogModel}}
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn
            color="blue darken-1"
            text
           @click="$emit('showDialog',this.dialogModel=false)"
          >
            Close
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="$emit('showDialog',this.dialogModel=false)"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
      </v-dialog>  
</template>
<script>
  export default {
    data () {
      return {
       dialogModel: false,
      selectedActors : [],
      }
    },
     methods:{
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