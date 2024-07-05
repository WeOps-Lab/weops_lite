<template>
    <div id="app" style="min-width: 1280px;overflow-y: hidden;" v-loading.fullscreen="userInfoLoading">
        <nav-frame />
        <app-auth ref="appAuth"></app-auth>
    </div>
</template>

<script lang="ts">
    import appAuth from '@/components/appAuth/index.vue'
    import bus from './common/bus/index'
    import navFrame from '@/components/navFrame/index.vue'
    import { Component, Vue } from 'vue-property-decorator'

    @Component({
        name: 'app',
        components: {
            appAuth,
            navFrame
        }
    })
    export default class App extends Vue {
        timer: any = null
        userInfoLoading: boolean = false
        mounted() {
            window.onbeforeunload = () => {
                if (sessionStorage.getItem('show-login-modal')) sessionStorage.removeItem('show-login-modal')
            }
            this.$bus.$on('setAppLoading', res => {
                this.userInfoLoading = res
            })
            bus.$on('show-login-modal', (params) => {
                this.$refs.appAuth.showLoginModal(params)
            })
            bus.$on('close-login-modal', () => {
                this.$refs.appAuth.hideLoginModal()
                window.location.reload() // 当前页面刷新
            })
        }
        checkRoute(role) {
            if (this.$route.path === '/') {
                if (role === null) {
                    this.$router.push('/workManage')
                    this.$error('该用户无权限,请联系管理员')
                }
                if (role === 'user') {
                    this.$router.push('/ticketList')
                }
            }
        }
    }
</script>
<style lang="scss">
* {
    box-sizing: border-box;
}
.bk-card .bk-card-head-left {
    padding-left: 30px !important;
}
.bk-card-head {
    padding: 0 20px !important;
}
.bk-form-item.operator-form-item {
    position: absolute;
}
.btn-flex-wrapper {
    .bk-form-content {
        display: flex;
        margin-left: 154px;
        .bk-button + .bk-button {
            margin-left: 8px;
        }
    }
}
html, body {
    height: 100%;
    width: 100%;
    font-size: 14px;
}

::-webkit-scrollbar {
    width: 6px;
    height: 6px;
    background-color: rgba(255, 255, 255, .07);
}

::-webkit-scrollbar-thumb {
    -webkit-border-radius: 10px;
    border-radius: 10px;
    width: 6px;
    background: #CED5DB;
    -webkit-box-shadow: inset 0 0 6px #C4C6CC;
}

::-webkit-scrollbar-thumb:window-inactive {
    background-color: #CED5DB;
}
.full-load {
    z-index: 9999;
}
</style>
