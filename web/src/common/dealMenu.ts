export function removeItemsWithId(items, idsToRemove) {
    if (!items) return false
    for (let i = items.length - 1; i >= 0; i--) {
        if (idsToRemove.includes(items[i].id)) {
            items.splice(i, 1)
        }
        // 如果元素具有子元素children，则递归调用removeItemsWithId函数
        if (items[i]?.children?.length) {
            removeItemsWithId(items[i].children, idsToRemove)
        }
    }
}
// 按照层级顺序检查每层级的第一个是否具有url属性
export function findFirstUrl(menus) {
    const traverseMenu = (menu) => {
        if (menu.children?.length) {
            for (const child of menu.children) {
                const result = traverseMenu(child) // 递归遍历子菜单
                if (result) {
                    return result // 如果找到了目标项，则直接返回结果
                }
            }
        }
        if (menu.id && !menu.isUrl && !menu.children?.length) {
            return menu.id // 返回具有 id 属性且 isUrl 为 false 的项的 id
        }
        return null // 如果当前菜单项不满足条件，则返回 null
    }
    for (const menu of menus) {
        const result = traverseMenu(menu) // 遍历每一个菜单项
        if (result) {
            return result // 如果找到了目标项，则直接返回结果
        }
    }

    return null // 如果没有满足条件的项，则返回 null 或其他默认值
}

export function hasPathInChildren(data, path) {
    // 遍历数组中的每个对象
    for (const item of data) {
        // 判断当前对象的 path 是否匹配
        if (item.url === path) {
            return true // 如果匹配，直接返回 true
        }
        // 判断当前对象是否有 children 属性且为非空数组
        if (item.children?.length) {
            // 递归调用 hasPathInChildren 函数检查子级数组
            if (hasPathInChildren(item.children, path)) {
                return true // 如果子级数组中存在匹配的 path，直接返回 true
            }
        }
    }
    // 如果遍历完整个数组都没有找到匹配的 path，返回 false
    return false
}

export function findIdsWithNoChildren(data, result = []) {
    for (const item of data) {
        if (!item.children || item.children.length === 0) {
            result.push(item.id)
        } else {
            findIdsWithNoChildren(item.children, result)
        }
    }
    return result
}

export function filterDataWithId(arr, id) {
    for (let i = 0; i < arr.length; i++) {
        const item = arr[i]
        if (item.id === id) {
            return [item] // 返回包含id的项作为初始层级
        }
        if (item.children) {
            const result = filterDataWithId(item.children, id)
            if (result.length > 0) {
                return [{ ...item, children: result }] // 返回包含id的项及其子层级的新对象
            }
        }
    }
    return [] // 没有找到符合条件的项
}

// 根据菜单id找到auth信息
export function findAuthById(id, routeConfig) {
    // 递归遍历routeConfig数组
    for (let i = 0; i < routeConfig.length; i++) {
        const route = routeConfig[i]
        // 如果找到匹配的id
        if (route.id === id) {
            const auth = route.auth
            // 遍历auth数组
            for (let j = 0; j < auth.length; j++) {
                const authItem = auth[j]
                const key = authItem.key
                // 如果key以'_view'结尾
                if (key.endsWith('_view')) {
                    return auth
                }
            }
        }
        // 递归遍历子节点
        if (route.children) {
            const childAuth = findAuthById(id, route.children)
            if (childAuth) {
                return childAuth
            }
        }
    }
    return null // 如果未找到匹配的id，返回null
}

// 获取菜单ids和操作权限ids
export function getMenuIdsAndOperateIds(data) {
    const operateIds = []
    const authData = data.filter(item => /^[A-Z]/.test(item)) // 获取以大写字母开头的菜单查看和操作权限id
    const menusIds = authData.filter(item => item.endsWith('view')).map(item => item.split('_')[0])
    const operateArr = authData.filter(item => !item.endsWith('view')).map(item => item)
    operateArr.forEach(item => {
        const menuId = item.split('_')[0]
        const target = operateIds.find(operate => operate.menuId === menuId)
        if (!target) {
            operateIds.push({
                menuId,
                operate_ids: [item]
            })
            return
        }
        target.operate_ids.push(item)
    })
    return {
        menus_ids: menusIds,
        operate_ids: operateIds
    }
}

// 转换成大驼峰格式
export const underscoreToCamelCase = (str) => {
    const words = str.split('_') // 将字符串以下划线分隔成单词数组
    const camelCaseWords = words.map(word => {
        return word.charAt(0).toUpperCase() + word.slice(1) // 单词首字母大写
    })
    return camelCaseWords.join('') // 将单词数组合并成驼峰格式的字符串
}

// 大驼峰格式还原以下划线拼接
export const camelCaseToUnderscore = (str) => {
    return str.replace(/([A-Z])/g, (match, p1, offset) => {
        if (!offset) {
            // 第一个单词不需要加下划线
            return match.toLowerCase()
        }
        return '_' + match.toLowerCase()
    })
}
