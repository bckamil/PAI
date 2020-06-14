<template>
  <div>
    <TournamentsList :tournaments="getTournaments" />
    <div class="mb-5">
      <button
        v-if="getTournaments.previous"
        v-on:click="loadPage(getTournaments.previous)"
        class="btn btn-outline-success float-left"
      >Previous</button>
      <button
        v-if="getTournaments.next"
        v-on:click="loadPage(getTournaments.next)"
        class="btn btn-outline-success float-right"
      >Next</button>
    </div>
  </div>
</template>

<script>
import TournamentsList from "../components/TournamentsList";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "TorunamentsListView",

  computed: mapGetters(["getTournaments"]),
  components: {
    TournamentsList
  },
  created() {
    this.fetchTournaments();
  },
  methods: {
    ...mapActions(["fetchTournaments"]),
    loadPage: function(link) {
      this.fetchTournaments(link);
    }
  }
};
</script>

<style>
</style>