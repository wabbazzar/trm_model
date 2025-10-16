<script>
  import Citation from '../components/Citation.svelte';
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">Enter HRM</h1>
    <h2 class="slide-subtitle text-center">Thinking, Fast and Slow... in Neural Networks?</h2>
    
    <div class="content-area">
      <div class="grid grid-cols-2 gap-4 mb-4">
        <!-- Architecture -->
        <div class="architecture-section">
          <h3 class="text-xl font-bold mb-2 text-slate-800">
            HRM's Core Idea
            <Citation citeId="hrm-core-architecture" inline={true} />
          </h3>
          <img src="/assets/hrm_architecture.svg" alt="HRM Architecture" class="w-full mb-2" />
          <ul class="space-y-1 text-sm text-slate-700">
            <li><strong class="text-blue-600">H-Network:</strong> Slow, abstract planning</li>
            <li><strong class="text-blue-600">L-Network:</strong> Fast, detailed execution</li>
            <li>Recursive interaction between them</li>
            <li><strong class="text-purple-600">ACT Halting:</strong> Q-learning when to stop <Citation citeId="hrm-act-mechanism" inline={true} /></li>
          </ul>
        </div>
        
        <!-- Kahneman Connection -->
        <div class="kahneman-section">
          <h3 class="text-xl font-bold mb-2 text-slate-800">Kahneman Connection</h3>
          <img src="/assets/kahneman_systems.svg" alt="Kahneman Systems" class="w-full mb-2" />
          <div class="mapping bg-blue-50 p-3 rounded-lg text-sm">
            <p class="mb-1"><strong>Brain's System 1:</strong> Fast, automatic</p>
            <p class="mb-1"><strong>Brain's System 2:</strong> Slow, analytical</p>
            <hr class="my-2 border-blue-300" />
            <p class="mb-1"><strong>HRM's L-network:</strong> High frequency</p>
            <p><strong>HRM's H-network:</strong> Low frequency</p>
          </div>
        </div>
      </div>
      
      <div class="quote-box bg-blue-100 border-l-4 border-blue-600 p-3 rounded-r-lg">
        <p class="text-sm italic text-slate-700">
          "Inspired by hierarchical and multi-timescale processing in the human brain..."
        </p>
        <p class="text-xs text-slate-600 mt-1">— HRM Paper (Wang et al., 2025)</p>
      </div>
      
      <div class="result mt-3 text-center">
        <p class="text-lg font-bold">Result: <span class="text-blue-600">40%</span> claimed, <span class="text-orange-600">32%</span> verified</p>
      </div>
    </div>
  </div>
</div>

