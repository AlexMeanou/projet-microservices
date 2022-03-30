import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        user : {
            username : "",
            password : "",
            token : ""
        },
        movies : [

        ]
    },
    mutations: {
      setToken(state, token) {
        state.user.token = token;
      },
      setUser(state,user) {
        state.user = user;
      },
    },
    actions: {
      async getTodoLists(state) {
        const headers = { "Authorization" : state.getters.getToken}
        const res = await axios.get('http://localhost:5000/lists', { headers })
        state.commit('setTodoLists',res.data.data)
      },
      async getTodoList(state, {id}) {
        const headers = { "Authorization" : state.getters.getToken}
        const res = await axios.get('http://localhost:5000/lists/'+id, { headers })
        state.commit('setCurrentTodoList',res.data.data.todo_list)
      },
      async updateTodoList(state, todoList) {
        const headers = { "Authorization" : state.getters.getToken}
        
        const url = 'http://localhost:5000/lists/'+todoList.id
        const res = await axios.patch(url, todoList , { headers })
        if (res.status !== 200) {
          console.log("ERROR updateTodoList")
        }
      },
      async addTodo(state, payload) {
        const headers = { "Authorization" : state.getters.getToken}
        
        const url = 'http://localhost:5000/lists/todos/'+payload.todoList.id
        const body = {
          name : payload.todo.name,
          description : payload.todo.description
        } 
        const res = await axios.put(url, body , { headers })
        if (res.data.status === 200) {
          state.commit("addTodo", {todo : res.data.data.todo, todoList : res.data.data.updated_todo_list})
        } else {
          console.log("error", res.data)
        }
  
      },
      async createTodoList(state, {name}) {
        const headers = { "Authorization" : state.getters.getToken}
        
        const url = 'http://localhost:5000/lists'
        const body = {
          name
        } 
        const res = await axios.put(url, body , { headers })
        if (res.data.status === 200) {
          state.dispatch('getTodoLists')
        } else {
          console.log("error", res.data)
        }
      },
      async delTodoList(state, {todoList}) {
        const headers = { "Authorization" : state.getters.getToken}
        
        const url = 'http://localhost:5000/lists/'+todoList.id
  
        const res = await axios.delete(url, { headers })
        if (res.data.status === 200) {
          state.dispatch('getTodoLists')
        } else {
          console.log("error", res.data)
        }
      },
      async deleteTodo(state, {todo}) {
        const headers = { "Authorization" : state.getters.getToken}
        
        const todoList = state.getters.getTodoList
        const url = 'http://localhost:5000/lists/todos/'+todoList.id+'/'+todo.id
  
        const res = await axios.delete(url, { headers })
        if (res.data.status === 200) {
          state.dispatch('getTodoList', {id : todoList.id})
        } else {
          console.log("error", res.data)
        }
      },
      resetCurrentTodo(state) {
        state.commit('setCurrentTodo', {}) // stats.setCurrentTodo = {}
      },
      resetCurrentTodoList(state) {
        state.commit('setCurrentTodoList', {})
      },
      async login(state, payload) {
        const url = 'http://localhost:5000/login'
  
        const body = {
          username : payload.user.username,
          password : payload.user.password
        }
  
        const res = await axios.post(url, body)
        if (res.data.status === 200) {
          const user = {
            username : res.data.data.user.username,
            password : res.data.data.user.password,
            token : res.data.data.token,
          }
          state.commit('setUser', user)
        } else {
          return res.data
        }
      },
      async account(state, payload) {
        const url = 'http://localhost:5000/account'
  
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