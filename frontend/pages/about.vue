<template>
  <section class="container">
    <section class="section">
      <div class="box">
        <img
          src="~/assets/images/logowebapp_dark.png"
          alt=""
          style="width: 240px"
        />
      </div>

      <div class="box">
        <h1 class="title is-5 is-karla">Tentang Aplikasi</h1>
        <p class="subtitle is-6 is-karla">
          <b>OCTDetection</b> adalah aplikasi untuk melakukan deteksi <b>citra OCT</b> yang diunggah ke dalam
          <b>4 kondisi (CNV, DME, Drusen, Normal)</b>. <b>OCTDetection</b> tersedia dalam <b>6 pilihan model</b> 
          yang dikembangkan menggunakan beberapa arsitektur state-of-the-art seperti
          <b>ResNet-18</b>, <b>InceptionV3</b>, dan <b>ResNeXt-50_32x4d</b> dan modifikasi. Aplikasi ini dikembangkan sebagai implementasi penelitian pada Proyek Akhir dengan judul<b>"Deteksi Penyakit Penyebab Kebutaan pada Citra OCT menggunakan Metode Convolutional Neural Network"</b>
        </p>

        <span class="title is-6">GitHub</span>
        <span class="icon-text">
          <span class="icon">
            <i class="fab fa-github"></i>
          </span>
          <span>
            <a href="https://github.com/arinalhaq/octdetection">arinalhaq/octdetection</a>
          </span>
        </span>
      </div>

      <div class="box">
        <div class="columns">
          <div class="column is-one-fifth">
            <image-card
              :image="require(`~/assets/images/about-arinalhaq.png`)"
              :is_square="true"
              :label="'Arinal Haq'"
              style="width: 172px"
            />
          </div>
          <div class="column">
            <h1 class="subtitle is-3"><b>Arinal Haq</b></h1>
            <p>Final Year Student</p>
            <p><b>Politeknik Elektronika Negeri Surabaya (PENS)</b></p>
            <p class="icon-text">
              <span class="icon">
                <i class="fab fa-github"></i>
              </span>
              <span>arinalhaq</span>
            </p>
            <p class="icon-text">
              <span class="icon">
                <i class="fab fa-linkedin"></i>
              </span>
              <span>arinalhaq</span>
            </p>
          </div>
        </div>
      </div>
    </section>
  </section>
</template>

<script>
export default {
  
};
</script>