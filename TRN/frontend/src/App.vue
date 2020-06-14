<template>
  <div id="app" class="text-left">
    <div v-if='this.$route.path !== "/login"' id="nav">
      <NavBar />
    </div>
    <div class="container">
      <router-view/>      
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar';
import { mapActions } from 'vuex';

export default {
  name: 'App',
  created() {
    if (this.$store.getters.isAuthenticated) {
      this.fetchUserMe()
    }
  },
  methods: {
    ...mapActions(['fetchUserMe'])
  },
  components: {
    NavBar,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

@media only screen and (max-width: 600px) {
   .w-sm-100 {
    width: 100%;
  }
}

.theme-success .vdatetime-popup__header,
.theme-success .vdatetime-calendar__month__day--selected > span > span,
.theme-success .vdatetime-calendar__month__day--selected:hover > span > span {
  background: #5cb85c;
}

.theme-success .vdatetime-month-picker__item--selected,
.theme-success .vdatetime-year-picker__item--selected,
.theme-success .vdatetime-time-picker__item--selected,
.theme-success .vdatetime-popup__actions__button {
  color: #5cb85c;
}
a:hover {
  text-decoration: none;
  color: black;
}
a {
  color: #444;
}
</style>
