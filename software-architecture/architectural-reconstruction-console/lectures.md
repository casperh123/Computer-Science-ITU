# Notes from Mirceas lecture

Just do: ´if importn then include` kinda style of AST walking instead of the mess that is right now.

Collapse file names `.ts, .js, .jsx, .tsx` to their nearest folder as the module.

## Filtering irrelevant nodes.

Here we filter out the imports that we don't want to consider. So not in the file scanning stage, but in the tree parsing stage.
This makes sure, that the edges are architecturally relevant, and not just random noise. 

One other way to do this, might also be to limit the depth of traversal, so this might include collapsing the files into the xth folder, instead of having it at each root.

- Relection model: Aggregate the individual files to the module level.
- 
- 
- 

