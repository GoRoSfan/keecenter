<template>
    <HomeSlot #main>
        <div class="context-header"><h2>Партнери центру</h2></div>

    </HomeSlot>
</template>

<script>
    import HomeSlot from './Home';
    import $ from 'jquery'

    export default {
        name: 'Partners',

        components: {
            HomeSlot,
        },

        data: function () {
            return {
                partner_list: '',
            }
        },

        created() {
            $.ajax({
                url: process.env.VUE_APP_API_URL + "/public/partners/",
                type: 'GET',
                data: {},
                success: function (response) {
                    this.partner_list = response.data;
                },
            });
        },
    };
</script>

<style scoped>

</style>
