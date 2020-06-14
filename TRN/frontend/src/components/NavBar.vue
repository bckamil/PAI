<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="success">
      <b-navbar-brand>
        <router-link :to="{ 'name': 'Tournaments' }">Tournaments</router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-form class="ml-5" v-if="this.$route.path === '/'">
            <b-form-input
              size="sm"
              class="mr-sm-2"
              placeholder="Search"
              v-model="searchData"
            ></b-form-input>
          </b-nav-form>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <template v-if="isAuthenticated">
            <b-nav-item right class="mr-2 ml-2">
              <router-link :to="{ 'name': 'TournamentsCreate'}">Add tournament</router-link>
            </b-nav-item>
            <b-nav-item right class="mr-2 ml-2">
              <router-link :to="{ 'name': 'UserTournamentsList' }">My tournaments</router-link>
            </b-nav-item>
            <b-nav-item-dropdown right>
              <template v-slot:button-content>
                <em>Profile</em>
              </template>
              <b-dropdown-item href="#" v-on:click="signOut">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </template>
          <template v-else>
            <b-nav-item right>
              <router-link :to="{ 'name': 'Auth' }">LogIn</router-link>
            </b-nav-item>
          </template>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "NavBar",

  data() {
    return {
      searchData: "",
      isAuthenticated: this.$store.getters.isAuthenticated
    };
  },
  methods: {
    ...mapActions(["searchTournaments"]),
    signOut: function() {
      localStorage.removeItem("token");
      window.location.reload();
    }
  },
  watch: {
    searchData: function() {
      this.searchTournaments(this.searchData);
    }
  }
};
</script>

<style>
</style>