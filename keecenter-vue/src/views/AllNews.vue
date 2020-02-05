<template>
    <HomeSlot #main>
        <div class="context-header"><h2>Новини центру</h2></div>
        <div class="all-news-container">
            <article
                    v-for="one_new in news_list"
                    :key="one_new"
                    class="news-container"
            >
                <header class="news-header">
                    <cite>{{one_new.title}}</cite>
                    <time>{{one_new.post_date}}</time>
                </header>
                <div class="news-main">
                    <img :src="host + one_new.image" alt="Фотографія до новини" class="news-image">
                    <pre class="news-description">{{one_new.description}}</pre>
                </div>
                <footer class="news-footer" @click="go_to_detail(host + one_new.detail)">Детальніше</footer>
            </article>
        </div>
        <mu-flex justify-content="center" style="margin: 2vh 0;">
            <mu-pagination
                    :total="total_news"
                    :current.sync="current_page"
                    :page-size="page_size"
                    @change="page_change"
            ></mu-pagination>
        </mu-flex>
    </HomeSlot>
</template>

<script>
    import HomeSlot from './Home';
    import $ from 'jquery'

    export default {
        name: 'AllNews',

        components: {
            HomeSlot,
        },

        data() {
            return {
                news_list: '',
                host: process.env.VUE_APP_API_URL,
                current_page: 1,
                total_news: 10,
                page_size: 10,
            };
        },

        created() {
            $.ajax({
                url: this.host + '/public/news/',
                type: 'GET',
                data: {
                    'current_page': this.current_page,
                    'first_connection': true,
                },
                success: (response) => {
                    this.news_list = response.data;
                    this.total_news = response.total_news;
                    this.page_size = response.page_size;
                },
            });
        },

        methods: {

            page_change: function () {
                $.ajax({
                    url: this.host + '/public/news/',
                    type: 'GET',
                    data: {
                        'current_page': this.current_page,

                    },
                    success: (response) => {
                        this.news_list = response.data;
                    },
                });
            },

            go_to_detail: function (link) {
                location.href = link;
            },
        },
    };
</script>

<style scoped>
    .all-news-container {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        flex-direction: column;
        flex-wrap: nowrap;
        -webkit-flex-flow: column nowrap;
    }

    .all-news-container article {
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

    .all-news-container header {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;

        -webkit-flex-flow: row wrap;
        flex-flow: row wrap;
        justify-content: space-between;

        padding: 0.8vh 2vw;

        color: #3914AF;

        border-radius: 2vw 2vw 0 0;
        border-bottom: #FFD300 solid 1px;

        -webkit-box-shadow: inset 0 -1px #646464;
        -moz-box-shadow: inset 0 -1px #646464;
        box-shadow: inset 0 -1px #646464;

        background-color: #FFD300;
    }

    .all-news-container .news-header cite {
        align-self: center;

        font-style: normal;
        font-size: 1.5rem;
    }

    .all-news-container .news-header time {
        align-self: start;

        font-size: 1rem;
    }

    .all-news-container .news-main {
        padding: 1.5vh 1.5vw;

        color: #FFE773;
        text-align: left;
        font-size: 1.2rem;

        background-color: #311491;
    }

    .all-news-container .news-main img {
        width: 30%;
        float: right;
    }

    .all-news-container footer {
        text-align: center;

        padding: 1.5vh 2vw;
        border-radius: 0 0 2vw 2vw;

        color: #3914AF;
        font-size: 1.4rem;

        background-color: #FFD300;

        cursor: pointer;
    }

    .all-news-container footer:hover {
        background-color: #FFAA00;
    }
</style>
