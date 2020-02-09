<template>
    <nav>
        <OneMenuItem
                v-for="(menu_item, index) in menu_list"
                :key="index"
                :menu-item-title="menu_item.title"
                :menu-item-link="menu_item.link"
                :sub-menu-list="menu_item.sub_menu_list"
        />
    </nav>
</template>

<script>
    import OneMenuItem from "./MenuItem";

    export default {
        name: "menu",
        components: {
            OneMenuItem
        },

        data() {
            return {
                menu_list: [
                    {
                        title: 'Новини',
                        link: 'news',
                        sub_menu_list: []
                    },
                    {
                        title: 'Учасникам',
                        link: '',
                        sub_menu_list: [
                            {
                                title: 'Студентам',
                                link: 'for_students'
                            },
                            {
                                title: 'Батькам',
                                link: 'for_parents'
                            },
                            {
                                title: 'Партнерам',
                                link: 'for_partners'
                            },
                        ]
                    },
                    {
                        title: 'Правова база',
                        link: 'legal',
                        sub_menu_list: []
                    },
                    {
                        title: 'Додатково',
                        link: '',
                        sub_menu_list: [
                            {
                                title: 'Про нас',
                                link: 'about'
                            },
                            {
                                title: 'Плани',
                                link: 'events'
                            },
                            {
                                title: 'Партнери',
                                link: 'partners'
                            },
                            {
                                title: 'Команда',
                                link: 'employees'
                            },
                            {
                                title: 'Контакти',
                                link: 'contact'
                            },
                        ]
                    },
                ]
            }
        }
    }
</script>

<style scoped>
    nav {
        display: flex;

        flex-flow: row wrap;
        justify-content: stretch;

        margin: 0;

        color: #3914AF;
        font-size: 1.2rem;

        background-color: #FFD300;
    }




</style>
