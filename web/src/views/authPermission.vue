<template>
    <el-empty description=" ">
        <span>无菜单权限</span>
        <div class="text-subtitle" style="margin-top: 20px;">您没有相应菜单的访问权限，请前往申请相关菜单权限</div>
    </el-empty>
</template>

<script lang="ts">
    import { Vue, Component } from 'vue-property-decorator'
    @Component({
        name: 'no-purview'
    })
    export default class NoPurview extends Vue {}
</script>

<style lang="scss">
/* stylelint-disable selector-class-pattern */
.el-empty__bottom {
    color: #63656e;
    font-size: 24px;
    text-align: center;
    margin-top: 14px;
}
</style>
