<template>
  <div class="text-center">
    <h1 v-if="status === true">Success</h1>
    <h1 v-else-if="status === false">Error</h1>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "ConfirmEmailView",

  created() {
    let data = {
      uidb64: this.$route.params.uidb64,
      token: this.$route.params.token
    }
    this.confirmAccount(data).then(resp => {
      this.status = true;
    }).catch(err => {
      this.status = false;
    })
  },
  data() {
    return {
      status: null
    }
  },
  methods: {
    ...mapActions(["confirmAccount"])
  }
};
</script>

<style>
</style>