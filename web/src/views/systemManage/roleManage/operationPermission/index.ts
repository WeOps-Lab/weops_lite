import { Vue, Component, Prop } from 'vue-property-decorator'
import { removeItemsWithId, getMenuIdsAndOperateIds, getMenuListByAllowedKeys } from '@/common/dealMenu'
@Component
export default class OperationPermission extends Vue {
    @Prop({
        type: Object,
        default: () => ({})
    })
    role: any | undefined
    menuList = []
    menuLoading: boolean = false
    checkAuthMenusIds = []
    operateAuthMenusIds = []
    // 保存角色的原始的权限
    permissions = {}
    // 查看权限的映射, 菜单Id:具体操作名称
    checkMap = {}
    get user() {
        return this.$store.state.permission.user
    }
    mounted() {
        this.menuList = JSON.parse(JSON.stringify(this.$store.state.permission.menuList))
        this.getMenusList()
        this.getRoleMenus()
    }
    getMenusList() {
        this.menuList = JSON.parse(JSON.stringify(this.$store.state.permission.menuList))
        // 隐藏角色管理菜单
        const ONLY_ADMIN_HAS_MENUS = ['SysRole']
        removeItemsWithId(this.menuList, ONLY_ADMIN_HAS_MENUS)
        this.handleMenus(this.menuList)
    }
    getLatestMenu() {
        this.checkAuthMenusIds = []
        this.operateAuthMenusIds = []
        this.getSelectMenusIds(this.menuList)
        this.$emit('getLatestMenu', {
            checkAuthIds: this.checkAuthMenusIds,
            operateAuthIds: this.operateAuthMenusIds
        })
        // 将角色权限数据传给父组件
        this.$emit('getPermissions', this.permissions)
    }
    getSelectMenusIds(data) {
        data.forEach(item => {
            if (item.children) {
                this.getSelectMenusIds(item.children)
            }
            const obj = {
                menuId: item.id,
                operate_ids: []
            }
            item.auth.forEach(tex => {
                if (tex.type === 'check' && tex.value) {
                    this.checkAuthMenusIds.push(item.id)
                }
                if (!item.children) {
                    if (tex.type === 'operate' && tex.value) {
                        obj.operate_ids.push(tex.key)
                    }
                }
            })
            if (obj.operate_ids.length) {
                this.operateAuthMenusIds.push(obj)
            }
        })
    }
    setExpandStatus(item) {
        if (item.children) {
            this.$set(item, 'isExpand', !item.isExpand)
        }
    }
    getIndeterminateValue(item, type) {
        if (item.children) {
            const allTypeArr = []
            item.children.forEach(nev => {
                nev.auth.forEach(c => {
                    if (c.type === type) {
                        allTypeArr.push(c)
                    }
                })
            })
            item.auth.forEach(nev => {
                if (nev.type === type) {
                    nev.value = allTypeArr.every(c => c.value)
                    nev.isIndeterminate = !(allTypeArr.every(c => c.value) || allTypeArr.every(c => !c.value)) || !!allTypeArr.find(c => c.isIndeterminate)
                }
            })
            item.isChecked = item.auth.every(nev => nev.value)
            item.isIndeterminate = !(item.auth.every(nev => nev.value) || item.auth.every(nev => !nev.value)) || !!item.auth.find(nev => nev.isIndeterminate)
        }
    }
    handleOperateChecked(item, type, isInit?) {
        item.isChecked = item.auth.every(tex => tex.value)
        item.auth.forEach(tex => {
            if (tex.type === type) {
                tex.isIndeterminate = false
            }
        })
        if (type === 'operate' && item.auth.find(tex => tex.type === 'operate' && tex.value) && !isInit) {
            item.auth.forEach(tex => {
                if (tex.type === 'check') {
                    tex.value = true
                    this.setCheckedStatus(item, tex.value, 'check')
                    this.handleParentChecked(item, 'check')
                }
                const manageAll = item.auth.find(nev => nev.key === 'manageAllArticlesAuth')
                if (tex.key === 'manageMyArticlesAuth' && manageAll.value) {
                    tex.value = true
                    this.setCheckedStatus(item, tex.value, 'check')
                    this.handleParentChecked(item, 'check')
                }
            })
        }
        if (type === 'check' && !item.auth.find(tex => tex.type === 'check').value && !isInit) {
            item.auth.forEach(tex => {
                if (tex.type === 'operate') {
                    tex.value = false
                    this.setCheckedStatus(item, tex.value, 'operate')
                    this.handleParentChecked(item, 'operate')
                }
            })
        }
        if (!item.children) {
            item.isIndeterminate = !(item.auth.every(tex => tex.value) || item.auth.every(tex => !tex.value))
        } else {
            this.setCheckedStatus(item, item.auth.find(tex => tex.type === type).value, type)
        }
        this.handleParentChecked(item, type)
    }
    handleParentChecked(item, type?) {
        if (item.parentId) {
            const parent = this.findItemById(item.parentId, this.menuList)
            if (type) {
                this.getIndeterminateValue(parent, type)
            } else {
                this.handleAllCheckValue(parent)
            }
            if (parent.parentId) {
                this.handleParentChecked(parent, type)
            }
        }
    }
    handleAllCheckValue(item) {
        if (item.children) {
            item.isChecked = item.children.every(tex => tex.isChecked)
            item.isIndeterminate = !!item.children.find(tex => tex.isChecked) || !!item.children.find(tex => tex.isIndeterminate)
            item.auth.forEach(tex => {
                const arr = []
                item.children.forEach(nev => {
                    nev.auth.forEach(c => {
                        if (c.type === tex.type) {
                            arr.push(c)
                        }
                    })
                })
                tex.value = arr.every(nev => nev.value)
                const authTarget = arr.every(nev => nev.value) || arr.every(nev => !nev.value)
                tex.isIndeterminate = !authTarget || !!arr.find(tex => tex.isIndeterminate)
            })
        }
    }
    handleMenuChecked(item) {
        this.setCheckedStatus(item, item.isChecked, 'all')
    }
    setCheckedStatus(item, status, type, isLastLevel?) {
        if (item.children) {
            item.children.forEach(tex => {
                if (type === 'all') {
                    this.$set(tex, 'isChecked', status)
                }
                this.setCheckedStatus(tex, status, type)
            })
        }
        if (type === 'all') {
            item.auth.forEach(tex => {
                this.$set(tex, 'value', status)
            })
            this.$set(item, 'isIndeterminate', false)
            this.handleParentChecked(item)
        } else {
            item.auth.forEach(tex => {
                if (tex.type === type) {
                    tex.value = status
                }
            })
            item.isChecked = item.auth.every(tex => tex.value)
            item.isIndeterminate = !(item.auth.every(tex => tex.value) || item.auth.every(tex => !tex.value))
        }
    }
    handleMenus(data, parentId?) {
        data.forEach(item => {
            if (parentId) {
                this.$set(item, 'parentId', parentId)
            }
            this.$set(item, 'isChecked', false)
            this.$set(item, 'isIndeterminate', false)
            item?.auth.forEach(tex => {
                this.$set(tex, 'isIndeterminate', false)
            })
            if (item.children) {
                this.$set(item, 'isExpand', false)
                this.handleMenus(item.children, item.id)
            }
        })
    }
    findItemById(id, list) {
        let res = list.find(item => item.id === id)
        if (res) {
            return res
        } else {
            for (let i = 0; i < list.length; i++) {
                if (list[i].children instanceof Array && list[i].children.length > 0) {
                    res = this.findItemById(id, list[i].children)
                    if (res) {
                        return res
                    }
                }
            }
            return null
        }
    }
    getRoleMenus() {
        this.menuLoading = true
        this.$emit('getMenuLoading', this.menuLoading)
        const { superior_role: superiorRole, name } = this.role
        const superiorIsAdmin = superiorRole === 'admin'
        Promise.all([this.getCurrentRoleMenus(name), !superiorIsAdmin && this.getSuperiorMenus(superiorRole)]).finally(() => {
            this.menuLoading = false
            this.$emit('getMenuLoading', this.menuLoading)
        })
    }
    async getCurrentRoleMenus(roleId) {
        const res = await this.$api.RoleManageMain.getRoleMenus({ roleId })
        if (!res.result) {
            return this.$error(res.message)
        }
        this.permissions = res.data
        const result = getMenuIdsAndOperateIds(res.data)
        // 计算一开始有权限的id
        const rawIds = res.data
        // 传给父组件保存
        this.$emit('getRawIds', rawIds)
        for (const k in result) {
            result[k].forEach(item => {
                const target = this.findItemById(k === 'operate_ids' ? item.menuId : item, this.menuList)
                if (target) {
                    if (k === 'operate_ids') {
                        item[k].forEach(tex => {
                            const flag = target.auth.find(nev => nev.key === tex)
                            flag.value = true
                            this.handleOperateChecked(target, flag.type, true)
                        })
                    } else {
                        if (target.children && target.children.length) {
                            return false
                        }
                        const flag = target.auth.find(nev => nev.key.includes(item))
                        flag.value = true
                        this.handleOperateChecked(target, flag.type)
                    }
                }
            })
        }
    }
    async getSuperiorMenus(roleId) {
        const res = await this.$api.RoleManageMain.getRoleMenus({ roleId })
        if (!res.result) {
            return this.$error(res.message)
        }
        const keys = res.data.map(item => {
            if (item.endsWith('_view')) {
                item = item.replace('_view', '')
            }
            return item
        })
        this.menuList = getMenuListByAllowedKeys(this.menuList, keys)
        removeItemsWithId(this.menuList, ['SysRole'])
    }
}
