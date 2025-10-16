<script>
  import { onMount } from 'svelte';
  import Citation from '../components/Citation.svelte';
  
  let matrixData = null;
  
  onMount(async () => {
    const response = await fetch('/data/training_inference_matrix.json');
    matrixData = await response.json();
  });
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">Training vs Inference</h1>
    <h2 class="slide-subtitle text-center">How You Train Matters More Than How You Infer</h2>
    
    <div class="content-area">
      {#if matrixData}
        <div class="results-grid grid grid-cols-3 gap-4 mb-4">
          {#each matrixData.key_comparisons as config}
            <div class="result-box bg-white p-6 rounded-lg shadow-lg border-2 
              {config.color === 'gray' ? 'border-gray-400' : 
               config.color === 'orange' ? 'border-orange-500' : 
               'border-green-500'}">
              <div class="config mb-2">
                <p class="text-sm font-medium text-slate-600">Train: {config.training_steps} | Test: {config.inference_steps}</p>
              </div>
              <div class="accuracy mb-2">
                <p class="text-5xl font-bold 
                  {config.color === 'gray' ? 'text-gray-600' : 
                   config.color === 'orange' ? 'text-orange-600' : 
                   'text-green-600'}">
                  {(config.accuracy * 100).toFixed(1)}%
                </p>
              </div>
              <div class="label">
                <p class="text-base font-semibold text-slate-700">{config.label}</p>
              </div>
            </div>
          {/each}
        </div>
        
        <div class="insights bg-gradient-to-r from-orange-50 to-green-50 p-5 rounded-lg border-2 border-orange-400">
          <h3 class="text-2xl font-bold mb-3 text-slate-800 text-center">
            The Verdict
            <Citation citeId="training-vs-inference" inline={true} />
          </h3>
          <div class="grid grid-cols-3 gap-4 text-center">
            <div class="insight">
              <p class="text-5xl font-bold text-orange-600 mb-1">{matrixData.insights.training_impact}</p>
              <p class="text-sm font-semibold text-slate-700">Training impact</p>
              <p class="text-xs text-slate-600">(16 steps → 1 step test)</p>
            </div>
            <div class="insight">
              <p class="text-5xl font-bold text-green-600 mb-1">{matrixData.insights.inference_impact}</p>
              <p class="text-sm font-semibold text-slate-700">Inference impact</p>
              <p class="text-xs text-slate-600">(1 step → 4 steps test)</p>
            </div>
            <div class="insight">
              <p class="text-5xl font-bold text-blue-600 mb-1">{matrixData.insights.ratio}</p>
              <p class="text-sm font-semibold text-slate-700">Training advantage</p>
              <p class="text-xs text-slate-600">over inference</p>
            </div>
          </div>
          <div class="conclusion mt-4 text-center">
            <p class="text-lg font-semibold text-slate-800">{matrixData.insights.conclusion}</p>
          </div>
        </div>
      {/if}
    </div>
  </div>
</div>

