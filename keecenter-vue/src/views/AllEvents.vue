<template>
  <HomeSlot #main>
    <div class="context-header"><h2>План роботи центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';
  import $ from 'jquery'

  export default {
    name: 'AllEvents',

    components: {
      HomeSlot,
    },

    data: function () {
      return {
        events: '',
        count_pages: '',
      }
    },

    created: function () {
      $.ajax({
        url: process.env.VUE_APP_API_URL + '/public/events/',
        type: 'GET',
        data: {
          connection: true,
        },
        success: (response) => {
          this.events = response.data;
        },
      })
    },
  };
</script>

<style scoped>

</style>
