import fs from 'node:fs/promises';
import path from 'node:path';
import * as parser from '@babel/parser';
import _traverse from '@babel/traverse';
const traverse = (_traverse as any).default ?? _traverse;


export class DependencyGraph {
  private dokployDir: string;

  constructor(dokployDir: string) {
    this.dokployDir = dokployDir;
  }


  public async build(filePaths: string[]): Promise<Map<string, Map<string, number>>> {
    const graph = new Map<string, Map<string, number>>();

    for (const filePath of filePaths) {
      const moduleName = this.toModuleName(filePath);

      if (!graph.has(moduleName)) {
        graph.set(moduleName, new Map());
      }

      let code: string;
      try {
        code = await fs.readFile(filePath, 'utf-8');
      } catch {
        continue;
      }

      const imports = this.getImports(code);

      for (const imp of imports) {
        const target = this.toImportModule(imp, filePath);
        if (!target || target === moduleName) continue;

        const deps = graph.get(moduleName)!;
        deps.set(target, (deps.get(target) ?? 0) + 1);
      }
    }

    // Remove empty nodes
    for (const [module, deps] of graph) {
      if (deps.size === 0) graph.delete(module);
    }

    return graph;
  }

  private toModuleName(filePath: string): string {
    const relative = path.relative(this.dokployDir, filePath);
    return path.dirname(relative);
  }

  private toImportModule(imp: string, fromFile: string): string | undefined {
    if (imp.startsWith('.')) {
      const fromDir = path.dirname(fromFile);
      const resolved = path.resolve(fromDir, imp);
      const relative = path.relative(this.dokployDir, resolved);
      return path.dirname(relative);
    }

    if (imp.startsWith('@/')) {
      const cleaned = imp.replace(/^@\//, '');
      const parts = cleaned.split('/');
      return parts.slice(0, -1).join('/') || parts[0];
    }

    if (imp.startsWith('@')) {
      const parts = imp.split('/');
      return parts.slice(0, 2).join('/');
    }

    return imp.split('/')[0] || "";
  }


  private getImports(code: string): string[] {
    const imports: string[] = [];
    try {
      const ast = parser.parse(code, {
        sourceType: 'module',
        plugins: ['typescript', 'jsx'],
      });
      traverse(ast, {
        ImportDeclaration(path: any) {
          imports.push(path.node.source.value);
        },
      });
    } catch {
      // skip files that fail to parse
    }
    return imports;
  }
}
