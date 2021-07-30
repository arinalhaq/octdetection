<template>
  <section class="section">
    <div class="container">
      <h5 class="title is-3">Komparasi<br />Model <b>OCTDetection</b></h5>
      <div class="columns is-6 is-centered">
        <div class="column is-one-fifth is-karla">
          <file-upload v-model="image" :class="'mb-3'" />
          <div
            class="field is-grouped is-grouped-centered"
            v-for="n in 3"
            :key="n"
          >
            <div
              class="control"
              v-for="value in modelused.slice(n * 2 - 2, n * 2)"
              :key="'menu' + value"
            >
              <label class="checkbox">
                <input
                  type="checkbox"
                  v-model="model"
                  :id="'key' + value"
                  :value="value"
                />
                <span class="subtitle is-6">{{ value }}</span>
              </label>
            </div>
          </div>
          <div class="field is-grouped-centered">
            <div class="control">
              <button
                type="button"
                class="button is-primary"
                :style="'width: 100%;'"
                @click="postUpload"
              >
                COMPARE
              </button>
            </div>
          </div>
        </div>
        <div class="column" v-if="comparation">
          <div class="columns is-multiline is-centered is-vcentered">
            <div
              class="column is-one-third"
              v-for="(value, model) in comparation"
              :key="model"
            >
              <div class="box">
                <h3
                  class="title is-5 mb-1"
                  style="color: rgba(0, 0, 226, 0.83)"
                >
                  {{ model }}
                </h3>
                <h1 class="title is-3 mb-0">
                  <b>{{ value.class }}</b>
                </h1>
                <h3 class="is-size-7-mobile is-size-5">{{ value.detail }}</h3>
                <p class="mt-3 is-7">probabilities :</p>
                <bar-chart
                  :chart-data="prBar(value.probabilities)"
                  :options="options"
                  :style="'height: 180px; width:100%;'"
                />
                <h3 class="title is-6">Deskripsi Hasil</h3>
                <p class="subtitle is-6">
                  Hasil Deteksi untuk citra OCT adalah
                  <b>{{ value.detail }}</b> menggunakan model
                  <b>{{ model }}</b> dengan tingkat keyakinan
                  <b>{{ confidenceScore(value.probabilities) }} %</b>
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.button.is-primary {
  background-color: #009999;
}
.button.is-primary:hover {
  background-color: #00b3b3;
}
</style>

<script>
export default {
  data() {
    return {
      image: "",
      model: [],
      modelused: [
        "resnet18",
        "inceptionv3",
        "resnext50",
        "resnet18_bn",
        "inceptionv3_bn",
        "resnext50_bn",
      ],
      data: {
        labels: ["CNV", "DME", "DRUSEN", "NORMAL"],
        datasets: [
          {
            label: "retina disease probability",
            data: [],
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
      comparation: "",
    };
  },
  methods: {
    postUpload() {
      if (!this.image) {
        alert("Mohon maaf anda belum Menggunggah citra");
        return;
      }

      if (this.model.length <= 1) {
        alert("Pilih model lebih dari 1 untuk dibandingkan");
        return this.model;
      }

      let formData = new FormData();
      formData.append("image", this.image);

      this.$nuxt.$loading.start();
      this.$axios
        .$post("/api/prod/comparison", formData, {
          params: { model: this.model.toString() },
        })
        .then((response) => {
          this.$nuxt.$loading.finish();
          this.comparation = response;
        })
        .catch((e) => {
          this.$nuxt.$loading.finish();
          alert("Internal Server Error\nMessage: " + e);
        });
    },

    prBar(model) {
      return {
        labels: ["CNV", "DME", "DRUSEN", "NORMAL"],
        datasets: [
          {
            label: "retina disease probability",
            data: model,
            backgroundColor: "rgba(0, 0, 226, 0.83)",
          },
        ],
      };
    },

    confidenceScore(data) {
      return Math.max.apply(null, data);
    },
  },
};
</script>