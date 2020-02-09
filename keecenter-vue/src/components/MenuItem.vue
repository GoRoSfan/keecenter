<template>
    <router-link tag="div" :to="{ path: menuItemLink}" class="main-menu-item">
        <h3 class="menu-item-name">{{menuItemTitle}}</h3>
        <ul class="sub-menu-list">
            <SubMenuItem
                    v-for="(sub_menu_item, index) in subMenuList"
                    :key="index"
                    :sub-menu-title="sub_menu_item.title"
                    :sub-menu-link="sub_menu_item.link"
            />
        </ul>
    </router-link>
</template>

<script>
    import SubMenuItem from "./SubMenuItem";

    export default {
        name: "MenuItem",
        components: {
            SubMenuItem
        },

        props: ['menuItemTitle', 'menuItemLink', 'subMenuList']
    }
</script>

<style scoped>
    .main-menu-item {
        position: relative;

        padding: 1.5vh 2vw;

        border: solid #000 0;
        border-right-width: 3px;

        cursor: pointer;

        transition: 0.5s ease-in-out;
    }

    .main-menu-item:first-child {
        border-left-width: 3px;
    }

    .main-menu-item:hover {
        padding: 1.5vh 5vw;

        background-color: #FFAA00;
    }

    .menu-item-name {
        color: #3914AF;
    }

    .sub-menu-list {
        visibility: hidden;
        opacity: 0;

        position: absolute;
        top: 100%;
        left: 0;

        width: 100%;

        text-align: left;
        background-color: #311491;

        z-index: 10;

        transition: 0.5s ease-in-out;
    }

    .main-menu-item:hover .sub-menu-list {
        visibility: visible;
        opacity: 1;
    }
</style>
