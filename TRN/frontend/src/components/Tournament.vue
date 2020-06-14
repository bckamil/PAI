<template>
  <router-link :to="{'name': 'Tournament', 'params': {'id': this.tournament.id}}">
    <div class="m-3 p-3 border rounded">
      <h3>{{ this.tournament.name }}</h3>
      <hr />
      <div class="mb-1">
        <span class="font-weight-bold">Discipline:</span>
        <span>{{ this.tournament.discipline }}</span>
      </div>
      <div class="mb-1">
        <span class="font-weight-bold">Deadline:</span>
        <span>{{ this.tournament.deadline | formatDate }}</span>
      </div>
      <div class="mb-1">
        <span class="font-weight-bold">Start:</span>
        <span>{{ this.tournament.datetime|formatDate }}</span>
      </div>
      <div>
        <span class="font-weight-bold">Limit:</span>
        <span>{{ this.tournament.limit }}</span>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "Tournament",

  props: {
    tournament: {
      required: true
    }
  }
};
</script>

<style>
</style>