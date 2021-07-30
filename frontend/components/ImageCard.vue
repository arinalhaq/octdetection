<template>
  <div class="card">
    <div class="card-image">
      <figure class="image" :class="{ 'is-square': is_square }">
        <img :src="image" />
      </figure>
    </div>
    <div class="has-text-centered">
      <span class="title is-size-6">{{ label }}</span>
    </div>
  </div>
</template>

<script>
export default {
  props: ["image", "label", "is_square"],
};
</script>