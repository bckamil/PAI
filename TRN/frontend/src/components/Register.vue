<template>
  <div>
    <h2>Sign In</h2>
    <FormErrors :errors="errors" />
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
    <div class="form-group">
      <input
        type="password"
        v-model="password2"
        placeholder="Confirm password"
        name="password2"
        id="login-password2"
        class="form-control"
      />
    </div>
    <div class="form-group">
      <input
        type="text"
        v-model="email"
        placeholder="Email"
        name="email"
        id="login-email"
        class="form-control"
      />
    </div>
    <div class="form-group">
      <input
        type="text"
        v-model="firstName"
        placeholder="First Name"
        name="firstName"
        id="login-firstName"
        class="form-control"
      />
    </div>
    <div class="form-group">
      <input
        type="text"
        v-model="lastName"
        placeholder="Last Name"
        name="lastName"
        id="login-lastName"
        class="form-control"
      />
    </div>
    <button v-on:click="submitRegister" class="btn btn-success w-100">Sign In</button>
  </div>
</template>

<script>
import FormErrors from './FormErrors';
import { mapActions } from "vuex";

export default {
  name: "Register",
  components: {
    FormErrors
  },
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      email: "",
      firstName: "",
      lastName: "",
      errors: []
    };
  },
  methods: {
    ...mapActions(["register"]),
    submitRegister: function() {
      this.errors = [];

      if (!this.username) {
        this.errors.push("Username is required");
      }
      if (!this.password || !this.password2) {
        this.errors.push("Password is required");
      } else {
        if (this.password !== this.password2) {
          this.errors.push("Passwords are different");
        } else {
          if (this.password.length < 8) {
            this.errors.push("Password is too short");
          }
        }
      }
      if (!this.email) {
        this.errors.push("Email is required");
      } else {
        const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re.test(this.email)) {
          this.errors.push("Email is not valid");
        }
      }
      if (!this.firstName) {
        this.errors.push("First name is required");
      }
      if (!this.lastName) {
        this.errors.push("Last name is required");
      }

      if (this.errors.length === 0) {
        const registerData = {
          username: this.username,
          email: this.email,
          password: this.password,
          first_name: this.firstName,
          last_name: this.lastName
        }
        this.register(registerData);
      }
    }
  }
};
</script>

<style scoped>
</style>