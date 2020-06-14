<template>
  <div>
    <h2>Reset Password</h2>
      <div class="form-group">
        <input
          type="text"
          v-model="username"
          placeholder="Email"
          name="username"
          id="login-username"
          class="form-control"
        />
      </div>
      <button class="btn btn-success w-100">Reset Password</button>
  </div>
</template>

<script>
export default {
  name: "ResetPassword",
  data() {
    return {
      
    }
  },
  methods: {
    resetPassword: function () {

    }
  }
}
</script>

<style>

</style>