<template>
  <section class="hero is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container">
        <h5 class="title is-3">Hasil<br /><b>OCTDetection</b></h5>
        <div class="columns is-centered is-vcentered">
          <div class="column is-one-third">
            <image-card :image="image" :is_square="true" />
          </div>
          <div class="column is-one-third">
            <div class="box">
              <h3 class="title is-5 mb-1" style="color: rgba(0, 0, 226, 0.83)">
                model: {{ model }}
              </h3>
              <h1 class="title is-1 mb-0">
                <b>{{ prediction }}</b>
              </h1>
              <h3 class="is-size-5">{{ description }}</h3>

              <p class="mt-3 is-7">probabilities :</p>
              <bar-chart
                :chart-data="data"
                :options="options"
                :style="'height: 180px; width:100%; margin-bottom: 11px;'"
              />
              <h3 class="title is-6">Deskripsi Hasil</h3>
              <p class="subtitle is-6">
                Hasil Deteksi untuk citra OCT adalah
                <b>{{ description }}</b> menggunakan model
                <b>{{ model }}</b> dengan tingkat keyakinan
                <b>{{ confidenceScore(cpvalue) }}%</b>
              </p>
            </div>
          </div>
          <div class="column is-one-third"></div>
        </div>
        <div v-if="infdisease">
          <div class="box">
            <h5 class="title is-3 mb-3">Informasi terkait <b>penyakit</b></h5>
            <div class="columns">
              <div class="column is-one-third is-karla">
                <div class="content is-medium">
                  <h5>Definisi</h5>
                  <div class="subtitle is-6" v-html="infdisease.definition" />
                </div>
              </div>
              <div class="column is-one-third is-karla">
                <div class="content is-medium">
                  <h5>Penyebab</h5>
                  <div class="subtitle is-6" v-html="infdisease.causes" />
                </div>
              </div>
              <div class="column is-one-third is-karla">
                <div class="content is-medium">
                  <h5>Pengobatan</h5>
                  <div class="subtitle is-6" v-html="infdisease.treatment" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import diseases from "~/assets/diseases.json";
export default {
  data() {
    return {
      image: "",
      prediction: "Predicted Class",
      model: "inceptionv3",
      description: "description",
      cpvalue: [],
      data: {
        labels: ["CNV", "DME", "DRUSEN", "NORMAL"],
        datasets: [
          {
            label: "retina disease probability",
            data: this.$store.state.prediction.probabilities,
            backgroundColor: "rgba(0, 0, 226, 0.83)",
          },
        ],
      },
      options: {
        responsive: true,
        elements: {
          rectangle: {
            borderWidth: 6,
          },
        },
        legend: {
          display: false,
        },
        maintainAspectRatio: false,
      },
      infdisease: "",
    };
  },

  methods: {
    loadImage(image) {
      var reader = new FileReader();
      reader.onload = (e) => (this.image = e.target.result);
      reader.readAsDataURL(image);
    },

    confidenceScore(data) {
      return Math.max.apply(null, data);
    },
  },

  mounted() {
    if (this.$store.state.image) {
      this.loadImage(this.$store.state.image); // ### load from image upload
    }

    this.model = this.$store.state.prediction.model;
    this.prediction = this.$store.state.prediction.class;
    this.description = this.$store.state.prediction.detail;
    this.cpvalue = this.$store.state.prediction.probabilities;
    this.infdisease = diseases[this.prediction.toLowerCase()];
  },

  beforeCreate() {
    if (!this.$store.state.prediction) {
      this.$router.push("/");
    }
  },
};
</script>