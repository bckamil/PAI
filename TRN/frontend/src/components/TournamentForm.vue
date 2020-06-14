<template>
  <form @submit.prevent="getFormData" class="m-3 [-3">
    <div class="form-group">
      <label for="name">Name:</label>
      <input class="form-control" type="text" name="name" v-model="tournament.name" />
    </div>
    <div class="form-group">
      <label for="discipline">Discipline:</label>
      <input class="form-control" type="text" name="discipline" v-model="tournament.discipline" />
    </div>
    <div class="form-group">
      <label for="limit">Limit:</label>
      <input class="form-control" type="number" name="limit" v-model="tournament.limit" />
    </div>
    <div class="form-group">
      <label for="datetime">Start:</label>
      <datetime
        type="datetime"
        class="theme-success"
        minute-step="5"
        input-class="form-control"
        name="datetime"
        v-model="tournament.datetime"
      ></datetime>
    </div>
    <div class="form-group">
      <label for="deadline">Deadline:</label>
      <datetime
        type="datetime"
        class="theme-success"
        minute-step="5"
        input-class="form-control"
        name="datetime"
        v-model="tournament.deadline"
      ></datetime>
    </div>
    <div class="form-group">
      <label for="deadline">Organizer:</label>
      <input class="form-control" type="text" name="organizer" v-model="tournament.organizer" />
    </div>
    <button class="btn btn-success w-sm-100">Save</button>
  </form>
</template>

<script>
import { Datetime } from "vue-datetime";

export default {
  name: "TournamentForm",

  components: {
    Datetime
  },
  methods: {
    getFormData: function() {
      this.$emit("submit", this.tournament);
    },
    isFormValid: function() {}
  },
  props: {
    tournament: {
      type: Object,
      default: () => {
        return {
          datetime: null,
          deadline: null,
          discipline: "",
          limit: null,
          name: "",
          organizer: ""
        };
      }
    }
  }
};
</script>

<style>
</style>