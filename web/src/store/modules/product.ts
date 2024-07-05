// initial state
const state = {
    all: [1, 2, 3, 4],
    navToggle: false,
    cacheRouter: [],
    keepAliveList: ['SysSetting']
}

// getters
const getters = {
    allData: () => {
        return state.all
    },
    navToggle: () => {
        return state.navToggle
    },
    cacheRouter: () => {
        return state.cacheRouter
    }
}

// mutations
const mutations = {
    setProducts(state, products) {
        state.all = products
    },
    setNavToggle(state, toggle) {
        state.navToggle = toggle
    },
    setCacheRouter(state, router) {
        state.cacheRouter = router
    }
}

// actions
const actions = {
    setAllProducts({commit}) {
        commit('setProducts', [111, 3, 33, 444])
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
