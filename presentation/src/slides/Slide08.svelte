<script>
  // TRM Proves the Point
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">TRM Proves the Point</h1>
    <h2 class="slide-subtitle text-center">Remove Complexity, Keep Performance</h2>
    
    <div class="content-area">
      <div class="comparison bg-white p-4 rounded-lg shadow-lg mb-3">
        <h3 class="text-xl font-bold mb-3 text-slate-800 text-center">Component Analysis</h3>
        
        <div class="grid grid-cols-2 gap-4">
          <!-- HRM -->
          <div class="hrm-components">
            <h4 class="text-lg font-bold mb-2 text-blue-600">What HRM Has:</h4>
            <ul class="space-y-1 text-sm">
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Deep supervision (outer loop)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Adaptive halting (ACT)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Iterative refinement</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-blue-600 text-xl">✅</span>
                <span>Two networks (H and L)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-blue-600 text-xl">✅</span>
                <span>Hierarchical recursion</span>
              </li>
            </ul>
          </div>
          
          <!-- TRM -->
          <div class="trm-components">
            <h4 class="text-lg font-bold mb-2 text-orange-600">What TRM Keeps:</h4>
            <ul class="space-y-1 text-sm">
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Deep supervision (outer loop)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Adaptive halting (ACT)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-green-600 text-xl">✅</span>
                <span>Iterative refinement</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-red-600 text-xl">❌</span>
                <span class="line-through text-slate-400">Just ONE network</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="text-red-600 text-xl">❌</span>
                <span class="line-through text-slate-400">No hierarchy</span>
              </li>
            </ul>
          </div>
        </div>
        
        <div class="result mt-3 p-3 bg-gradient-to-r from-orange-100 to-green-100 rounded-lg">
          <p class="text-center text-lg font-bold text-slate-800">
            Result: <span class="text-orange-600">45%</span> vs <span class="text-blue-600">32%</span> 
            (TRM wins!)
          </p>
        </div>
      </div>
      
      <div class="proof bg-green-50 p-4 rounded-lg border-2 border-green-500 mb-3">
        <h3 class="text-xl font-bold mb-2 text-green-800 text-center">The Proof</h3>
        <div class="logical-chain space-y-2 text-base text-slate-700">
          <p>1️⃣ If hierarchy was <strong>essential</strong>, removing it should hurt</p>
          <p>2️⃣ Removing it <strong>helps</strong> (45% vs 32%)</p>
          <p>3️⃣ Therefore: Hierarchy is <strong>not the driver</strong></p>
        </div>
      </div>
      
      <div class="venn-diagram bg-white p-4 rounded-lg shadow-lg">
        <h3 class="text-lg font-bold mb-2 text-slate-800 text-center">Shared Components = Performance Drivers</h3>
        <div class="flex justify-center items-center gap-4">
          <div class="component bg-green-100 p-3 rounded-lg border-2 border-green-500 text-center text-sm">
            <p class="font-bold text-green-700">Deep Supervision</p>
            <p class="text-xs text-slate-600">(Both)</p>
          </div>
          <div class="component bg-green-100 p-3 rounded-lg border-2 border-green-500 text-center text-sm">
            <p class="font-bold text-green-700">Iterative Refinement</p>
            <p class="text-xs text-slate-600">(Both)</p>
          </div>
          <div class="component bg-blue-100 p-3 rounded-lg border-2 border-blue-500 text-center opacity-50 text-sm">
            <p class="font-bold text-blue-700">Hierarchy</p>
            <p class="text-xs text-slate-600">(Optional)</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

