import Vue from 'vue';

Vue.prototype.$copy = function (val) {
    if (!val) return {};
    return JSON.parse(JSON.stringify(val))
};
Vue.prototype.$apply = function (data) {
    return Object.assign({}, data, data);
};
Vue.prototype.$deepClone = function (val) {
    if (!val) return {};
    let a: any = {};
    a.o = val;
    return JSON.parse(JSON.stringify(a.o))
};

// 在template中使用可选链
Vue.prototype.$optionalChaining = (obj, ...rest) => {
    let tmp = obj
    for (const key in rest) {
        const name = rest[key]
        tmp = tmp?.[name]
    }
    if (tmp === 0) return tmp
    else return tmp || '--'
}

Vue.prototype.$stampToTime = (timeStamp) => {
    const date = new Date(timeStamp)
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()
    const clockTime = date.toString().split(' ')[4]
    return year + '/' + (month < 10 ? '0' + month : month) + '/' + (day < 10 ? '0' + day : day) + ' ' + clockTime
}
