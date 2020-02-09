<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<style>
    html {
        min-width: 240px;

        font-size: 15px;
    }


    body {
        margin: 0;
        display: flex;

        justify-content: center;
    }

    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    h2, h3, h4 {
        margin: 0;
    }

    h2 {
        font-size: 1.4rem;
        font-weight: 400;
    }

    #app {
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        margin-top: 5vmin;

        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        color: #FFE773;
        text-align: center;
    }

    .context-header {
        text-align: center;
        color: #FFE773;

        border-radius: 2.5vw 0;
        background-color: #311491;
    }

    @media (max-width: 1180px) {
        html {
            font-size: 12px;
        }
    }

    @media (max-width: 600px) {
        html {
            font-size: 10px;
        }
    }

    @media (max-width: 400px) {
        html {
            font-size: 8px;
        }
    }
</style>
