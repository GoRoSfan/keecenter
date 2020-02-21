<template>
    <article>
        <header class="news-header">
            <cite>{{NewTitle}}</cite>
            <time>{{NewPostDate}}</time>
        </header>
        <div class="news-main">
            <img :src="host + NewImage" alt="Фотографія до новини" class="news-image">
            <pre class="news-description">{{NewDescription | truncateDescription(IsNewsPage, min_description_len, opened_description)}}</pre>
            <b v-if="IsNewsPage && NewDescription.length >= min_description_len"
               @click="opened_description = !opened_description"
            >
                {{opened_description ? 'Скрыть' : 'Подробнее'}}
            </b>
        </div>
    </article>
</template>

<script>
    export default {
        name: "NewItem",
        props: ['NewTitle', 'NewPostDate', 'NewImage', 'NewDescription', 'IsNewsPage'],
        data() {
            return {
                host: process.env.VUE_APP_API_URL,
                min_description_len: 350,
                opened_description: false,
            }
        },
        filters: {
            truncateDescription: (description, isNewsPage, min_description_len, isFullForm) => {
                if (isNewsPage) {
                    if (description.length > min_description_len && !isFullForm) {
                        return description.slice(0, min_description_len).concat(' ...')
                    } else {
                        return description
                    }
                } else {
                    return description.slice(0, min_description_len / 2).concat(' ...')
                }
            }
        }
    }
</script>

<style scoped>
    article {
        display: flex;

        flex-direction: column;

        margin: 2vh 0;
    }

    header {
        display: flex;

        flex-flow: row wrap;
        justify-content: space-between;

        padding: 0.8vh 2vw;

        color: #3914AF;

        border-radius: 2vw 2vw 0 0;
        border-bottom: #FFD300 solid 1px;

        box-shadow: inset 0 -1px #646464;

        background-color: #FFD300;
    }

    header cite {
        align-self: center;

        font-style: normal;
        font-size: 1.5rem;
    }

    aside header cite {
        font-size: 1.2rem;
    }

    header time {
        align-self: start;

        font-size: 1rem;
    }

    aside time {
        display: none;
    }

    .news-main {
        padding: 1rem 1.5vw;

        color: #FFE773;

        background-color: #311491;

        box-shadow: 2px 3px 1.5rem #ad8946;
    }

    .news-main img {
        width: 30%;
        float: right;
        padding: 0 0 2rem 1rem;
    }

    aside .news-main img {
        width: 90%;
        float: none;
        padding-left: 0;
    }

    .news-main pre {
        font-family: inherit;
        font-size: 1.2rem;
        text-align: left;

        word-break: normal;
    }

    aside .news-main pre {
        font-size: 0.85rem;
    }

    .news-main b {
        font-size: 1.3rem;

        cursor: pointer;
    }

    .news-main b:hover {
        color: #FFAA00;
    }

    .news-main b:active {
        color: #311491;
    }
</style>
