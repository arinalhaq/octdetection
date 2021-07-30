<template>
  <section class="section">
    <div class="container has-text-centered">
      <h5 class="title is-3"><b>Pusat</b><br/>Informasi</h5>
      <select-model-field
        :data_option="categories"
        :field="'Category'"
        :default_option="'Select Category'"
        v-model="category"
        :class="'mb-5'"
      />
      <div class="columns is-multiline is-karla">
        <div
          class="column is-one-third"
          v-for="data in display_data"
          :key="data.title.toLowerCase()"
        >
          <info-image-card
            :title="data.title"
            :image="require(`~/assets/images/${data.image}`)"
            :page="'/information/'+category+'s/'+data.title.toLowerCase()"

            v-if="data.image"
          />
          <info-image-card
            :title="data.title"
            :page="'/information/'+category+'s/'+data.title.toLowerCase()"

            v-else
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import diseases from "~/assets/diseases.json"
import models from "~/assets/models.json"
export default {
  data() {
    return {
      category: "",
      categories: [
        { display: "Diseases", value: "disease" },
        { display: "Models", value: "model" },
      ]
    };
  },

  computed: {
    display_data: function () {
      if (this.category == "disease") {
        return diseases;
      } else if (this.category == "model") {
        return models;
      }
    },
  },
};
</script>