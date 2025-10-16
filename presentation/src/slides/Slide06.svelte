<script>
  import AblationChart from '../components/AblationChart.svelte';
  import Citation from '../components/Citation.svelte';
  import { onMount } from 'svelte';
  
  let ablationData = null;
  
  onMount(async () => {
    const response = await fetch('/data/arc_prize_ablations.json');
    ablationData = await response.json();
  });
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">The ARC Prize Revelation</h1>
    <h2 class="slide-subtitle text-center">Official Verification Changes Everything</h2>
    
    <div class="content-area">
      <div class="intro bg-white p-6 rounded-lg shadow-lg mb-6">
        <p class="text-lg text-slate-700 mb-4">
          <strong>ARC Prize Foundation (2025)</strong> ran controlled ablations on HRM:
          <Citation citeId="arc-prize-ablations" inline={true} />
        </p>
      </div>
      
      {#if ablationData}
        <AblationChart data={ablationData} />
        
        <div class="findings mt-6 bg-gradient-to-r from-green-100 to-blue-100 p-6 rounded-lg border-2 border-green-500">
          <h3 class="text-2xl font-bold mb-4 text-slate-800 text-center">The Smoking Gun</h3>
          <div class="grid grid-cols-2 gap-6">
            <div class="finding bg-white p-4 rounded-lg shadow">
              <p class="text-3xl font-bold text-green-600 mb-2">+20pp</p>
              <p class="text-lg">Outer Loop (Deep Supervision)</p>
              <p class="text-sm text-slate-600">19% → 39% (2x improvement)</p>
            </div>
            <div class="finding bg-white p-4 rounded-lg shadow">
              <p class="text-3xl font-bold text-blue-600 mb-2">+3.3pp</p>
              <p class="text-lg">Hierarchy (H/L Networks)</p>
              <p class="text-sm text-slate-600">35.7% → 39% (9% improvement)</p>
            </div>
          </div>
          <div class="conclusion mt-4 text-center">
            <p class="text-2xl font-bold text-orange-600">
              Deep supervision is <strong>~6x more impactful</strong> than hierarchy
            </p>
          </div>
        </div>
        
        <div class="quote mt-6 bg-slate-100 border-l-4 border-slate-600 p-6 rounded-r-lg">
          <p class="text-lg italic text-slate-700">
            "Deep supervision seems to be the primary driver of the performance gains... 
            while recursive hierarchical reasoning only slightly improved accuracy"
          </p>
          <p class="text-sm text-slate-600 mt-2">— ARC Prize Foundation, 2025</p>
        </div>
      {/if}
    </div>
  </div>
</div>

