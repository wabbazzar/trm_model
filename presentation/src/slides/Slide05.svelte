<script>
  import CodeBlock from '../components/CodeBlock.svelte';
  import Citation from '../components/Citation.svelte';
  
  const code = `for step in range(16):  # Up to 16 refinement steps
    prediction = model(input, current_answer, latent_state)
    
    if good_enough(prediction):
        break  # Adaptive halting
    
    current_answer = prediction  # Refine
    latent_state = latent_state.detach()  # Carry forward`;
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="slide-title text-center">The Hidden Variable</h1>
    <h2 class="slide-subtitle text-center">Deep Supervision: The Outer Loop Nobody Talks About</h2>
    
    <div class="content-area">
      <div class="description bg-white p-4 rounded-lg shadow-lg mb-3">
        <p class="text-base text-slate-700 mb-2">
          Both models share a <strong>secret weapon</strong> that has nothing to do with hierarchy:
        </p>
        <h3 class="text-xl font-bold text-blue-600 mb-2">
          Deep Supervision (The Outer Loop)
          <Citation citeId="deep-supervision-both" inline={true} />
        </h3>
      </div>
      
      <CodeBlock {code} language="python" />
      
      <div class="grid grid-cols-2 gap-4 mt-3">
        <div class="what-it-does bg-blue-50 p-4 rounded-lg">
          <h3 class="text-lg font-bold mb-2 text-blue-800">What This Does:</h3>
          <ul class="space-y-1 text-sm text-slate-700">
            <li>✅ Predicts answer</li>
            <li>✅ Evaluates quality</li>
            <li>✅ Refines if needed</li>
            <li>✅ Repeats up to 16 times</li>
            <li><strong class="text-orange-600">Crucially:</strong> Trains with this loop!</li>
          </ul>
        </div>
        
        <div class="flow-diagram bg-green-50 p-4 rounded-lg">
          <h3 class="text-lg font-bold mb-2 text-green-800">Refinement Flow:</h3>
          <div class="flex flex-col space-y-2">
            <div class="step bg-white p-2 rounded shadow text-sm">1️⃣ Initial Prediction</div>
            <div class="arrow text-center text-xl">↓</div>
            <div class="step bg-white p-2 rounded shadow text-sm">2️⃣ Evaluate Quality</div>
            <div class="arrow text-center text-xl">↓</div>
            <div class="step bg-white p-2 rounded shadow text-sm">3️⃣ Refine Answer</div>
            <div class="arrow text-center text-xl">↺</div>
            <div class="step bg-green-100 p-2 rounded shadow font-bold text-sm">4️⃣ Repeat or Stop</div>
          </div>
        </div>
      </div>
      
      <div class="kahneman-reframe mt-3 bg-purple-100 border-l-4 border-purple-600 p-3 rounded-r-lg">
        <p class="text-base italic text-slate-800">
          <strong>Kahneman Reframe:</strong> "Maybe the real 'System 2' isn't the architecture—
          it's the <span class="text-purple-600 font-bold">iterative refinement process</span> itself"
        </p>
      </div>
    </div>
  </div>
</div>

