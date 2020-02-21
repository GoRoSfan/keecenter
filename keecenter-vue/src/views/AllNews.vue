<template>
    <HomeSlot #main>
        <div class="context-header"><h2>Новини центру</h2></div>
        <div class="all-news-container">
            <NewItem
                    v-for="(one_new, index) in news_list"
                    :key="index"
                    :new-title="one_new.title"
                    :new-post-date="one_new.post_date"
                    :new-image="one_new.image"
                    :new-description="one_new.description"
                    :is-news-page="true"
            />
<!--            <article-->
<!--                    v-for="(one_new, index) in news_list"-->
<!--                    :key="index"-->
<!--                    class="news-container"-->
<!--            >-->
<!--                <header class="news-header">-->
<!--                    <cite>{{one_new.title}}</cite>-->
<!--                    <time>{{one_new.post_date}}</time>-->
<!--                </header>-->
<!--                <div class="news-main">-->
<!--                    <img :src="host + one_new.image" alt="Фотографія до новини" class="news-image">-->
<!--                    <pre class="news-description">{{one_new.description}}</pre>-->
<!--                </div>-->
<!--                <footer class="news-footer" @click="go_to_detail(host + one_new.detail)">Детальніше</footer>-->
<!--            </article>-->
        </div>
        <mu-flex justify-content="center" style="margin: 2vh 0;">
            <mu-pagination
                    :total="total_news"
                    :current.sync="current_page"
                    :page-size="page_size"
                    @change="page_change"
            />
        </mu-flex>
    </HomeSlot>
</template>

<script>
    import HomeSlot from './Home';
    import NewItem from "../components/NewItem";
    import $ from 'jquery'

    export default {
        name: 'AllNews',

        components: {
            HomeSlot,
            NewItem
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

            // go_to_detail: function (link) {
            //     location.href = link;
            // },
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

    /*.all-news-container footer {*/
    /*    text-align: center;*/

    /*    padding: 1.5vh 2vw;*/
    /*    border-radius: 0 0 2vw 2vw;*/

    /*    color: #3914AF;*/
    /*    font-size: 1.4rem;*/

    /*    background-color: #FFD300;*/

    /*    cursor: pointer;*/
    /*}*/

    /*.all-news-container footer:hover {*/
    /*    background-color: #FFAA00;*/
    /*}*/
</style>
