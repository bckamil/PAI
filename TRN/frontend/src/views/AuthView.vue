<template>
  <div class="login-box p-3 pt-4">
    <div class="mb-3">
      <Login v-if="showLogin"/>
      <Register v-if="showRegister" />
      <ResetPassword v-if="showResetPassword" />
    </div>
    <div class="mb-1">
      <button
        v-on:click="setShowFalse(); showLogin = true;"
        v-if="!showLogin"
        class="btn btn-outline-info w-100 mb-2"
      >Login</button>
      <button
        v-on:click="setShowFalse(); showRegister = true;"
        v-if="!showRegister"
        class="btn btn-outline-info w-100 mb-2"
      >Register</button>
      <button
        v-on:click="setShowFalse(); showResetPassword = true;"
        v-if="!showResetPassword"
        class="btn btn-outline-info w-100 mb-2"
      >Reset password</button>
    </div>
  </div>
</template>

<script>
import Login from "../components/Login";
import Register from "../components/Register";
import ResetPassword from "../components/ResetPassword";

export default {
  name: "AuthView",
  components: {
    Login,
    Register,
    ResetPassword
  },
  data() {
    return {
      showLogin: true,
      showRegister: false,
      showResetPassword: false
    };
  },
  methods: {
    setShowFalse: function() {
      this.showLogin = false;
      this.showRegister = false;
      this.showResetPassword = false;
    }
  }
};
</script>

<style>
.login-box {
  border: 1px solid #2f3033;
  border-radius: 25px;
  min-width: 35%;
  top: 50%;
  left: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
  box-sizing: border-box;
  text-align: center;
}
</style>