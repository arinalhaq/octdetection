<template>
  <section class="section">
    <div class="container">
      <breadcrumb
        :data_page="['Home', 'Information', 'Diseases']"
        :active="data.title"
      />
      <div class="box">
        <section class="section is-karla">
          <h1 class="title is-1 has-text-light">{{ data.title }}</h1>
          <h3 class="subtitle is-3 is-size-5-mobile has-text-light">{{ data.subtitle }}</h3>
        </section>
      </div>

      <div class="columns is-karla">
        <div class="column is-two-thirds">
          <section class="section">
            <div class="block content is-medium">
              <h3>Pengertian</h3>
              <p v-html="data.definition" />
            </div>
          </section>
          <section class="section">
            <div class="block content is-medium">
              <h3>Penyebab</h3>
              <p v-html="data.causes" />
            </div>
          </section>
          <section class="section">
            <div class="block content is-medium">
              <h3>Pengobatan</h3>
              <p v-html="data.treatment" />
            </div>
          </section>
          <section class="section">
            <div class="block content is-medium">
              <h3>Diagnosis</h3>
              <p v-html="data.diagnosis" />
            </div>
          </section>
          <section class="section">
            <div class="block content is-medium">
              <h3>Referensi</h3>
              <p v-html="data.references" />
            </div>
          </section>
        </div>
        <div class="column is-one-third">
          <image-card
            :image="require(`~/assets/images/${data.image}`)"
            :label="data.title + ' OCT Sampel'"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.box {
  background-color: #009999
}
</style>

<script>
import Breadcrumb from "~/components/Breadcrumb.vue";
import diseases from "~/assets/diseases.json";
export default {
  components: { Breadcrumb },
  data() {
    return {
      data: diseases[this.$route.params.disease],
      imgsrc: require("~/assets/images/CNV-1-Sampel.jpeg"),
    };
  },
};
</script>