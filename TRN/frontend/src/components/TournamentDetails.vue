<template>
  <div class="p-3">
        <div v-if="getUserMe.id === tournament.owner" class="float-right">
      <router-link
        :to="{ 'name': 'TournamentUpdate', 'params': {'id': tournament.id}}"
        class="btn btn-outline-success"
      >Edit</router-link>
    </div>
    <h2>{{ this.tournament.name }}</h2>
    <p>
      <span class="font-weight-bold">Discipline:</span>
      {{ this.tournament.discipline }}
    </p>
    <p>
      <span class="font-weight-bold">Limit:</span>
      {{ this.tournament.limit }}
    </p>
    <p>
      <span class="font-weight-bold">Deadline:</span>
      {{ this.tournament.deadline|formatDate }}
    </p>
    <p>
      <span class="font-weight-bold">Start:</span>
      {{ this.tournament.datetime|formatDate }}
    </p>
    <p>
      <span class="font-weight-bold">Organizer:</span>
      {{ this.tournament.organizer }}
    </p>
    <p>
      <span class="font-weight-bold">Participants: </span>
      <span v-if="tournament.applications">{{ this.tournament.applications.length }}</span>
    </p>
    <div
      v-if="tournament.applications && tournament.applications.length < tournament.limit && !isParticipant()"
    >
      <button
        v-if="!showJoinForm"
        v-on:click="showJoinForm = true;"
        class="btn btn-outline-success"
      >Join!</button>
    </div>
    <div v-if="tournament.matches.length > 0">
      <Matches :matches="tournament.matches" />
    </div>
    <div v-if="showJoinForm" class="border rounded mt-2 p-2">
      <FormErrors :errors="joinData.errors" />
      <div class="group-form">
        <label for="license_number">License number:</label>
        <input
          v-model="joinData.licenseNumber"
          type="text"
          name="license_number"
          class="form-control"
        />
      </div>
      <div class="group-form">
        <label for="ranking">Ranking::</label>
        <input v-model="joinData.ranking" type="text" name="ranking" class="form-control" />
      </div>
      <div>
        <button v-on:click="joinTournament" class="btn btn-success mt-1">Join now!</button>
        <button v-on:click="showJoinForm = false;" class="btn btn-outline-danger mt-1 ml-1">Cancel</button>
      </div>
    </div>

  </div>
</template>

<script>
import FormErrors from "./FormErrors";
import Matches from "./Matches";
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  name: "TournamentDetails",

  data() {
    return {
      showJoinForm: false,
      joinData: {
        licenseNumber: "",
        ranking: null,
        errors: []
      }
    };
  },
  components: {
    FormErrors,
    Matches
  },
  computed: mapGetters(["getUserMe"]),
  methods: {
    isParticipant: function() {
      if (this.tournament.applications) {
        return (
          this.tournament.applications.filter(o => o.user === this.getUserMe.id)
            .length > 0
        );
      }
      return false;
    },
    joinTournament: function() {
      this.joinData.errors = []

      if (!this.joinData.licenseNumber) {
        this.joinData.errors.push("License number is required");
      }
      if (!this.joinData.ranking) {
        this.joinData.errors.push("Ranking is required");
      } else {
        const reg = /^\d+$/;
        if (!reg.test(this.joinData.ranking)) {
          this.joinData.errors.push("Ranking is invalid");
        } else {
          if (this.joinData.ranking < 1) {
            this.joinData.errors.push("Ranking is invalid");
          }
        }
      }
      if (this.joinData.errors.length === 0) {
        const data = {
          tournament_application: this.$route.params.id,
          license_number: this.joinData.licenseNumber,
          ranking: this.joinData.ranking
        };
        axios
          .post("api/tournaments/join/", data)
          .then(resp => {
            if (resp.status === 201) {
              window.location.reload();
            }
          })
          .catch(err => {
            this.joinData.errors = [err.response.data.msg];
          });
      }
    }
  },
  props: {
    tournament: {
      required: true
    }
  }
};
</script>

<style>
</style>