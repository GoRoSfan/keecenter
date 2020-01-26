<template>
    <HomeSlot #main>
        <div class="context-header"><h2>Команда центру</h2></div>

    </HomeSlot>
</template>

<script>
    import HomeSlot from './Home';
    import $ from 'jquery'

    export default {
        name: 'AllEmployees',

        components: {
            HomeSlot,
        },

        data: function () {
            return {
                employee_list: '',
            }
        },

        created() {
            $.ajax({
                url: process.env.VUE_APP_API_URL + "/public/employees/",
                type: 'GET',
                data: {},
                success: function (response) {
                    this.employee_list = response.data;
                },
            });
        },
    };
</script>

<style scoped>

</style>
