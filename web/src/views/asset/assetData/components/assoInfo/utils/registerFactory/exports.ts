import { registerNode } from './registerNode'
import { registerEdge } from './registerEdge'

export default (G6, vueInstance) => {
    registerNode(G6, vueInstance)
    registerEdge(G6, vueInstance)
}
