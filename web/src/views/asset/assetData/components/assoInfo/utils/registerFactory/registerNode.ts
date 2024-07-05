export const registerNode = (G6, vue) => {
    // 注册自定义节点，包括一个子分组作为keyShape
    G6.registerNode(
        'asso-node',
        {
            draw(cfg, group) {
                const width = cfg.size[0]
                const height = cfg.size[1]
                const keyShape = addMainShape(cfg, group)
                const subShape = group.addGroup(
                    {
                        name: 'sub-group',
                        opacity: 1
                    }
                )
                addTextShape(cfg, subShape)
                addTextShapes(cfg, subShape)
                // 处理图标逻辑
                addIconShape(cfg, subShape)
                addPathShape(cfg, subShape)
                // 必须返回一个keyShape
                cfg.children?.length &&
                    group.addShape('marker', {
                        attrs: {
                            x: width,
                            y: height / 2,
                            r: 6,
                            cursor: 'pointer',
                            symbol: cfg.collapsed ? G6.Marker.expand : G6.Marker.collapse,
                            stroke: '#666',
                            lineWidth: 1,
                            fill: '#fff'
                        },
                        name: 'collapse-icon'
                    })
                return keyShape
            },
            // getAnchorPoints() {
            //     return [
            //         [0, 0.5]
            //         // [0, 0.5],
            //         // [0, 0.5],
            //         // [0, 0.5]
            //     ]
            // },
            setState(name, value, item) {
                if (name === 'collapsed') {
                    const marker = item.get('group').find((ele) => ele.get('name') === 'collapse-icon')
                    const icon = value ? G6.Marker.expand : G6.Marker.collapse
                    marker.attr('symbol', icon)
                }
            }
        },
        'rect'
    )
}

const addMainShape = (cfg, group) => {
    const width = cfg.size[0]
    const height = cfg.size[1]
    return group.addShape(
        'rect', {
            attrs: {
                x: 0,
                y: 0,
                width: width,
                height: height,
                fill: '#fff',
                radius: 4,
                stroke: '#DADEE2',
                lineWidth: 1,
                shadowColor: '#E7EBEE',
                shadowBlur: 100,
                cursor: 'pointer'
            },
            name: 'key-shape',
            zIndex: 0,
            draggable: true
        })
}

const addIconShape = (cfg, group) => {
    let ccImage = require('@/assets/svg/model/cc-default_默认.svg')
    try {
        ccImage = require(`@/assets/svg/model/${cfg.icn}.svg`)
    } catch (e) {
        console.log('not find ', cfg.icn)
    }
    return group.addShape(
        'image', {
            attrs: {
                x: 14,
                y: 14,
                img: ccImage,
                width: 22,
                height: 22
            },
            name: 'icon-box',
            draggable: true
        })
}

const addPathShape = (cfg, group) => {
    return group.addShape(
        'path', {
            attrs: {
                path: [
                    ['M', 50, 51.5],
                    ['L', 50, 0.5]
                ],
                stroke: '#DADEE2',
                lineWidth: 1
            },
            name: 'icon-division'
        })
}

const addTextShape = (cfg, group) => {
    let vale = ''
    if (cfg.inst_name === null || cfg.inst_name === '') {
        vale = ''
    } else {
        const re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/
        if (re.test(cfg.inst_name)) {
            vale = cfg.inst_name.split('').length > 13 ? cfg.inst_name.split('').slice(0, 10).join('') + '...' : cfg.inst_name
        } else {
            if (typeof cfg.inst_name === 'string') {
                vale = cfg.inst_name.split('').length > 8 ? cfg.inst_name.split('').slice(0, 5).join('') + '...' : cfg.inst_name
            }
        }
    }
    // 判断是不是ip格式
    return group.addShape(
        'text', {
            attrs: {
                x: 106,
                y: `${cfg.inst_name === undefined ? 20 : 14}`,
                text: `${vale}`,
                textAlign: 'center',
                fontSize: 14,
                lineHeight: 15,
                fill: '#5F6568',
                textBaseline: 'top',
                cursor: 'pointer'
            },
            name: 'node' + '-' + cfg.inst_name,
            zIndex: 1,
            draggable: true
        })
}

const addTextShapes = (cfg, group) => {
    return group.addShape(
        'text', {
            attrs: {
                x: 106,
                y: 32,
                text: `${cfg.model_name === undefined ? '' : cfg.model_name}`,
                textAlign: 'center',
                fontSize: 12,
                lineHeight: 15,
                fill: '#C4C6CC',
                textBaseline: 'top',
                cursor: 'pointer'
            },
            name: 'node' + '-' + cfg.model_name,
            zIndex: 1,
            draggable: true
        })
}
