import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { FileExplorer } from './fileExploration.js';
import { DependencyGraph } from './dependencyGraph.js';
import { Diagram } from './diagramGenerater.js';

const explorer = new FileExplorer();
const __baseDir = path.dirname(fileURLToPath(import.meta.url));
const __dokployDir = path.join(__baseDir, '../libs/dokploy/');

const files = await explorer.getJavaScriptFiles(__dokployDir);
const dependencyGraphbuilder = new DependencyGraph(__dokployDir);
const graph = await dependencyGraphbuilder.build(files);
const diagram = new Diagram;

diagram.saveGraph(graph);
