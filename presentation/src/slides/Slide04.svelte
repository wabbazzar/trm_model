<script>
  import Citation from '../components/Citation.svelte';
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">TRM Simplifies</h1>
    <h2 class="slide-subtitle text-center">What if System 1/System 2 is the wrong analogy?</h2>
    
    <div class="content-area">
      <div class="grid grid-cols-2 gap-4 mb-4">
        <!-- HRM -->
        <div class="comparison-box bg-blue-50 p-3 rounded-lg border-2 border-blue-500">
          <h3 class="text-xl font-bold mb-2 text-blue-600">HRM</h3>
          <img src="/assets/hrm_architecture.svg" alt="HRM" class="w-full mb-2" />
          <ul class="space-y-1 text-sm text-slate-700">
            <li>✅ Two networks (H & L)</li>
            <li>✅ Hierarchical recursion</li>
            <li>✅ 27M parameters</li>
            <li>✅ 4 layers × 2 networks</li>
            <li>📊 32% verified</li>
          </ul>
        </div>
        
        <!-- TRM -->
        <div class="comparison-box bg-orange-50 p-3 rounded-lg border-2 border-orange-500">
          <h3 class="text-xl font-bold mb-2 text-orange-600">
            TRM
            <Citation citeId="trm-core-architecture" inline={true} />
          </h3>
          <img src="/assets/trm_architecture.svg" alt="TRM" class="w-full mb-2" />
          <ul class="space-y-1 text-sm text-slate-700">
            <li>❌ Single network</li>
            <li>❌ No hierarchy</li>
            <li>✅ 7M parameters (4x smaller!)</li>
            <li>✅ Just 2 layers</li>
            <li>📊 45% claimed</li>
          </ul>
        </div>
      </div>
      
      <div class="paradox bg-gradient-to-r from-orange-100 to-red-100 p-4 rounded-lg border-2 border-orange-500">
        <h3 class="text-xl font-bold mb-2 text-center text-slate-800">The Paradox</h3>
        <div class="grid grid-cols-3 gap-3 text-center">
          <div>
            <p class="text-3xl font-bold text-orange-600">❌</p>
            <p class="text-sm">Removes hierarchy</p>
          </div>
          <div>
            <p class="text-3xl font-bold text-green-600">✨</p>
            <p class="text-sm">Better performance</p>
          </div>
          <div>
            <p class="text-3xl font-bold text-blue-600">🎯</p>
            <p class="text-sm">4x fewer params</p>
          </div>
        </div>
      </div>
      
      <div class="key-question mt-4 text-center">
        <p class="text-lg font-bold text-slate-800">
          "If the biological inspiration matters, why does 
          <span class="text-orange-600">removing it</span> 
          improve performance?"
        </p>
      </div>
    </div>
  </div>
</div>

