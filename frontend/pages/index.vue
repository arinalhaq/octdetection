<template>
  <section class="hero is-fullheight-with-navbar">
    <div class="hero-body">
      <div class="container has-text-centered is-karla">
        <file-upload v-model="image" />
        <select-model-field
          :data_option="model_list"
          :field="'model'"
          :default_option="'Select Model'"
          v-model="model"
        />
        <div class="field is-grouped-centered">
          <div class="control">
            <button type="button" class="button is-primary" @click="postServer">
              PREDICT
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="content has-text-centered pb-5">
      <p><strong>OCTDetection</strong> by <a href="">Arinal Haq</a></p>
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
      model: "",
      model_list: [
        { display: "Inception V3", value: "inceptionv3" },
        { display: "ResNet18", value: "resnet18" },
        { display: "ResNeXt50", value: "resnext50" },
        { display: "Inception V3 (modified)", value: "inceptionv3_bn" },
        { display: "ResNet18 (modified)", value: "resnet18_bn" },
        { display: "ResNeXt50 (modified)", value: "resnext50_bn" },
      ],
    };
  },

  methods: {
    postServer(e) {
      if (!this.image) {
        alert("Mohon maaf anda belum Menggunggah citra");
        return;
      }

      let formData = new FormData();
      formData.append("img", this.image);

      this.$nuxt.$loading.start();
      this.$axios
        .$post("/api/prod/predict", formData, {
          params: { model: this.model },
        })
        .then((response) => {
          this.$nuxt.$loading.finish();
          this.$store.commit("add", response);
          this.$store.commit("addimage", this.image);
          this.$router.push("/result");
        })
        .catch((e) => {
          this.$nuxt.$loading.finish();
          alert("Internal Server Error");
        });
    },
  },
};
</script>
