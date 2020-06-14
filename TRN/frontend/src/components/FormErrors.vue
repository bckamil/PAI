<template>
      <div v-if="errors.length > 0" class="bg-warning pt-1 mb-2 errors-list">
      <ul style="text-align: left;">
        <li class="error-msg" v-for="error in errors" :key="error">
          <span>{{ error }}</span>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: "FormErrors",
  props: {
    errors: {
      required: true
    }
  }
}
</script>

<style>

</style>