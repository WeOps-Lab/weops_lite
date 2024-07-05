import { Vue, Component, Prop } from 'vue-property-decorator'
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
        default: () => 450
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
    @Prop({
        type: Object,
        default: () => ({
            field: '',
            value: '',
            type: ''
        })
    })
    config

    conditionList: any = {
        'bool': [
            { value: 'bool', label: '等于' }
        ],
        'str': [
            { value: 'str=', label: '等于' },
            { value: 'str*', label: '包含' },
            { value: 'str<>', label: '不等于' }
        ],
        'int': [
            { value: 'int=', label: '等于' },
            { value: 'int<>', label: '不等于' },
            { value: 'int>', label: '大于' },
            { value: 'int<', label: '小于' }
        ]
    }

    get showCondition() {
        return ['bool', 'str', 'int'].includes(this.currentFeildInfo['attr_type'])
    }
    get currentFeildInfo() {
        return this.propertyList.find(item => item.attr_id === this.config.field) || {}
    }

    changeFieldvaule(val) {
        this.$emit('change', val)
    }
    changeFieldKey() {
        this.config.value = ''
        this.config.type = ''
        switch (this.currentFeildInfo.attr_type) {
            case 'enum':
                this.config.type = 'str[]'
                break
            case 'user':
                this.config.type = 'str[]'
                break
            case 'organization':
                this.config.type = 'str[]'
                break
            case 'bool':
                this.config.type = 'bool'
                break
            case 'time':
                this.config.type = 'time'
                break
        }
    }
}
