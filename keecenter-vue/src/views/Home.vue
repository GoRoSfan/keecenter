<template>
    <mu-container class="main">
        <header>
            <div class="site-header">
                <h1>ХЕРСОНСЬКИЙ НАУКОВО-ДОСЛІДНИЦЬКИЙ ЦЕНТР УЧНІВСЬКОЇ ТА СТУДЕНТСЬКОЇ МОЛОДІ</h1>
            </div>
            <MainMenu/>
        </header>
        <div class="content-container">
            <main>
                <slot name="main"/>
            </main>
            <aside>
                <div class="context-header">Актуальна інформація</div>
                <div class="last-news">
                    <NewItem v-for="(last_one, index) in last_list"
                             :key="index"
                             :new-title="last_one.title"
                             :new-post-date="last_one.post_date"
                             :new-image-tg="last_one.image_url"
                             :new-image-media="last_one.image"
                             :new-description="last_one.description"
                    />
                </div>
                <div class="context-header">
                    <span>Корисні ресурси</span>
                </div>
                <div class="helpful-links"></div>
            </aside>
        </div>
        <footer/>
    </mu-container>
</template>

<script>
    import $ from 'jquery'
    import MainMenu from '@/components/MainMenu'
    import NewItem from "../components/NewItem";

    export default {
        name: 'Home',
        components: {
            MainMenu,
            NewItem
        },

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
        }

    };
</script>

<style scoped>

    .site-header {
        display: flex;

        flex-flow: row wrap;
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

    .content-container {
        display: flex;

        flex-flow: row wrap;
        justify-content: space-between;

        margin-top: 2vh;
    }

    .content-container > main {
        width: 70%;

        padding: 0;
        margin: 0;
    }

    .content-container > aside {
        display: flex;

        flex-direction: column;

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

    @media (max-width: 767px) {
        .content-container > main {
            width: 100%
        }

        .content-container > aside {
            display: none
        }
    }
</style>
