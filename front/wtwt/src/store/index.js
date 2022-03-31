// import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

// Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        user : {
            username : "",
            token : ""
        },
        movies : [

        ],
        moviesUser : [

        ]
    },
    mutations: {
      setToken(state, token) {
        state.user.token = token;
      },
      setUser(state,user) {
        state.user = user;
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
      // async getTodoList(state, {id}) {
      //   const headers = { "Authorization" : state.getters.getToken}
      //   const res = await axios.get('http://localhost:5000/lists/'+id, { headers })
      //   state.commit('setCurrentTodoList',res.data.data.todo_list)
      // },
      async getPopularMovies(state) {
        const headers = { "Authorization" : state.getters.getToken}
        const url = 'http://localhost:8585/movie/popular'
        const res = await axios.get(url, { headers })
        state.commit('setMovies', res.data.data)
      },
      // async addTodo(state, payload) {
      //   const headers = { "Authorization" : state.getters.getToken}
        
      //   const url = 'http://localhost:8585/lists/todos/'+payload.todoList.id
      //   const body = {
      //     name : payload.todo.name,
      //     description : payload.todo.description
      //   } 
      //   const res = await axios.put(url, body , { headers })
      //   if (res.data.code === 200) {
      //     state.commit("addTodo", {todo : res.data.data.todo, todoList : res.data.data.updated_todo_list})
      //   } else {
      //     console.log("error", res.data)
      //   }
  
      // },
      // async createTodoList(state, {name}) {
      //   const headers = { "Authorization" : state.getters.getToken}
        
      //   const url = 'http://localhost:5000/lists'
      //   const body = {
      //     name
      //   } 
      //   const res = await axios.put(url, body , { headers })
      //   if (res.data.code === 200) {
      //     state.dispatch('getTodoLists')
      //   } else {
      //     console.log("error", res.data)
      //   }
      // },
      // async delTodoList(state, {todoList}) {
      //   const headers = { "Authorization" : state.getters.getToken}
        
      //   const url = 'http://localhost:5000/lists/'+todoList.id
  
      //   const res = await axios.delete(url, { headers })
      //   if (res.data.code === 200) {
      //     state.dispatch('getTodoLists')
      //   } else {
      //     console.log("error", res.data)
      //   }
      // },
      // async deleteTodo(state, {todo}) {
      //   const headers = { "Authorization" : state.getters.getToken}
        
      //   const todoList = state.getters.getTodoList
      //   const url = 'http://localhost:5000/lists/todos/'+todoList.id+'/'+todo.id
  
      //   const res = await axios.delete(url, { headers })
      //   if (res.data.code === 200) {
      //     state.dispatch('getTodoList', {id : todoList.id})
      //   } else {
      //     console.log("error", res.data)
      //   }
      // },
      // resetCurrentTodo(state) {
      //   state.commit('setCurrentTodo', {}) // stats.setCurrentTodo = {}
      // },
      // resetCurrentTodoList(state) {
      //   state.commit('setCurrentTodoList', {})
      // },
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
          return user
        } else {
          return Promise.reject(res.error)
        }
      },
      async register(state, payload) {
        const url = 'http://localhost:8585/user/register'
  
        const body = {
          username : payload.user.username,
          password : payload.user.password
        }

        return (await axios.post(url, body)).data
      }
    },
    modules: {
    },
    getters: {
      getUser: state => state.user,
      getToken: state => state.user.token,
      getMovies: state => state.movies,
      isLogged: state => state.user.token !== ''
    }
  })