<template>
  <a :href="page">
    <div class="card">
      <div class="card-image" v-if="image">
        <figure class="image is-square">
          <img :src="image" />
        </figure>
      </div>
      <div class="card-content">
        <div class="content">
          <h5 class="is-4">{{ title }}</h5>
        </div>
      </div>
    </div>
  </a>
</template>

<script>
export default {
  props: ["title", "image", "page"],
};
</script>