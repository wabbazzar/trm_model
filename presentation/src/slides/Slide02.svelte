<script>
  import { onMount } from 'svelte';
  import Citation from '../components/Citation.svelte';
  
  let modelData = null;
  
  onMount(async () => {
    const response = await fetch('/data/model_comparison.json');
    const data = await response.json();
    modelData = data.models;
  });
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">The ARC-AGI Challenge</h1>
    <h2 class="slide-subtitle text-center">Why These Papers Matter</h2>
    
    <div class="content-area">
      <div 
        class="challenge-description bg-white p-4 rounded-lg shadow-lg mb-4 cursor-pointer transition-all duration-200 hover:shadow-xl hover:scale-[1.02] hover:border-2 hover:border-blue-500"
        on:click={() => window.open('https://arcprize.org/arc-agi', '_blank')}
        on:keydown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            window.open('https://arcprize.org/arc-agi', '_blank');
          }
        }}
        role="link"
        tabindex="0"
      >
        <h3 class="text-xl font-bold mb-2 text-slate-800">
          What is ARC-AGI? 
          <span class="text-blue-500 text-sm">🔗</span>
        </h3>
        <ul class="space-y-1 text-base text-slate-700">
          <li>✅ Tests <strong>abstract reasoning</strong>, not knowledge retrieval</li>
          <li>✅ Simple visual patterns (3×3 to 30×30 grids)</li>
          <li>✅ Requires understanding transformation rules from few examples</li>
          <li>❌ LLMs struggle despite massive scale</li>
        </ul>
      </div>
      
      {#if modelData}
        <div class="model-performance bg-white p-4 rounded-lg shadow-lg">
          <h3 class="text-xl font-bold mb-2 text-slate-800">
            Performance Comparison
            <Citation citeId="llm-performance-comparison" inline={true} />
          </h3>
          <div class="grid grid-cols-3 gap-3">
            {#each modelData as model}
              <div class="model-box p-3 rounded-lg" style="background-color: {model.color}20; border: 2px solid {model.color};">
                <h4 class="font-bold text-base mb-1">
                  {model.name}
                  {#if model.name === 'HRM'}
                    <Citation citeId="hrm-performance-trm-paper" inline={true} />
                  {:else if model.name === 'TRM'}
                    <Citation citeId="trm-performance" inline={true} />
                  {/if}
                </h4>
                <p class="text-xs text-slate-600 mb-1">{model.type}</p>
                {#if model.arc_agi_1}
                  <p class="text-2xl font-bold" style="color: {model.color};">{(model.arc_agi_1 * 100).toFixed(1)}%</p>
                  <p class="text-xs text-slate-500">ARC-AGI-1</p>
                {/if}
                {#if model.arc_agi_2}
                  <p class="text-lg" style="color: {model.color};">{(model.arc_agi_2 * 100).toFixed(1)}%</p>
                  <p class="text-xs text-slate-500">ARC-AGI-2</p>
                {/if}
              </div>
            {/each}
          </div>
        </div>
      {/if}
      
      <div class="key-point mt-4 text-center">
        <p class="text-xl font-bold text-orange-600">
          "Something fundamentally different is needed"
        </p>
      </div>
    </div>
  </div>
</div>

