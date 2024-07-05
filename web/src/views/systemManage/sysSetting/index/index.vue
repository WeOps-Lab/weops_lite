<template>
    <div>
        <header-sub class="system-setting-header">
            <template slot="title">
                <menu-tab
                    :panels="panels"
                    type="line"
                    v-model="active" />
            </template>
        </header-sub>
        <page-explanation
            :title="getTitleOrContent('label')"
            :content="getTitleOrContent('content')" />
        <component :is="active" />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
