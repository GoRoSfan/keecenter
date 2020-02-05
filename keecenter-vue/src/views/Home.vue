<template>
    <mu-container class="main">
        <header>
            <div class="site-header">
                <h1>ХЕРСОНСЬКИЙ НАУКОВО-ДОСЛІДНИЦЬКИЙ ЦЕНТР УЧНІВСЬКОЇ ТА СТУДЕНТСЬКОЇ МОЛОДІ</h1>
            </div>
            <nav>
                <router-link tag="div" to="/news" class="main-menu-item">
                    <div class="menu-item-name">Новини</div>
                </router-link>
                <div class="main-menu-item">
                    <div class="menu-item-name">Учасникам</div>
                    <div class="sub-menu-list sub-menu-members">
                        <router-link tag="div" to="/for_students" class="sub-menu-item">
                            <div class="menu-item-name">Студентам</div>
                        </router-link>
                        <router-link tag="div" to="/for_parents" class="sub-menu-item">
                            <div class="menu-item-name">Батькам</div>
                        </router-link>
                        <router-link tag="div" to="/for_partners" class="sub-menu-item">
                            <div class="menu-item-name">Партнерам</div>
                        </router-link>
                    </div>
                </div>
                <router-link tag="div" to="/legal" class="main-menu-item">
                    <div class="menu-item-name">Правова база</div>
                </router-link>
                <div class="main-menu-item">
                    <div class="menu-item-name">Додатково</div>
                    <div class="sub-menu-list sub-menu-about">
                        <router-link tag="div" to="/about" class="sub-menu-item">
                            <div class="menu-item-name">Про нас</div>
                        </router-link>
                        <router-link tag="div" to="/events" class="sub-menu-item">
                            <div class="menu-item-name">Плани</div>
                        </router-link>
                        <router-link tag="div" to="/partners" class="sub-menu-item">
                            <div class="menu-item-name">Партнери</div>
                        </router-link>
                        <router-link tag="div" to="/employees" class="sub-menu-item">
                            <div class="menu-item-name">Каманда</div>
                        </router-link>
                        <router-link tag="div" to="/contact" class="sub-menu-item">
                            <div class="menu-item-name">Контакти</div>
                        </router-link>
                    </div>
                </div>
            </nav>
        </header>
        <div class="content-container">
            <main>
                <slot name="main"></slot>
            </main>
            <aside>
                <div class="context-header">Актуальна інформація</div>
                <div class="last-news">
                    <article
                            v-for="one_last in last_list"
                            :key="one_last"
                            class="last-container"
                    >
                        <header class="last-header">
                            <cite>{{one_last.title}}</cite>
                        </header>
                        <div class="last-main">
                            <img :src="host + one_last.image" alt="Фотографія до новини" class="last-image">
                            <pre class="last-description">{{one_last.description}}</pre>
                        </div>
                        <footer class="last-footer" @click="go_to_detail(host + one_last.detail)">Детальніше</footer>
                    </article>
                </div>
                <div class="context-header">
                    <span>Корисні ресурси</span>
                </div>
                <div class="helpful-links"></div>
            </aside>
        </div>
        <footer></footer>
    </mu-container>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: 'Home',

        props: {},

        data() {
            return {
                last_list: '',
                host: process.env.VUE_APP_API_URL,
            };
        },

        created() {
            $.ajax({
                url: this.host + '/public/news/',
                type: 'GET',
                data: {
                    'current_page': 1,

                },
                success: (response) => {
                    this.last_list = response.data;
                },
            });
        },

        methods: {
            go_to_detail: function (link) {
                location.href = link;
            },
        },

    };
</script>

