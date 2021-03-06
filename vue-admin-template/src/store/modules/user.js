import { login, getInfo, registered } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    role: ''
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  // 用户权限
  SET_ROLE: (state, role) => {
    state.role = role
  }
}

const actions = {
  // user login
  login({ commit }, userInfo) {
    const { username, password, identify_code } = userInfo
    return new Promise((resolve, reject) => {
      login({ username: username.trim(), password: password, identify_code: identify_code }).then(response => {
        const data = response.data
        console.log(data)
        // Vuex
        commit('SET_TOKEN', data.jwt_token)
        // 浏览器cookie
        setToken(data.jwt_token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  registered({ commit }, userInfo) {
    const { username, password, invite_code } = userInfo
    return new Promise((resolve, reject) => {
      registered({ username: username.trim(), password: password, register_key: invite_code.trim() }).then(response => {
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo().then(response => {
        const data = response.data

        if (!data) {
          return reject('Verification failed, please Login again.')
        }

        commit('SET_NAME', data.username)
        commit('SET_ROLE', data.role)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    removeToken() // must remove  token  first
    resetRouter()
    commit('RESET_STATE')
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

