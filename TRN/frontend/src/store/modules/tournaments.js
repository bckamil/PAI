import axios from 'axios';

export default {
  state: {
    allTournaments: [],
    userTournaments: [],
    tournament: {}
  },
  getters: {
    getTournaments: state => state.allTournaments,
    getUserTournaments: state => state.userTournaments,
    getTournament: state => state.tournament
  },
  mutations: {
    setTournaments: (state, tournaments) => (state.allTournaments = tournaments),
    setUserTournaments: (state, tournaments) => (state.userTournaments = tournaments),
    setTournament: (state, tournament) => (state.tournament = tournament)
  },
  actions: {
    async fetchTournaments({ commit }, link = undefined) {
      if (link === undefined) {
        link = "api/tournaments/";
      }
      const response = await axios.get(
        link
      )

      commit('setTournaments', response.data)
    },

    async searchTournaments({ commit }, data) {
      const response = await axios.get(
        `api/tournaments/?search=${data}`
      )

      commit('setTournaments', response.data)
    },

    async fetchTournament({ commit }, id) {
      const response = await axios.get(
        `api/tournaments/${id}`
      )

      commit('setTournament', response.data)
    },

    async fetchUserTournaments({ commit }, link = undefined) {
      if (link === undefined) {
        link = 'api/tournamens/user/';
      }
      const response = await axios.get(
        link
      )

      commit('setUserTournaments', response.data)
    },

    async updateTournament({ commit }, { id, data }) {
      const response = await axios.put(
        `api/tournaments/${id}/update`, data
      )

      commit('setTournament', response.data)
    },

    async createTournament({ commit }, data) {
      const response = await axios.post(
        'api/tournaments/', data
      )

      commit('setTournament', response.data)
    },
  }
}