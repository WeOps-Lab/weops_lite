# 开发示例指引

## 在projects目录下创建您的第一个子应用example

### example目录 （src/projects/example）
```markdown
├── api # 请求
│    ├── modules # api模块管理
│    │    ├── example.ts # 自定义api模块
│    ├── index.ts # 统一引入api模块
├── assets # 静态文件
│    ├── svg # 例如图片文件
├── router # 路由
│    ├── frameRouter.ts # 自定义路由
├── store  # vuex
│    ├── modules # store模块管理
│    |    ├── example.ts # 自定义store模块
│    ├── index.ts # 统一引入store模块
├── views # vue文件
│    ├── index.vue # example的首页
└── main.ts # 入口 加载组件 自定义指令 初始化等
```
### example目录文件内容示例

- 接口模块
``` js
//  api/modules/example.ts
import { get, post } from '@/api/axiosconfig/axiosconfig'
import Mock from 'mockjs' // 使用Mockjs

// mock数据
const data = Mock.mock({
    'list|10': [
    {
      id: '@increment',
      name: '@cname()',
      address: '@city(true)',
      date: '@date(yyyy-MM-dd)'
    }
  ]
})
// 拦截get请求
Mock.mock(/example\/list/, 'get', (option) => {
    return {
        result: 'success',
        code: '20000',
        message: 'success',
        data: data.list
    }
})
// 拦截post请求
Mock.mock(/example\/list/, 'post', (option) => {
    return {
        result: 'success',
        code: '20000',
        message: 'success',
        data: null
    }
})

export default {
    getList(params = {}) {
        return get('/example/list/', params)
    },
    modifyList(params = {}) {
        return post('/example/list/', params)
    }
}
```

- 统一管理接口模块
``` js
//  api/index.ts
import example from './modules/example'

const exampleBaseApi = {
    example
}

export default exampleBaseApi
```

- 子应用路由配置文件
- **注意**：`framRouter`中的`name`属性值需要与`adminRouteConfig`中的children的`id`一致
``` js
// router/frameRouter.ts

// 引入页面
const Example = () => import('@example/views/index.vue')
const Other = () => import('@example/views/other.vue')
// 定义路由前缀
const routerPrefix = 'example'

// 页面路由都写在frameRouter里
export const frameRouter = [
    {
        // 访问该路由的路径
        path: `/${routerPrefix}/index`,
        name: 'Example',
        component: Example,
        meta: {
            title: '一级菜单示例'
        },
        path: `/${routerPrefix}/other`,
        name: 'Other',
        component: Other,
        meta: {
            title: '二级菜单示例'
        }
    }
]

// 子应用入口，主框架会找到该文件的路由配置，合并到主框架中
export const adminRouteConfig = [
    {
        // 相当于一级菜单
        // name为一级菜单的名称
        name: '一级菜单示例',
        id: 'ExampleApp',
        // children数组相当于二级菜单，可配置多个对象
        children: [
            {
                // 二级菜单名称
                name: '二级菜单示例',
                // id需要与上面frameRouter的name一致
                id: 'Example',
                // 三级菜单，最多写到三级菜单
                children: [
                    name: '三级菜单示例',
                    id: 'Other',
                    url: '/other'
                ]
            }
        ]
    }
]

export const createAdminRouteConfig = () => adminRouteConfig
```

- store模块文件
``` js
//  store/modules/example.ts
// initial state
const state = {
    list: [{'message': '我是信息'}]
}

// getters
const getters = {
    //
}

// mutations
const mutations = {
    setList(state, newData) {
        state.list = newData
    }
}

// actions
const actions = {
    updateList({ commit }, newData) {
        commit('setList', newData)
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
```

- 统一管理store模块
``` js
//  store/index.ts
import example from './modules/example'

export default {
    example
}
```

- 页面组件文件
``` js
//  views/index.vue
<template>
    <div class="example-wrapper" v-bkloading="{ isLoading: loading, zIndex: 10 }">
        <div class="example-wrapper-content">
            {{msg}}
        </div>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { mapState, mapActions } from 'vuex'

@Component({
    components: {},
    computed: {
        ...mapState('example', { list: 'list' })
    },
    methods: {
        ...mapActions('example', { updateList: 'updateList' })
    }
})

export default class Example extends Vue {
    loading: boolean = false

    created() {
        this.getDetail()
    }

    get msg() {
        return this.list || '--'
    }

    async getDetail() {
        const { id } = this.$route.query
        this.loading = true
        try {
            const res = await this.$api.example.getList({ id })
            if (!res.result) {
                return this.$error(res.message)
            }
            this.updateList(res.data)
        } finally {
            this.loading = false
        }
    }
}
</script>

<style  lang="scss" scoped>
.example-wrapper {
    background: #fff;
    height: 100%;

    .example-wrapper-content {
        color: #000;
    }
}
</style>
```
```js
//  views/other.vue
<template>
    <div>other页面</div>
</template>
```
- 子应用入口文件，用于引入公共方法，自定义指令等等
- **注意**：不需要再新建vue实例配置路由，store等，主框架会进行处理
``` js
//  main.ts
// 公共方法
import '../../controller/func/common'

```
### 服务启动及打包
``` js
# 服务启动
npm run dev

# 服务打包
npm run build:micro
```
