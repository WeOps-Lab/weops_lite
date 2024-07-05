import Vue from 'vue';

let vm = new Vue();

const cwMessage = function (data, t = {theme: 'primary'}) {
    if (data === 'cancelRequest') {
        return false
    }
    if (typeof data === 'string') {
        // @ts-ignore
        vm.$bkMessage({
            theme: t.theme,
            message: data
        })
    } else {
        let option = Object.assign(t, data);
        // @ts-ignore
        vm.$bkMessage(option);
    }
};
const types = [
    {key: 'info', theme: 'primary'},
    {key: 'primary', theme: 'primary'},
    {key: 'error', theme: 'error'},
    {key: 'success', theme: 'success'},
    {key: 'warning', theme: 'warning'}
];
types.forEach(t => {
    cwMessage[t.key] = (data) => {
        return cwMessage(data, t);
    }
});
export default cwMessage;
