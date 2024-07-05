export const registerEdge = (G6, vue) => {
    G6.registerEdge(
        'cubic-horizontal',
        {
            afterDraw(cfg, group) {
                const shape = group.get('children')[0]
                const tagetModel = cfg.targetNode.getModel()
                const { isSource, asst_name: asstName } = tagetModel
                const style = {}
                const key = isSource ? 'endArrow' : 'startArrow'
                style[key] = {
                    path: 'M 0,0 L 8,4 L 8,-4 Z',
                    fill: '#ddd'
                }
                shape.attr(style)
                // 更新label内容
                const labelCfg = group.shapeMap['edge-label']
                if (labelCfg) {
                    // 下面没加update，更换label不生效
                    labelCfg.attr({ text: asstName })
                }
            },
            update(cfg, group) {

            }
        },
        'cubic-horizontal'
    )
}
