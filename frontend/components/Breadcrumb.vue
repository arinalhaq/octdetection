<template>
    <nav class="breadcrumb is-centered" aria-label="breadcrumbs">
        <ul>
          <li v-for="data in data_page" :key="data"><a href="">{{ data }}</a></li>
          <li class="is-active"><a href="" aria-current="page">{{ active }}</a></li>
        </ul>
      </nav>
</template>

<script>
export default {
    props: ['data_page', 'active']
}
</script>