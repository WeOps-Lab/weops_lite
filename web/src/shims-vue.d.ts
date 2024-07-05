import Vue from "vue";
import VueRouter, { Route } from "vue-router";

declare module "*.vue" {
    export default Vue;
}

declare module "vue/types/vue" {
    interface Vue {
        $router: VueRouter; // 这表示this下有这个东西
        $route: Route;
        $api: any,
        $echarts: any,
        $http: any,
        $message: any,
        $error: any,
        $warn: any,
        $success: any,
        $bus: any,
        $BtnPermission: any,
        $handleKeepAlive: any,
        $random: any,
        $deepClone: any,
        $formatDate: any,
        $FormatTime: any,
        $buildRules: any,
        $compareFormData: any,
        $ArrayObjDup: any,
        $copy: any,
        $bkInfo: any,
        $DateDisplay: any,
        $groupData: any,
        $Copy: any,
        $optionalChaining: any,
        $stampToTime: any
    }
}
