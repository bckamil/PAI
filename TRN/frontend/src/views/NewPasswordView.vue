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
export default {

}
</script>

<style>

</style>