<style scoped>
    /*.main{*/
    /*display: -webkit-box;*/
    /*display: -moz-box;*/
    /*display: -ms-flexbox;*/
    /*display: -webkit-flex;*/
    /*display: flex;*/

    /*flex-direction: column;*/
    /*flex-wrap: nowrap;*/
    /*-webkit-flex-flow: column nowrap;*/

    /*width: 90vw;*/
    /*}*/

    main > header {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        flex-direction: column;
        flex-wrap: wrap;
    }

    .site-header {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        -webkit-flex-flow: row wrap;
        justify-content: center;

        background-color: #311491;
    }

    .site-header h1 {
        padding: 0;
        margin: 2vh 1vw;

        font-size: 1.5rem;
        font-weight: 500;
        color: #FFE773;
    }

    header > nav {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        -webkit-flex-flow: row wrap;
        justify-content: stretch;

        margin: 0;

        list-style: none;

        color: #3914AF;
        font-size: 1.3rem;

        background-color: #FFD300;
    }

    nav .main-menu-item {
        position: relative;

        padding: 1.5vh 2vw;

        border: solid #000 0;
        border-right-width: 3px;

        cursor: pointer;

        -webkit-transition: 0.5s ease-in-out;
        -moz-transition: 0.5s ease-in-out;
        -o-transition: 0.5s ease-in-out;
        transition: 0.5s ease-in-out;
    }

    nav .main-menu-item:first-child {
        border-left-width: 3px;
    }

    nav .main-menu-item:hover {
        padding: 1.5vh 5vw;

        background-color: #FFAA00;
    }

    nav .menu-item-name {
        color: #3914AF;
    }

    nav .sub-menu-list {
        visibility: hidden;
        opacity: 0;

        position: absolute;
        top: 100%;
        left: 0;

        width: 100%;

        text-align: left;
        background-color: #311491;

        z-index: 10;

        -webkit-transition: 0.5s ease-in-out;
        -moz-transition: 0.5s ease-in-out;
        -o-transition: 0.5s ease-in-out;
        transition: 0.5s ease-in-out;
    }

    nav .main-menu-item:hover .sub-menu-list {
        visibility: visible;
        opacity: 1;
    }

    nav .sub-menu-item {
        padding: 1vh 1vw;

        border-bottom: 2px solid #fff;

        cursor: pointer;
    }

    nav .sub-menu-item:hover {
        padding: 2vh 1vw;

        background-color: #7109AA;
    }

    nav .sub-menu-item .menu-item-name {
        color: #FFE773;
    }

    .content-container {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        -webkit-flex-flow: row wrap;
        justify-content: space-between;

        margin-top: 2vh;
    }

    .content-container > main {
        width: 70%;

        padding: 0;
        margin: 0;
    }

    .content-container > aside {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        flex-direction: column;
        flex-wrap: nowrap;
        -webkit-flex-flow: column nowrap;

        width: 25%;
        min-height: 70vh;
    }

    .content-container > aside .context-header {
        margin: 1.5vh 0;

        font-size: 1.2rem;
    }

    .content-container > aside .context-header:first-child {
        margin-top: 0;
    }

    .last-news article {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        flex-direction: column;
        flex-wrap: nowrap;
        -webkit-flex-flow: column nowrap;

        margin: 2vh 0;
    }

    .last-news article:first-child {
        margin-top: 0;
    }

    .last-news header {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        -webkit-flex-flow: row wrap;
        flex-flow: row wrap;
        justify-content: center;

        padding: 0.8vh 2vw;

        color: #3914AF;

        border-radius: 2vw 2vw 0 0;
        border-bottom: #FFD300 solid 1px;

        -webkit-box-shadow: inset 0 -1px #646464;
        -moz-box-shadow: inset 0 -1px #646464;
        box-shadow: inset 0 -1px #646464;

        background-color: #FFD300;
    }

    .last-news .last-header cite {
        font-style: normal;
        font-size: 1.1rem;
    }

    .last-news .last-main {
        padding: 1.5vh 1.5vw;

        color: #FFE773;
        text-align: left;
        font-size: 0.8rem;

        background-color: #311491;
    }

    .last-news .last-main img {
        width: 35%;
        float: right;

        padding-bottom: 0.4vh;
    }

    .last-news footer {
        text-align: center;

        padding: 1.5vh 2vw;
        border-radius: 0 0 2vw 2vw;

        color: #3914AF;
        font-size: 1rem;

        background-color: #FFD300;

        cursor: pointer;
    }

    .last-news footer:hover {
        background-color: #FFAA00;
    }

    @media (max-width: 767.5px) {
        .content-container > main {
            width: 100%
        }

        .content-container > aside {
            display: none
        }
    }
</style>
