<template>
  <div class="field">
    <div class="file has-name is-large is-primary is-centered is-boxed">
      <label class="file-label">
        <input
          class="file-input"
          type="file"
          name="resume"
          accept="image/*"
          @change="uploadClient"
        />
        <span class="file-cta" v-if="!image">
          <span class="file-icon">
            <i class="fas fa-upload"></i>
          </span>
          <span class="file-label"> Choose a file… </span>
        </span>
        <figure class="image is-square" v-else>
          <img :src="preview" />
        </figure>
        <span class="file-name"> {{ filename }} </span>
      </label>
    </div>
  </div>
</template>

<style scoped>
.file.is-primary .file-cta {
  background-color: #009999
}

.file.is-primary .file-cta:hover {
  background-color: #00b3b3
}
</style>

<script>
export default {
  props: ["value"],
  emits: ["input"],
  data() {
    return {
      image: "",
      filename: "No File Uploaded",
      preview: "",
    };
  },
  methods: {
    uploadClient(e) {
      if (!e.target.files.length) return;

      this.image = e.target.files[0];
      this.filename = this.image.name;

      let reader = new FileReader();
      reader.onload = (e) => (this.preview = e.target.result);
      reader.readAsDataURL(this.image);

      this.$emit("input", this.image);
    },
  },
};
</script>