<template>
  <div>
    <TournamentForm @submit="handleSubmit" />
  </div>
</template>

<script>
import { mapActions } from "vuex";
import TournamentForm from "../components/TournamentForm";

export default {
  name: "TournamentCreateView",

  components: {
    TournamentForm
  },
  methods: {
    ...mapActions(["createTournament"]),
    handleSubmit: function(data) {
      this.$store.dispatch('createTournament', data).then((resp) => {
        this.$router.push('/')
      })
    }
  }
};
</script>

<style>
</style>