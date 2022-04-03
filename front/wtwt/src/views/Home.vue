<template>
<div id="home">

    <div class="scrollmenu">
        <a v-for="genre in this.$store.getters.getGenres" :key="genre" @click="clickOnGenre(genre)">{{genre}}</a>
    </div>
    <div class="container">
        <div class="pad">

            <div class="d-flex justify-content-center">
                <div class="search">
                    <input v-model="search_input" class="search_input" type="text" name="" placeholder="Search here...">
                    <a @click="search(search_input)" class="search_icon"><i class="fa fa-search"></i></a>

                </div>
                <div class="search">
                    <a @click="showFilter()" class="search_icon"><i class="fa fa-search">more</i></a>
                </div>
            </div>
            <br/>

            <form v-if="show_filter" @submit.prevent="saveFilter">
                <div class="advensed-search">
                    <input v-model="is_adult" class="form-check-input" type="checkbox" value="" id="defaultCheck1">
                    <label class="form-check-label" for="defaultCheck1">
                        Adult Movie
                    </label>
                    <br/>
                    <br/>

                    <div>
                        <label for="exampleFormControlInput1">Acteur Name : (cette fonctionnalité comporte un probleme pour son bon fonctionnememnt il faut que le site soit rempli)</label>
                        <input v-model='actor' type="text" class="form-control" id="exampleFormControlInput1" placeholder="acteur name">
                    </div>
                    <br />

                    <label class="form-label" for="form-group">Nombre de votes</label>
                    <MultiRangeSlider :min="0" :max="10" :step="1" :ruler="true" :label="false" :minValue="note_inf" :maxValue="note_sup" @input="UpdateValues" />

                    <div>
                        <button class="save_button" type="submit">save</button>
                    </div>
                </div>
            </form>

        </div>

        <div class="row">
            <div class="col-md-3 col-sm-6" v-for="movie in this.$store.getters.getMovies" :key="movie._id">
                <film :movie="movie" />
            </div>
        </div>

        <v-pagination color="#e4872c" v-model="page" :length="20" :value="page" @click="reloadMovies()"></v-pagination>

    </div>
</div>
</template>

<script>
import Film from '../components/Film.vue';
import MultiRangeSlider from "multi-range-slider-vue";
import MenuVue from '@/components/Menu.vue';
export default {
    name: 'Home',
    components: {
        MultiRangeSlider,
        // FilmGrid,
        Film,
        // VerticalMenu,
    },
    data: function () {
        return {
            barMinValue: 0,
            barMaxValue: 10,
            show_filter: false,
            is_adult: false,
            genre: "all",
            page: 1,
            movies: [],
            note_inf: 0,
            note_sup: 10,
            actor: "nulle",
            search_input: "nulle",
            filterMovies: [],
            selectedGenre: "",
        }
    },
    mounted() {
        MenuVue.methods.setAuth()
        this.$store.dispatch('getGenres')
        this.reloadMovies()
    },
    methods: {
        UpdateValues(e) {
            this.barMinValue = e.minValue;
            this.barMaxValue = e.maxValue;
        },
        reloadMovies() {
            // const test = this.is_adult ? "1" : "0"
            this.$store.dispatch('getMoviesByGenre', {
                page: this.page,
                genre: this.genre,
                note_inf: this.note_inf,
                note_sup: this.note_sup,
                search_input: this.search_input,
                actor: this.actor,
            }).then(() => {

                this.movies = this.$store.getters.getMovies
                this.$router.push({
                    name: "Home"
                })
            }).catch(
                (err) => {
                    this.errorAtLogin = {
                        code: err.code,
                        message: err.message
                    }
                }
            )
        },
        saveFilter() {
            this.reloadMovies()
        },
        showFilter() {
            this.show_filter = !this.show_filter;
        },
        clickOnGenre(genre) {
            this.genre = genre
            this.reloadMovies()
            
        },
        search(search_input) {
            this.search_input = search_input
        }
    }
}
</script>

<style lang="scss" scoped>
.search {
    height: 70px;
    background-color: black;
    border-radius: 40px;
    padding: 10px
}

.pad{
  padding : 10px;
}
.advensed-search {
    text-align: center;

    background-color: black;
    border-radius: 40px;
    padding: 20px;
    color: white;
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

.save_button {}

.search .search_input {
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

.scrollmenu {
    background-color: #333;
    overflow: auto;
    white-space: nowrap;
    color: white;
}

a {
    display: inline-block;
    color: white;
    text-align: center;
    padding: 14px;
    text-decoration: none;
}

.scrollmenu a:hover {
    background-color: #777;
}

.select-genre {
    text-decoration: none !important;
}

.nav-link:hover {
    text-decoration: underline;
}

.btn {
    color: white;
    border-color: white;
}

.btn:hover {
    font-weight: 450;
    color: white;
}
</style>
