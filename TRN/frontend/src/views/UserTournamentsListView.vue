<template>
  <div>
    <TournamentsList :tournaments="getUserTournaments" />
    <div class="mb-5">
      <button
        v-if="getUserTournaments.previous"
        v-on:click="loadPage(getUserTournaments.previous)"
        class="btn btn-outline-success float-left"
      >Previous</button>
      <button
        v-if="getUserTournaments.next"
        v-on:click="loadPage(getUserTournaments.next)"
        class="btn btn-outline-success float-right"
      >Next</button>
    </div>
  </div>
</template>

<script>
import TournamentsList from "../components/TournamentsList";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "UserTournamentsListView",

  components: {
    TournamentsList
  },
  computed: mapGetters(["getUserTournaments"]),
  created() {
    this.fetchUserTournaments();
  },
  methods: {
    ...mapActions(["fetchUserTournaments"])
  }
};
</script>

<style>
</style>