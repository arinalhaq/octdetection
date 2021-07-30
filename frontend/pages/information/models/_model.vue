<template>
  <section class="section">
    <div class="container">
      <breadcrumb
        :data_page="['Home', 'Information', 'Models']"
        :active="data.title"
      />
      <div class="box">
        <section class="section is-karla">
          <h1 class="title is-1 has-text-light">{{ data.title }}</h1>
        </section>
      </div>

      <div class="columns is-karla">
        <div class="column is-two-thirds">
          <section class="section">
            <div class="content is-medium">
              <h3>Pengertian</h3>
              <p v-html="data.description" />
            </div>
          </section>
          <section class="section">
            <div class="content is-medium">
              <h3>Performa</h3>
              <h5>OCT2017</h5>
              <table class="table">
                <thead>
                  <tr>
                    <th>Model</th>
                    <th>Accuracy</th>
                    <th>Sensitivity</th>
                    <th>Spesificity</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="values, model in data.performance" :key="model">
                    <td>{{ model }}</td>
                    <td v-for="value in values" :key="value">{{ value }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </section>
          <section class="section">
            <div class="content is-medium">
              <h3>Referensi</h3>
              <p v-html="data.references" />
            </div>
          </section>
        </div>
        <div class="column is-one-third">
          <image-card
            :image="require(`~/assets/images/${data.image}`)"
            :label="data.img_caption"
          />
          <section class="section">
            <h1 class="title is-3">Arsitektur</h1>
            <button
              class="button is-colored"
              v-for="value, index in data.image_model"
              :key="value"
              @click="showGallery(value)"
            >
              {{ index }}
            </button>
          </section>
        </div>
      </div>
      <image-gallery
        v-show="show_gallery"
        @close="show_gallery = false"
        :image="display_gallery"
      />
    </div>
  </section>
</template>

<style scoped>
.box {
  background-color: #009999;
}

.is-colored {
  color: white;
  background-color: #009999;
}
</style>

<script>
import Breadcrumb from "~/components/Breadcrumb.vue";
import models from "~/assets/models.json";
export default {
  components: { Breadcrumb },
  data() {
    return {
      data: models[this.$route.params.model],
      imgsrc: "",
      show_gallery: false,
      display_gallery: "",
    };
  },
  methods: {
    showGallery(image_source) {
      this.show_gallery = true;
      this.display_gallery = require(`~/assets/images/${image_source}`);
    },
  },
};
</script>