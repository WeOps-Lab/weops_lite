import { Vue, Component, Prop } from 'vue-property-decorator'
import draggable from 'vuedraggable'
import uuid from 'uuid'
@Component({
    name: 'menu-item',
    components: {
        draggable
    }
})
export default class MenuItem extends Vue {
    @Prop({ type: Array, default: [] }) allMenu: any
    @Prop({ type: Array, default: [] }) menu: any
    menuList: any = this.menu
    editConfrim: boolean = false
    handleChange() {
        this.$emit('change', this.menuList)
    }
    changeMenuItem(menu, data) {
        data.children = menu
    }
    handleEditStatus(data, status) {
        if (data.isUrl) {
            this.$emit('edit-external-chain', data)
        } else {
            this.$set(data, 'isEdit', status)
        }
    }
    editExternalChain(data) {
        this.$emit('edit-external-chain', data)
    }
    handleConfirmEdit(data) {
        if (!data.name) {
            this.editConfrim = true
            return false
        }
        if (!data.isPage) {
            data.id = uuid()
        }
        data.isEdit = false
        this.editConfrim = false
        this.$emit('change', this.menuList)
    }
    deleteMenuItem(data) {
        this.$emit('delete', data)
    }
    handleDelete(data) {
        const deleteItem = (data, id) => {
            for (let i = 0; i < data.length; i++) {
                const item = data[i]
                if (item.id === id) {
                    data.splice(i, 1)
                    return true
                }
                if (item.children?.length) {
                    const deleted = deleteItem(item.children, id)
                    if (deleted) {
                        return true
                    }
                }
            }
            return false
        }
        deleteItem(this.allMenu, data.id)
        this.$emit('delete', data)
        // 判断删除的这个目录是否存在系统设置这个页面,存在的话将除系统设置的页面删掉
        let sysMenu = {}
        const hasSysSettingId = (item) => {
            if (item.id === 'SysSetting') {
                sysMenu = item
                return true
            }
            if (item.children && Array.isArray(item.children)) {
                for (const child of item.children) {
                    if (hasSysSettingId(child)) {
                        return true
                    }
                }
            }
            return false
        }
        if (hasSysSettingId(data)) {
            this.menuList.push(sysMenu)
            this.$emit('change', this.menuList)
        }
    }
}
