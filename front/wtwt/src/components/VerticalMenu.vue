<template>
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
              <input class="form-check-input" type="checkbox"> francais
            </div>
             <div class="form-check">
              <input class="form-check-input" type="checkbox"> Anglais
            </div>
            <div class="form-check">
              <input class="form-check-input" type="checkbox"> Espagnol
            </div>
          </div>
        </div>
        <div class="nav-bloc langue">
        <div class="form-group">
          <div class="form-check">
            <input class="form-check-input" type="checkbox"> francais
          </div>
            <div class="form-check">
            <input class="form-check-input" type="checkbox"> Anglais
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox"> Espagnol
          </div>
        </div>
      </div>
      </div>
    </nav>
</template>

<script>
export default {
    name: "Vertical-Menu",
    data(){
        return {}
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
  top:118px;
  left:0;
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
     .form-check{
       
     }
  }
}

</style>
