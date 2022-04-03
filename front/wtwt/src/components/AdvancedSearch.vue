<template>
<div class="container h-100">
    <div class="d-flex justify-content-center h-100">
        <div class="search">
            <input v-model="test" class="search_input" type="text" name="" placeholder="Search here...">
            <a @click="search(test)" class="search_icon"><i class="fa fa-search"></i></a>

        </div>
        <div class="search">
            <a @click="showFilter(test)" class="search_icon"><i class="fa fa-search">more</i></a>
        </div>
    </div>
</div>
</template>

<script>
export default {
    components: {},
    name: 'AdvancedSearch',
    props: ['movie'],
    data() {
        return {
            showDialog: false,
        }
    },
    mounted() {
    },
    methods: {
        search(test) {
        }
    }
}
</script>

<style>
.search {
    margin-bottom: auto;
    margin-top: auto;
    height: 70px;
    background-color: black;
    border-radius: 40px;
    padding: 10px
}

.search_input {
    color: white;
    border: 0;
    outline: 0;
    background: none;
    width: 0;
    margin-top: 5px;
    caret-color: transparent;
    line-height: 40px;
    transition: width 0.4s linear
}

.search .search_input {
    padding: 0 10px;
    width: 550px;
    caret-color: white;
    transition: width 0.4s linear
}

.search:hover>.search_icon {
    background: blue;
    color: #fff
}

.search:hover>.more_icon {
    background: blue;
    color: #fff
}

.search_icon {
    height: 50px;
    width: 50px;
    float: right;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color: white;
    background-color: black
}

a:link {
    text-decoration: none
}
</style>
