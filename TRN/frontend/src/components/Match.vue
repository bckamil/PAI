<template>
  <div class="border rounded mb-1 p-1">
    <span
      class="font-weight-bold"
    >{{ this.getUsername(match.player_1) }} vs {{ this.getUsername(match.player_2) }}</span>
    <br />
    <span>
      Winner: {{ this.getUsername(match.winner) || '---' }}
      <span class="font-weight-bold" style="color: red;" v-if="!match.accept && match.winner">?!</span>
    </span>
    <div
      v-if="!showResultForm && (getUserMe.id === getId(match.player_1) || getUserMe.id === getId(match.player_2))"
      class="mb-2"
    >
      <button
        v-if="getUserMe.id !== match.winner_set_by && !match.accept"
        v-on:click="showResultForm = true;"
        class="btn btn-outline-info"
      >Set winner</button>
    </div>
    <div v-if="showResultForm" class="mb-2">
      <button
        v-on:click="setWinner(getId(match.player_1))"
        class="btn btn-outline-info mr-1"
      >{{ this.getUsername(match.player_1) }}</button>
      <button
        v-on:click="setWinner(getId(match.player_2))"
        class="btn btn-outline-info mr-1"
      >{{ this.getUsername(match.player_2) }}</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "Match",

  computed: mapGetters(["getUserMe"]),
  data() {
    return {
      showResultForm: false
    };
  },
  methods: {
    getUsername: function(player) {
      if (player && player.username) {
        return player.username;
      }
      return "???";
    },
    getId: function(player) {
      if (player && player.id) {
        return player.id;
      }

      return undefined;
    },
    setWinner: function(winnerId) {
      axios
        .put(`api/match/winner/${this.match.id}`, { winner: winnerId })
        .then(resp => {
          if (resp.status === 200) {
            this.match.winner = resp.data.winner;
            this.match.winner_set_by = resp.data.winner_set_by;
            this.match.accept = resp.data.accept;
            this.showResultForm = false;
            if (resp.data.accept) {
              window.location.reload()
            }
          }
        });
    }
  },
  props: {
    match: {
      required: true
    }
  }
};
</script>

<style>
</style>