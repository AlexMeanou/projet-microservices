<template>
<div id="home">

    <div class="scrollmenu">
        <a v-for="genre in this.$store.getters.getGenres" :key="genre" @click="clickOnGenre(genre)">{{genre}}</a>
    </div>
    <div class="container">
        <div class="d-flex justify-content-center">
            <div class="search">
                <input v-model="search_input" class="search_input" type="text" name="" placeholder="Search here...">
                <a @click="search(search_input)" class="search_icon"><i class="fa fa-search"></i></a>

            </div>
            <div class="search">
                <a @click="showFilter()" class="search_icon"><i class="fa fa-search">more</i></a>
            </div>
        </div>
        <form v-if="show_filter" @submit.prevent="saveFilter">
            <input v-model="is_adult" class="form-check-input" type="checkbox" value="" id="defaultCheck1">
            <label class="form-check-label" for="defaultCheck1">
                Adult Movie
            </label>
            <div class="form-group">
                <label for="exampleFormControlInput1">Acteur Name</label>
                <input v-model='actor' type="text" class="form-control" id="exampleFormControlInput1" placeholder="acteur name">
            </div>
            <label class="form-label" for="form-group">Nombre de votes</label>
            <v-slider v-model="nbVotes" thumb-color="white" thumb-label="always" :max="255" class="align-center" style="margin-top:1.8rem" @click="$emit('nbVotes',nbVotes)"> </v-slider>
          

            <div>
                <button type="submit">save</button>
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
</template>

<script>
import Film from '../components/Film.vue';

import Enum from "../utils/enum"
import MenuVue from '@/components/Menu.vue';
export default {
    name: 'Home',
    components: {
        // FilmGrid,
        Film,
        // VerticalMenu,
    },
    data: function () {
        return {
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
        reloadMovies() {
            this.$store.dispatch('getMoviesByGenre', {
                page: this.page,
                genre: this.genre,
                note_inf: this.note_inf,
                note_sup: this.note_sup,
                search_input: this.search_input,
                // is_adult: this.is_adult ? "1" : "0",
                actor: this.actor,
            }).then(() => {

                console.log("ggg")
                this.movies = this.$store.getters.getMovies
                console.log("les films ont etet reload", this.movies)
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
            console.log("je save", this.is_adult)
            this.reloadMovies()
        },
        showFilter() {
            this.show_filter = !this.show_filter;
            console.log("on montre les filtres")
        },
        clickOnGenre(genre) {
            console.log(genre)
            this.genre = genre
            this.reloadMovies()
            // this.filterList.genre=genreId;

            //  this.filter(); 
        },
        selectGenre() {
            this.filterList.genre = this.selectedGenre;
            this.filter();
        },
        search(search_input) {
            this.search_input = search_input
            console.log(search_input)
        },
        selectLangues(langues) {
            this.filterList.langues = langues;
            this.filter();
        },
        selectActeurs(acteurs) {
            this.filterList.acteurs = acteurs;
            this.filter();
        },
        selectNotes(notes) {
            this.filterList.notes = notes;
            this.filter();
        },
        selectVotes(nbVotes) {
            this.filterList.nbVotes = nbVotes;
            this.filter();
        },
        selectAdult(isAdult) {
            this.filterList.isAdult = isAdult;
            this.filter();
        },
        filter() {
            console.log("filter", this.filterList);
            this.filterMovies = this.movies.filter(x => {
                if (this.filterList.genre !== Enum.genre.TOUS) {
                    return x.genres == this.filterList.genre
                } else {
                    return true;
                }
            });

            this.filterMovies = this.filterMovies.filter(x =>
                this.filterList.langues.every(l => {
                    return x.languages.includes(l);
                }));

        },
        filterGenre() {
            return 0
        },
        // changePage(){
        //   this.movies = 
        //   // console.log("filerList",this.filterList);
        //   // this.axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';
        //   // console.log("page numero",this.page);
        //   //  this.axios.get('http://localhost:8585/movies/Short/' + this.page)
        //   // .then(response =>{
        //   //   this.movies = response.data
        //   //   console.log(this.movies)
        //   // } );
        // }
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
