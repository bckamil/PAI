<template>
  <div>
    <Tournament
      class="mb-5"
      v-for="tournament in tournaments.results"
      :key="tournament.id"
      :tournament="tournament"
    />
  </div>
</template>

<script>
import Tournament from "./Tournament";

export default {
  name: "TournamentsList",
  components: {
    Tournament
  },

  props: {
    tournaments: {
      required: true
    }
  }
};
</script>

<style>
</style>