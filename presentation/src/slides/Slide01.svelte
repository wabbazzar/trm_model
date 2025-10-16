<script>
  import { onMount } from 'svelte';
  import Citation from '../components/Citation.svelte';
  
  let modelData = null;
  
  onMount(async () => {
    const response = await fetch('/data/model_comparison.json');
    modelData = await response.json();
  });
</script>

<div class="slide bg-gradient-to-br from-slate-900 to-slate-800 text-white">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="text-5xl font-bold mb-3 text-center">
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-orange-600">
        It's Not the Architecture
      </span>
    </h1>
    
    <h2 class="text-2xl text-black mb-8 text-center">
      Why Training Method Matters More Than Model Design
    </h2>
    
    <div class="thesis-box bg-slate-800/50 p-6 rounded-xl border-2 border-blue-500 mb-8">
      <p class="text-lg text-center italic">
        "The success of both <span class="text-blue-400">HRM</span> (Hierarchical Reasoning Model) 
        and <span class="text-orange-400">TRM</span> (Tiny Recursive Model) comes not from their <span class="text-blue-400">architectures</span>, 
        but from <span class="text-orange-400">how they train</span>—through iterative refinement with deep supervision."
      </p>
    </div>
    
    {#if modelData}
      <div class="comparison-grid grid grid-cols-2 gap-6 mb-6">
        <!-- HRM -->
        <!-- Source: NUMBER_VERIFICATION.md, lines 43-44 -->
        <div class="model-card bg-blue-900/30 p-4 rounded-lg border-2 border-blue-500">
          <h3 class="text-xl font-bold mb-3 text-blue-400">
            <a href="https://arxiv.org/abs/2506.21734" target="_blank" class="hover:underline">
              HRM (2025) 🔗
            </a>
          </h3>
          <ul class="space-y-1 text-base">
            <li>📊 27M parameters</li>
            <li>🏗️ Complex hierarchy (H/L)</li>
            <li>✅ 32% ARC-AGI-1 (verified)</li>
            <li>
              <a href="https://arcprize.org/blog/hrm-analysis" target="_blank" class="hover:underline">
                📉 40% → 32% (verification drop) 🔗
              </a>
              <Citation citeId="hrm-verification-drop" inline={true} />
            </li>
          </ul>
        </div>
        
        <!-- TRM -->
        <div class="model-card bg-orange-900/30 p-4 rounded-lg border-2 border-orange-500">
          <h3 class="text-xl font-bold mb-3 text-orange-400">
            <a href="https://arxiv.org/abs/2510.04871" target="_blank" class="hover:underline">
              TRM (2025) 🔗
            </a>
          </h3>
          <ul class="space-y-1 text-base">
            <li>📊 7M parameters (4x smaller!)</li>
            <li>🏗️ Simple 2-layer network</li>
            <li>✅ 45% ARC-AGI-1 (claimed)</li>
            <li>❓ Not yet verified</li>
          </ul>
        </div>
      </div>
    {/if}
    
    <div class="teaser text-center text-lg text-black">
      <p>Both papers invoke Kahneman's "Thinking, Fast and Slow"...</p>
    </div>
  </div>
</div>

