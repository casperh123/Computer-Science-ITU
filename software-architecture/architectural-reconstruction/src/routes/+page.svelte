<script lang="ts">
	import { getGraph } from './graph.remote';
	import { renderGraph } from '$lib/sourceAnalysis/renderer';

	let container: HTMLDivElement | null = null;
	let cy: any;
  let depth = $state(0);
  
  const depths = Array.from({ length: 11 }, (_, i) => i + 1);
	const graphQuery = $derived(getGraph(depth));

	$effect(() => {
		(async () => {
			const graph = await graphQuery;

			if (cy) cy.destroy();

			cy = renderGraph(container!, graph);
		})();
	});
</script>

<header class="header">
  <div class="header-inner-wrapper max-width">
    <h1>Hej!</h1>
    
    <button onclick={() => graphQuery.refresh()} class="btn">
	    Refresh graph
    </button>

    <select name="depth-picker" id="depth" bind:value={depth}>
      <option value="Depth">Depth</option>
      {#each depths as depth}
         <option value={depth}>{depth}</option>
      {/each}
    </select>
  </div>
</header>

{#if graphQuery.loading}
	<p>Loading...</p>
{:else}
	<div bind:this={container} style="height: 100vh;"></div>
{/if}

<style>
  .header {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.2);
    padding: 20px;
  }

  .header-inner-wrapper {
  }
</style>
