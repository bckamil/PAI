<template>
  <div>
    <h3>Matches:</h3>
    <div v-for="level in sortedMatches" :key="level.level" class="mb-3">
      <h4 v-if="level.level === 1">Final:</h4>
      <h4 v-else>1/{{ 2 ** (level.level - 1) }}:</h4>
      <Match v-for="match in level.matches" :key="match.id" :match="match" />
    </div>
  </div>
</template>

<script>
import Match from "./Match";

export default {
  name: "Matches",

  created() {
    this.sortMatches();
  },
  components: {
    Match
  },
  data() {
    return {
      sortedMatches: []
    };
  },
  methods: {
    sortMatches: function() {
      if (this.matches) {
        let sortedMatches = [];
        const maxLevel = this.matches[0].tournament_level;
        for (let level = 1; level <= maxLevel; level++) {
          let element = this.matches.filter(o => o.tournament_level === level);
          let obj = {};
          obj["matches"] = element;
          obj["level"] = level;
          sortedMatches.push(obj);
        }
        this.sortedMatches = sortedMatches;
      }
    }
  },
  props: {
    matches: {
      required: true
    }
  },
  watch: {
    matches: function() {
      this.sortMatches();
    }
  }
};
</script>

<style>
</style>