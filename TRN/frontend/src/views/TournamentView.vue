<template>
  <div>
    <TournamentDetails :tournament="getTournament" />
  </div>
</template>

<script>
import TournamentDetails from "../components/TournamentDetails";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "TournamentView",
  components: {
    TournamentDetails
  },
  computed: mapGetters(["getTournament"]),
  created() {
    const id = this.$route.params.id;
    this.fetchTournament(id);
  },
  methods: {
    ...mapActions(["fetchTournament"])
  }
};
</script>

<style>
</style>