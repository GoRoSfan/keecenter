<template>
    <router-link tag="li" :to="{ path: subMenuLink}" class="sub-menu-item">
        <h4 class="menu-item-name">{{subMenuTitle}}</h4>
    </router-link>
</template>

<script>
    export default {
        name: "SubMenuItem",
        props: ['subMenuTitle', 'subMenuLink']
    }
</script>

<style scoped>
    .sub-menu-item {
        padding: 1vh 1vw;

        border-bottom: 2px solid #fff;

        cursor: pointer;
    }

    .sub-menu-item:hover {
        padding: 2vh 1vw;

        background-color: #7109AA;
    }

    .sub-menu-item .menu-item-name {
        color: #FFE773;
    }
</style>
