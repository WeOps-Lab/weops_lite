import { Vue, Component, Prop, Watch } from 'vue-property-decorator'
@Component({
    components: {}
})
export default class SelectInput extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    propertyList: Array<any>
    @Prop({
        type: Number,
        default: () => 400
    })
    width: number
    @Prop({
        type: Array,
        default: () => []
    })
    userList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>

    fieldKey: string = ''
    fieldValue: any = ''
    exactSearch: boolean = true
    isExactSearch: number = 0

    get currentFeildInfo() {
        return this.propertyList.find(item => item.attr_id === this.fieldKey) || {}
    }

    @Watch('propertyList', { immediate: true, deep: true })
    onPropertyListChange(newVal: any) {
        if (newVal?.length) {
            this.fieldKey = newVal[0].attr_id
        }
    }

    changeFieldvaule(val) {
        let condition: any = {
            field: this.fieldKey,
            type: this.currentFeildInfo.attr_type,
            value: val
        }
        // 排除布尔类型的false || 多选框没选时的空数组
        if ((!val && val !== false) || (Array.isArray(val) && !val.length)) {
            condition = null
        } else {
            switch (this.currentFeildInfo.attr_type) {
                case 'enum':
                    condition.type = typeof val === 'number' ? 'int=' : 'str='
                    break
                case 'str':
                    condition.type = this.isExactSearch ? 'str=' : 'str*'
                    break
                case 'user':
                    condition.type = 'user[]'
                    condition.value = [val]
                    break
                case 'int':
                    condition.type = 'int='
                    condition.value = +condition.value
                    break
                case 'organization':
                    condition.type = 'str='
                    break
                case 'time':
                    delete condition.value
                    condition.start = val.at(1)
                    condition.end = val.at(-1)
                    break
            }
        }
        this.$emit('change', condition, val)
    }
    changeFieldKey() {
        this.fieldValue = ''
    }
}
