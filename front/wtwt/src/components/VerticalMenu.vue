<template class="vertical-menu">
   <div>coucou</div>
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
</style>
