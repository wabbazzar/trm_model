<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  
  export let data = null;
  let chartContainer;
  let selectedBar = null;
  let showModal = false;
  
  onMount(async () => {
    if (!data) {
      const response = await fetch('/data/arc_prize_ablations.json');
      const jsonData = await response.json();
      data = jsonData;
    }
    
    createChart();
  });
  
  function handleBarClick(experiment) {
    selectedBar = experiment;
    showModal = true;
  }
  
  function closeModal() {
    showModal = false;
    selectedBar = null;
  }
  
  function createChart() {
    if (!data || !chartContainer) return;
    
    const margin = { top: 20, right: 30, bottom: 100, left: 60 };
    const width = 800 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;
    
    const svg = d3.select(chartContainer)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);
    
    // X scale
    const x = d3.scaleBand()
      .domain(data.experiments.map(d => d.name))
      .range([0, width])
      .padding(0.2);
    
    // Y scale
    const y = d3.scaleLinear()
      .domain([0, d3.max(data.experiments, d => d.accuracy)])
      .nice()
      .range([height, 0]);
    
    // Bars
    svg.selectAll('.bar')
      .data(data.experiments)
      .enter()
      .append('rect')
      .attr('class', 'bar')
      .attr('x', d => x(d.name))
      .attr('y', d => y(d.accuracy))
      .attr('width', x.bandwidth())
      .attr('height', d => height - y(d.accuracy))
      .attr('fill', d => d.color)
      .attr('opacity', 0.8)
      .style('cursor', 'pointer')
      .on('mouseover', function() {
        d3.select(this).attr('opacity', 1);
      })
      .on('mouseout', function() {
        d3.select(this).attr('opacity', 0.8);
      })
      .on('click', function(event, d) {
        handleBarClick(d);
      });
    
    // Value labels on bars
    svg.selectAll('.label')
      .data(data.experiments)
      .enter()
      .append('text')
      .attr('class', 'label')
      .attr('x', d => x(d.name) + x.bandwidth() / 2)
      .attr('y', d => y(d.accuracy) - 5)
      .attr('text-anchor', 'middle')
      .attr('font-size', '14px')
      .attr('font-weight', 'bold')
      .text(d => `${(d.accuracy * 100).toFixed(1)}%`);
    
    // X axis
    svg.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(d3.axisBottom(x))
      .selectAll('text')
      .attr('transform', 'rotate(-25)')
      .style('text-anchor', 'end');
    
    // Y axis
    svg.append('g')
      .call(d3.axisLeft(y).tickFormat(d => `${d * 100}%`));
    
    // Y axis label
    svg.append('text')
      .attr('transform', 'rotate(-90)')
      .attr('y', 0 - margin.left)
      .attr('x', 0 - (height / 2))
      .attr('dy', '1em')
      .style('text-anchor', 'middle')
      .style('font-weight', 'bold')
      .text('Accuracy');
  }
</script>

<div class="chart-wrapper">
  <div bind:this={chartContainer} class="chart-container"></div>
</div>

{#if showModal && selectedBar}
  <!-- svelte-ignore a11y-click-events-have-key-events -->
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div class="modal-backdrop" on:click={closeModal}>
    <div class="modal-content" on:click|stopPropagation>
      <button class="close-btn" on:click={closeModal}>✕</button>
      <div class="modal-body">
        {@html selectedBar.detailed_description}
      </div>
    </div>
  </div>
{/if}

<style>
  .chart-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    backdrop-filter: blur(5px);
  }
  
  .modal-content {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    max-width: 600px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
    color: #333;
  }
  
  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #666;
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    transition: background 0.2s;
  }
  
  .close-btn:hover {
    background: #f0f0f0;
    color: #333;
  }
  
  .modal-body {
    line-height: 1.6;
  }
  
  .modal-body :global(strong) {
    color: #1e40af;
  }
  
  .modal-body :global(ul) {
    margin: 0.5rem 0;
    padding-left: 1.5rem;
  }
  
  .modal-body :global(code) {
    background: #f3f4f6;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-family: 'Fira Code', monospace;
  }
</style>

