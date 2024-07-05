// 添加角色的校验规则
import { Rule } from '../index'
export interface RulesForm {
    role_name: Array<Rule>,
    superior_role: Array<Rule>
}
