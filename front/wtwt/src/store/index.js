// import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';
// import * as menu from '../components/Menu.vue'
// Vue.forceUpdate();
// Vue.use(Vuex)


export default new Vuex.Store({
    state: {
      user : {
        token : ''
      },
      movies : [

      ],
      moviesUser : [

      ]
    },
    mutations: {
      setUser(state,user) {
        if (user != null) {
          state.user.token = user.token
        } else {
          state.user.token = ''
        }
        localStorage.setItem('user', JSON.stringify(user))
      },
      setMovies(state, movies) {
        state.movies = movies;
      },
      setMoviesUser(state, movies) {
        state.moviesUser = movies;
      }
    },
    actions: {
      async getMoviesByGenre(state, genre, page) {
        const headers = { "Authorization" : state.getters.getToken}
        const url = 'http://localhost:8585/movies/'
        const res = await axios.get(url + genre + "/" + page, { headers })
        state.commit('setMovies',res.data.data)
      },
      async getPopularMovies(state) {
        const headers = { "Authorization" : state.getters.getToken}
        const url = 'http://localhost:8585/movie/popular'
        const res = await axios.get(url, { headers })
        state.commit('setMovies', res.data.data)
      },
      async login(state, payload) {
        const url = 'http://localhost:8585/user/login'
  
        const body = {
          username : payload.user.username,
          password : payload.user.password
        }
  
        const res = (await axios.post(url, body)).data
        if (res.data) {
          const user = {
            username : res.data.username,
            token : res.data.token,
          }
          state.commit('setUser', user)
          // menu.default.methods.setAuth()
          return user
        } else {
          return Promise.reject(res.error)
        }
      },
      async register(state, payload) {
        const url = 'http://localhost:8585/user/register'
  
        const body = {
          username : payload.user.username,
          password : payload.user.password,
          group : payload.user.group
        }

        return (await axios.post(url, body)).data
      },
      disconnect(state) {
        state.commit('setUser', null)
      }
    },
    modules: {
    },
    getters: {
      getUser: () => JSON.parse(localStorage.getItem('user')),
      getToken: () => JSON.parse(localStorage.getItem('user'))?.token,
      getMovies: state => state.movies,
      isLogged: () => {
        console.log('isLogged', localStorage)
        const user = JSON.parse(localStorage.getItem('user'))
        return user && user.token !== ('' && null)
      },
      isLogged2: (state) => {return state.user.token !== ('' && null) } // Obligé de faire ca sinon les v-if ne marche pas car il récup 
    }
  })