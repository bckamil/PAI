<template>
  <div>
    <TournamentForm :tournament="getTournament" @submit="handleSubmit" />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import TournamentForm from "../components/TournamentForm";

export default {
  name: "TournamentUpdateView",

  components: {
    TournamentForm
  },
  computed: mapGetters(["getTournament"]),
  created() {
    const id = this.$route.params.id;
    this.fetchTournament(id);
  },
  methods: {
    ...mapActions(["updateTournament", "fetchTournament"]),
    handleSubmit: function(data) {
      const id = this.$route.params.id;
      this.$store.dispatch("updateTournament", {id, data}).then(resp => {
        this.$router.push("/");
      });
    }
  }
};
</script>

<style>
</style>