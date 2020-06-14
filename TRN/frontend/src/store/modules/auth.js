import axios from 'axios';

export default {
  state: {
    token: localStorage.getItem('token') || '',
    user: {}
  },
  getters: {
    isAuthenticated: state => !!state.token,
    getUserMe: state => state.user
  },
  mutations: {
    auth_success(state, token) {
      state.token = token;
    },
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    login({ commit }, loginData) {
      return new Promise((resolve, reject) => {
        axios
          .post('auth/login/', {
            username: loginData.username,
            password: loginData.password
          })
          .then(
            response => {
              const token = response.data.key

              localStorage.setItem('token', token);
              axios.defaults.headers.common['Authorization'] = 'Token ' + token;
              commit('auth_success', token);

              resolve(response);
            },
            error => {
              reject(error);
            }
          );
      });
    },
    register({ commit }, registerData) {
      return new Promise((resolve, reject) => {
        axios.post('api/register/', registerData).then(response => { resolve(response) }, error => { reject(error) });
      })
    },
    resetPassword(resetData) {
      return new Promise((resolve, reject) => {
        axios.post('', resetData)
      })
    },
    confirmAccount({ commit }, data) {
      return new Promise((resolve, reject) => {
        axios.post(`api/user/confirm/${data.uidb64}/${data.token}/`).then(response => { resolve(response) }, error => { reject(error) });
      })
    },
    async fetchUserMe({ commit }) {
      const response = await axios.get(
        'api/user/me/'
      )

      commit('setUser', response.data)
    }
  }
};
