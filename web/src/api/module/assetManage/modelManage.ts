// 模型管理模块
import {get, deletes, post, put, reUrl} from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 查询模型分类
     * @param {Object} params 请求参数
     */
    getClassification(params = {}) {
        return get(`${reUrl}/classification/`, params)
    },
    /**
     * 创建模型分类
     * @param {Object} params 请求参数
     */
    createClassification(params = {}) {
        return post(`${reUrl}/classification/`, params)
    },
    /**
     * 修改模型分类
     * @param {Object} params 请求参数
     */
    updateClassification(params = {}) {
        return put(`${reUrl}/classification/${params.classification_id}/`, params)
    },
    /**
     * 删除模型分类
     * @param {Object} params 请求参数
     */
    deleteClassification(params = {}) {
        return deletes(`${reUrl}/classification/${params.id}/`)
    },
    /**
     * 查询模型
     * @param {Object} params 请求参数
     */
    getModel(params = {}) {
        return get(`${reUrl}/model/`, params)
    },
    /**
     * 创建模型
     * @param {Object} params 请求参数
     */
    createModel(params = {}) {
        return post(`${reUrl}/model/`, params)
    },
    /**
     * 修改模型
     * @param {Object} params 请求参数
     */
    updateModel(params = {}) {
        return put(`${reUrl}/model/${params.model_id}/`, params)
    },
    /**
     * 删除模型
     * @param {Object} params 请求参数
     */
    deleteModel(params = {}) {
        return deletes(`${reUrl}/model/${params.id}/`)
    },
    /**
     * 查询模型属性
     * @param {Object} params 请求参数
     */
    getModelAttrList(params = {}) {
        return get(`${reUrl}/model/${params.id}/attr_list/`)
    },
    /**
     * 创建模型属性
     * @param {Object} params 请求参数
     */
    createModelAttr(params = {}) {
        return post(`${reUrl}/model/${params.id}/attr/`, params)
    },
    /**
     * 修改模型属性
     * @param {Object} params 请求参数
     */
    updateModelAttr(params = {}) {
        return put(`${reUrl}/model/${params.id}/attr_update/`, params)
    },
    /**
     * 删除模型属性
     * @param {Object} params 请求参数
     */
    deleteModelAttr(params = {}) {
        return deletes(`${reUrl}/model/${params.id}/attr/${params.attr_id}/`)
    },
    /**
     * 查询模型关联
     * @param {Object} params 请求参数
     */
    getModelAssoList(params = {}) {
        return get(`${reUrl}/model/${params.id}/association/`, params.body)
    },
    /**
     * 查询模型关联类型
     * @param {Object} params 请求参数
     */
    getAssotypeList(params = {}) {
        return get(`${reUrl}/model/model_association_type/`, params)
    },
    /**
     * 创建模型关联
     * @param {Object} params 请求参数
     */
    createAssociation(params = {}) {
        return post(`${reUrl}/model/association/`, params)
    },
    /**
     * 修改模型关联
     * @param {Object} params 请求参数
     */
    updateAssociation(params = {}) {
        return put(`${reUrl}/model/association/${params.model_asst_id}/`, params)
    },
    /**
     * 删除
     * @param {Object} params 请求参数
     */
    deleteAssociation(params = {}) {
        return deletes(`${reUrl}/model/association/${params.id}/`)
    }
}
