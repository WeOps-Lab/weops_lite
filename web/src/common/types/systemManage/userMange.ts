// 添加用户的校验规则
import { Rule } from '../index'
export interface OperateUserRules {
    username?: Array<Rule>,
    lastName?: Array<Rule>,
    password: Array<Rule>,
    confirmPassword: Array<Rule>,
}
// 添加用户表单
export interface OperateUserFormData {
    username?: string,
    lastName?: string,
    email?: string,
    password: string,
    confirmPassword: string
}
