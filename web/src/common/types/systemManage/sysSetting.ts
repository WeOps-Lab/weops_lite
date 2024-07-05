// 添加角色的校验规则
import { Rule } from '../index'
export interface ExtenalChainRules {
    name: Array<Rule>,
    url: Array<Rule>
}
