<script>
  // Our Hypothesis
</script>

<div class="slide bg-gradient-to-br from-purple-50 to-blue-50">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center text-purple-800">Our Hypothesis</h1>
    <h2 class="slide-subtitle text-center text-purple-600">Iterative Refinement is All You Need</h2>
    
    <div class="content-area">
      <div class="claim bg-white p-4 rounded-lg shadow-lg mb-3 border-4 border-purple-500">
        <h3 class="text-xl font-bold mb-2 text-center text-slate-800">The Claim</h3>
        <p class="text-base text-slate-700 leading-relaxed">
          The entire architecture debate (hierarchy vs flat, H/L networks vs single network) is a 
          <strong class="text-red-600">distraction</strong>. What actually drives performance is:
        </p>
        <ol class="mt-3 space-y-2 text-base text-slate-700">
          <li><strong class="text-purple-600">1.</strong> Deep supervision during training</li>
          <li><strong class="text-purple-600">2.</strong> Iterative refinement at both train and inference time</li>
          <li><strong class="text-purple-600">3.</strong> Adaptive halting to know when to stop</li>
          <li><strong class="text-purple-600">4.</strong> Architecture is secondary</li>
        </ol>
      </div>
      
      <div class="evidence bg-green-50 p-4 rounded-lg border-2 border-green-500 mb-3">
        <h3 class="text-xl font-bold mb-2 text-green-800">Supporting Evidence</h3>
        <div class="grid grid-cols-2 gap-3">
          <div class="evidence-item bg-white p-3 rounded-lg shadow text-sm">
            <p class="font-bold text-green-700 mb-1">✅ ARC Prize Ablations</p>
            <p class="text-xs text-slate-600">2x from outer loop vs 9% from hierarchy</p>
          </div>
          <div class="evidence-item bg-white p-3 rounded-lg shadow text-sm">
            <p class="font-bold text-green-700 mb-1">✅ TRM's Simplification</p>
            <p class="text-xs text-slate-600">Remove hierarchy → improve performance</p>
          </div>
          <div class="evidence-item bg-white p-3 rounded-lg shadow text-sm">
            <p class="font-bold text-green-700 mb-1">✅ Training Dynamics</p>
            <p class="text-xs text-slate-600">Train with refinement helps single-pass inference</p>
          </div>
          <div class="evidence-item bg-white p-3 rounded-lg shadow text-sm">
            <p class="font-bold text-green-700 mb-1">✅ Shared Components</p>
            <p class="text-xs text-slate-600">Both models share deep supervision, differ in architecture</p>
          </div>
        </div>
      </div>
      
      <div class="predictions bg-blue-50 p-4 rounded-lg border-2 border-blue-500 mb-3">
        <h3 class="text-xl font-bold mb-2 text-blue-800">Testable Predictions</h3>
        <ol class="space-y-1 text-sm text-slate-700">
          <li>1. Vanilla 2-layer Transformer + deep supervision → ~40% on ARC-AGI</li>
          <li>2. Remove deep supervision from TRM → collapse to ~20%</li>
          <li>3. Apply deep supervision to CNN/RNN → see similar 2x improvement</li>
          <li>4. Architecture choice has &lt;10% impact vs refinement strategy</li>
        </ol>
      </div>
      
      <div class="kahneman-revisited bg-purple-100 border-l-4 border-purple-600 p-3 rounded-r-lg">
        <h3 class="text-lg font-bold mb-2 text-purple-800">Kahneman Revisited</h3>
        <p class="text-base italic text-slate-700">
          "The real 'System 2' thinking isn't in the neural architecture—it's in the 
          <strong class="text-purple-600">training loop</strong> that teaches models to think iteratively"
        </p>
      </div>
    </div>
  </div>
</div>

