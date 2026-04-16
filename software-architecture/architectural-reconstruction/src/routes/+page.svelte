<script lang="ts">
	import { getGraph } from './graph.remote';
	import { renderGraph } from '$lib/sourceAnalysis/renderer';

	let container: HTMLDivElement | null = null;
	let cy: any;

	const graphQuery = getGraph();

	$effect(() => {
		(async () => {
			const graph = await graphQuery;

			if (cy) cy.destroy();

			cy = renderGraph(container!, graph);
		})();
	});
</script>

<button onclick={() => graphQuery.refresh()}>
	Refresh graph
</button>

{#if graphQuery.loading}
	<p>Loading...</p>
{:else}
	<div bind:this={container} style="height: 100vh;"></div>
{/if}
