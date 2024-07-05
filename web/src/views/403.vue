<template>
    <div>
        <el-empty description=" ">
            <span>抱歉，您暂无该功能的权限</span>
            <div class="text-subtitle">你没有该功能的权限，请联系您的专属客户经理进行申请</div>
        </el-empty>
    </div>
</template>

<style lang="scss">
/* stylelint-disable selector-class-pattern */
.el-empty__bottom {
    span {
        font-size: 24px;
        color: #63656e;
    }
    .text-subtitle {
        color: #979BA5;
        font-size: 14px;
        text-align: center;
        margin-top: 14px;
    }
}
</style>
