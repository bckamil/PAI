<template>
  <div>
    <h2>LogIn</h2>
    <FormErrors :errors="errors" />
    <form @submit.prevent="loginSubmit">
      <div class="form-group">
        <input
          type="text"
          v-model="username"
          placeholder="Username"
          name="username"
          id="login-username"
          class="form-control"
        />
      </div>
      <div class="form-group">
        <input
          type="password"
          v-model="password"
          placeholder="Password"
          name="password"
          id="login-password"
          class="form-control"
        />
      </div>
      <button type="submit" class="btn btn-success w-100">Login</button>
    </form>
  </div>
</template>

<script>
import FormErrors from './FormErrors'
import { mapActions } from "vuex";

export default {
  name: "Login",
  components: {
    FormErrors
  },
  data() {
    return {
      username: "",
      password: "",
      errors: []
    };
  },
  methods: {
    ...mapActions(["login", "fetchUserMe"]),
    loginSubmit: function() {
      this.errors = [];
      const loginData = {
        username: this.username,
        password: this.password
      };
      this.login(loginData).then(resp => {
        this.fetchUserMe()
        this.$router.push("/");
      }).catch(err => {
        this.errors.push("Invalid username or password")
      });
    }
  }
};
</script>

<style>
</style>