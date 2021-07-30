<template>
  <nav class="navbar is-primary" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="~/assets/images/logowebapp.png" />
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarData"
        @click="show_nav = !show_nav"
        :class="{ 'is-active': show_nav }"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarData" class="navbar-menu" :class="{ 'is-active': show_nav }">
      <div class="navbar-end">
        <a class="navbar-item is-karla" href="/">
          Home
        </a>
        <a class="navbar-item is-karla" href="/information">
          Info
        </a>
        <a class="navbar-item is-karla" href="/comparison">
          Komparasi
        </a>
        <a class="navbar-item is-karla" href="/guide">
          Guide
        </a>
        <a class="navbar-item is-karla" href="/about">
          About
        </a>
        <a class="navbar-item is-karla">

        </a>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar.is-primary {
  background-color: #009999
}

.navbar.is-primary a.navbar-item:hover {
  background-color: #00b3b3
}
</style>

<script>
export default {
  data() {
    return {
      show_nav: false
    }
  }
};
</script>