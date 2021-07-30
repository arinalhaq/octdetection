<template>
  <div class="modal is-active">
    <div class="modal-background" @click="$emit('close')"></div>
    <div class="modal-content">
      <p class="image">
        <img :src="image" alt="" />
      </p>
    </div>
    <button class="modal-close is-large" @click="$emit('close')"></button>
  </div>
</template>

<script>
export default {
  props: ["image"],
};
</script>