<template>
  <div class="field has-addons has-addons-centered">
    <div class="control">
      <a class="button is-static is-link"> {{ field }} </a>
    </div>
    <div class="control">
      <div class="select is-primary">
        <select :value="model" @change="$emit('input', $event.target.value)">
          <option disabled value="">{{ default_option }}</option>
          <option
            v-for="option in data_option"
            :value="option.value"
            :key="option.value"
          >
            {{ option.display }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>

<style scoped>
.select.is-primary select {
  border-color: #009999
}
</style>

<script>
export default {
  props: ["value", "data_option", "field", "default_option"],
  emits: ["input"],
  data() {
    return {
      model: '',
    };
  },
};
</script>