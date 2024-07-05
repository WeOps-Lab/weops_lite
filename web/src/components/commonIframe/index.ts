import { Component, Prop, Vue } from 'vue-property-decorator'
@Component({
    name: 'wiki-iframe'
})
export default class WikiIframe extends Vue {
    @Prop({ type: String, default: '' }) url: string
    @Prop({ type: String, default: 'frame_reset' }) link: string

    loading: boolean = true
    mounted() {
        const close = this.closeLoading
        $('#frame-box').load(() => {
            close()
        })
    }
    closeLoading() {
        this.loading = false
    }
    // loadFrame函数是iframe加载完成后回调函数
    loadFrame() {
        // 获取iframe节点
        const iframeBox = document.getElementById('frame-box')
        // 获取iframe html文件
        const doc = iframeBox.contentWindow.document
        // 获取iframe html文件head
        const head = doc.getElementsByTagName('head')
        // 新建link标签
        const linkTag = document.createElement('link')
        // 设置link标签id
        linkTag.id = 'newstyle'
        // link标签引入css文件的地址
        linkTag.href = `${window.STATIC_URL}css/${this.link}.css` // 正式环境t换成o;
        // 设置link标签属性
        linkTag.setAttribute('rel', 'stylesheet')
        // 设置link标签属性
        linkTag.setAttribute('type', 'text/css')
        // 将link标签添加进iframe html文件的head里
        head[0].append(linkTag)
    }
}
