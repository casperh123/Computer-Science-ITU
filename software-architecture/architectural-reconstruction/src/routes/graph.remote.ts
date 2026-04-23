import { query } from "$app/server";
import { DependencyGraph } from "$lib/sourceAnalysis/dependencyGraph";
import { FileExplorer } from "$lib/sourceAnalysis/fileExploration";
import path from "path";
import { fileURLToPath } from "url";
import z from "zod";

export const getGraph = query(z.int(), async(depth: number) => {
  if(depth == 0) {
    depth = 2;
  }


  const __baseDir = path.dirname(fileURLToPath(import.meta.url));
  const dir = path.join(__baseDir, '../../libs/dokploy/'); 

  const explorer = new FileExplorer();
  const files = await explorer.getJavaScriptFiles(dir);
  const dependencyGraphbuilder = new DependencyGraph(dir, depth);

  return await dependencyGraphbuilder.build(files);
});
