<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Про нас</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


  export default {
    name: 'About',

    components: {
      HomeSlot,
    },

    data: function () {
      return {}
    },
  };
</script>

<style scoped>

</style>
