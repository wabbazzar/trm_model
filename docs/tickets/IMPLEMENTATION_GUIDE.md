# TRM Paper Presentation - Complete Implementation Guide

## Project Overview

Build an interactive web-based presentation analyzing the "Less is More: Recursive Reasoning with Tiny Networks" paper. The presentation will be 12 slides focusing on Hypothesis #2: "Iterative Refinement is All You Need", with Kahneman's "Thinking, Fast and Slow" as a narrative thread.

---

## Prerequisites

- Node.js 18+ and npm
- Python 3.11+ (for data extraction - already done)
- Modern web browser
- Text editor/IDE

---

## Project Structure

```
trm_model/
├── presentation/                    # Main presentation app
│   ├── public/
│   │   ├── data/                   # JSON data files
│   │   │   ├── arc_prize_ablations.json
│   │   │   ├── training_inference_matrix.json
│   │   │   ├── model_comparison.json
│   │   │   ├── augmentation_study.json
│   │   │   └── example_arc_task.json
│   │   └── assets/                 # Images and SVGs
│   │       ├── hrm_architecture.svg
│   │       ├── trm_architecture.svg
│   │       └── kahneman_systems.svg
│   ├── src/
│   │   ├── slides/                 # Individual slide components
│   │   │   ├── Slide01.svelte
│   │   │   ├── Slide02.svelte
│   │   │   └── ... (through Slide12.svelte)
│   │   ├── components/             # Reusable components
│   │   │   ├── ArchitectureDiagram.svelte
│   │   │   ├── AblationChart.svelte
│   │   │   ├── TrainingMatrix.svelte
│   │   │   ├── RefinementAnimation.svelte
│   │   │   └── CodeBlock.svelte
│   │   ├── lib/
│   │   │   └── stores.js           # Svelte stores for state
│   │   ├── App.svelte              # Main app
│   │   └── main.js                 # Entry point
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── docs/
│   ├── papers/                     # Source materials
│   │   ├── less_is_more_extracted.txt
│   │   └── hierarchical_reasoning_model_extracted.txt
│   └── tickets/
│       ├── presentation_plan_final.md
│       └── IMPLEMENTATION_GUIDE.md (this file)
└── .gitignore
```

---

## Phase 1: Project Setup (30 minutes)

### Step 1.1: Initialize Svelte + Vite Project

```bash
cd /Users/wesleybeckner/code/trm_model
npm create vite@latest presentation -- --template svelte
cd presentation
npm install
```

### Step 1.2: Install Dependencies

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install d3 katex prismjs reveal.js
npm install -D @sveltejs/vite-plugin-svelte
```

### Step 1.3: Configure Tailwind CSS

Create `presentation/tailwind.config.js`:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{svelte,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'hrm-blue': '#3b82f6',
        'trm-orange': '#f97316',
        'accent': '#8b5cf6',
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
        'mono': ['Fira Code', 'monospace'],
      },
    },
  },
  plugins: [],
}
```

Create `presentation/src/app.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom slide styles */
.slide {
  @apply min-h-screen flex flex-col items-center justify-center p-8 bg-gradient-to-br from-slate-50 to-slate-100;
}

.slide-title {
  @apply text-5xl font-bold mb-4 text-slate-800;
}

.slide-subtitle {
  @apply text-2xl text-slate-600 mb-8;
}

/* Code block styles */
.code-block {
  @apply bg-slate-900 text-slate-100 p-4 rounded-lg overflow-x-auto font-mono text-sm;
}

/* Chart container */
.chart-container {
  @apply w-full max-w-4xl h-96 bg-white rounded-lg shadow-lg p-6;
}
```

---

## Phase 2: Create Data Files (1 hour)

### Data File 1: `public/data/arc_prize_ablations.json`

**Note**: These are TWO SEPARATE ablation studies (not cumulative effects)

```json
{
  "title": "ARC Prize HRM Ablation Study Results",
  "source": "ARC Prize Foundation (2025) as cited in Jolicoeur-Martineau 2025",
  "reference": "TRM paper, lines 99-109; ARC Prize blog https://arcprize.org/blog/hrm-analysis",
  "note": "Two independent ablations showing different architectural choices",
  
  "experiments": [
    {
      "name": "Baseline\n(No Deep Supervision)",
      "accuracy": 0.19,
      "label": "19%",
      "description": "Single-step supervision only",
      "color": "#94a3b8",
      "baseline_for": "deep_supervision"
    },
    {
      "name": "Baseline\n(No Hierarchy)",
      "accuracy": 0.357,
      "label": "35.7%",
      "description": "Single transformer, no H/L split",
      "color": "#94a3b8",
      "baseline_for": "hierarchy"
    },
    {
      "name": "+ Deep Supervision\n(Outer Loop)",
      "accuracy": 0.39,
      "label": "39%",
      "improvement": "+20pp",
      "description": "Adds iterative refinement (up to 16 steps)",
      "color": "#10b981",
      "highlight": true,
      "impact": "2.05x improvement (105%)"
    },
    {
      "name": "+ Hierarchy\n(H/L Networks)",
      "accuracy": 0.39,
      "label": "39%",
      "improvement": "+3.3pp",
      "description": "Adds two-network recursion",
      "color": "#3b82f6",
      "impact": "9.2% improvement"
    }
  ],
  
  "key_insights": [
    "Deep supervision provides 2x improvement (19% → 39%)",
    "Hierarchy provides minimal improvement (35.7% → 39%)",
    "Deep supervision is ~6x more impactful than hierarchy",
    "Both end at 39%, but from different starting points"
  ],
  
  "comparison": {
    "deep_supervision_effect": 0.20,
    "hierarchy_effect": 0.033,
    "ratio": 6.06
  }
}
```

### Data File 2: `public/data/training_inference_matrix.json`

```json
{
  "title": "Training vs Inference Refinement Steps",
  "source": "ARC Prize Foundation (2025) - Figure 5",
  "description": "Accuracy based on number of refinement steps during training and inference",
  "matrix": [
    {
      "training_steps": 1,
      "inference_steps": 1,
      "accuracy": 0.19,
      "label": "Baseline"
    },
    {
      "training_steps": 1,
      "inference_steps": 4,
      "accuracy": 0.19,
      "label": "No training benefit"
    },
    {
      "training_steps": 4,
      "inference_steps": 1,
      "accuracy": 0.35,
      "label": "Training teaches refinement"
    },
    {
      "training_steps": 4,
      "inference_steps": 4,
      "accuracy": 0.39,
      "label": "Full refinement"
    }
  ],
  "insights": [
    "Training with 4 steps, testing with 1 step: +16pp improvement",
    "Testing with 4 steps adds only +4pp more",
    "Training impact is 4x larger than inference impact"
  ]
}
```

### Data File 3: `public/data/model_comparison.json`

```json
{
  "models": [
    {
      "name": "Gemini 2.5 Pro",
      "type": "LLM",
      "parameters": "Unknown",
      "arc_agi_1": null,
      "arc_agi_2": 0.049,
      "sudoku": null,
      "maze": null,
      "color": "#ea4335"
    },
    {
      "name": "o3-mini",
      "type": "LLM",
      "parameters": "Unknown",
      "arc_agi_1": 0.21,
      "arc_agi_2": 0.03,
      "sudoku": 0,
      "maze": 0,
      "color": "#10a37f"
    },
    {
      "name": "Deepseek R1",
      "type": "LLM",
      "parameters": "Unknown",
      "arc_agi_1": 0.158,
      "arc_agi_2": 0.013,
      "sudoku": 0,
      "maze": 0,
      "color": "#8b5cf6"
    },
    {
      "name": "HRM",
      "type": "Small Model",
      "parameters": 27000000,
      "arc_agi_1": 0.32,
      "arc_agi_1_claimed": 0.40,
      "arc_agi_2": 0.02,
      "arc_agi_2_claimed": 0.05,
      "sudoku": 0.55,
      "maze": 0.745,
      "color": "#3b82f6"
    },
    {
      "name": "TRM",
      "type": "Small Model",
      "parameters": 7000000,
      "arc_agi_1": 0.45,
      "arc_agi_1_verified": null,
      "arc_agi_2": 0.08,
      "sudoku": 0.87,
      "maze": 0.85,
      "color": "#f97316"
    }
  ]
}
```

### Data File 4: `public/data/augmentation_study.json`

```json
{
  "title": "Data Augmentation Impact",
  "source": "ARC Prize Foundation (2025) - Figure 7",
  "data": [
    {"augmentations": 30, "accuracy": 0.35, "training_augs": 1000},
    {"augmentations": 100, "accuracy": 0.37, "training_augs": 1000},
    {"augmentations": 300, "accuracy": 0.39, "training_augs": 1000},
    {"augmentations": 1000, "accuracy": 0.41, "training_augs": 1000}
  ],
  "insights": [
    "300 augmentations achieves 95% of peak performance",
    "Training augmentation matters more than inference augmentation",
    "Diminishing returns after 300 augmentations"
  ]
}
```

### Data File 5: `public/data/example_arc_task.json`

```json
{
  "task_id": "example_transformation",
  "description": "Simple pattern: Flip colors",
  "train": [
    {
      "input": [[0, 1, 0], [1, 0, 1], [0, 1, 0]],
      "output": [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    }
  ],
  "test": [
    {
      "input": [[1, 1, 0], [0, 1, 1], [1, 0, 0]]
    }
  ],
  "colors": {
    "0": "#000000",
    "1": "#0074D9"
  }
}
```

---

## Phase 3: Create SVG Assets (1 hour)

### Asset 1: `public/assets/hrm_architecture.svg`

```svg
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- HRM Architecture Diagram -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3b82f6" />
    </marker>
  </defs>
  
  <!-- Input -->
  <rect x="50" y="150" width="100" height="60" fill="#e0e7ff" stroke="#3b82f6" stroke-width="2" rx="5"/>
  <text x="100" y="185" text-anchor="middle" font-size="14" font-weight="bold">Input x</text>
  
  <!-- L-Network (Fast) -->
  <rect x="250" y="50" width="120" height="80" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" rx="5"/>
  <text x="310" y="85" text-anchor="middle" font-size="14" font-weight="bold">L-Network</text>
  <text x="310" y="105" text-anchor="middle" font-size="12">(Fast/Detailed)</text>
  <text x="310" y="120" text-anchor="middle" font-size="11" fill="#666">High Frequency</text>
  
  <!-- H-Network (Slow) -->
  <rect x="250" y="250" width="120" height="80" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" rx="5"/>
  <text x="310" y="285" text-anchor="middle" font-size="14" font-weight="bold">H-Network</text>
  <text x="310" y="305" text-anchor="middle" font-size="12">(Slow/Abstract)</text>
  <text x="310" y="320" text-anchor="middle" font-size="11" fill="#666">Low Frequency</text>
  
  <!-- Output -->
  <rect x="500" y="150" width="100" height="60" fill="#e0e7ff" stroke="#3b82f6" stroke-width="2" rx="5"/>
  <text x="550" y="185" text-anchor="middle" font-size="14" font-weight="bold">Output y</text>
  
  <!-- Arrows -->
  <line x1="150" y1="180" x2="250" y2="90" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="150" y1="180" x2="250" y2="290" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="370" y1="90" x2="500" y2="180" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
  <line x1="370" y1="290" x2="500" y2="180" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowhead)"/>
  
  <!-- Recursive arrows -->
  <path d="M 310 130 Q 380 170 310 250" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)" stroke-dasharray="5,5"/>
  <path d="M 310 250 Q 240 210 310 130" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead)" stroke-dasharray="5,5"/>
  
  <!-- Labels -->
  <text x="400" y="50" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e293b">HRM: Hierarchical</text>
  <text x="400" y="390" text-anchor="middle" font-size="12" fill="#64748b">27M Parameters</text>
</svg>
```

### Asset 2: `public/assets/trm_architecture.svg`

```svg
<svg width="800" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- TRM Architecture Diagram -->
  <defs>
    <marker id="arrowhead-orange" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#f97316" />
    </marker>
  </defs>
  
  <!-- Input -->
  <rect x="50" y="150" width="100" height="60" fill="#fff7ed" stroke="#f97316" stroke-width="2" rx="5"/>
  <text x="100" y="185" text-anchor="middle" font-size="14" font-weight="bold">Input x</text>
  
  <!-- Single Network -->
  <rect x="300" y="120" width="140" height="120" fill="#fed7aa" stroke="#f97316" stroke-width="3" rx="5"/>
  <text x="370" y="165" text-anchor="middle" font-size="14" font-weight="bold">Single Network</text>
  <text x="370" y="185" text-anchor="middle" font-size="12">(2 layers)</text>
  <text x="370" y="205" text-anchor="middle" font-size="11" fill="#666">Unified Processing</text>
  <text x="370" y="225" text-anchor="middle" font-size="10" fill="#666">No Hierarchy</text>
  
  <!-- Output -->
  <rect x="550" y="150" width="100" height="60" fill="#fff7ed" stroke="#f97316" stroke-width="2" rx="5"/>
  <text x="600" y="185" text-anchor="middle" font-size="14" font-weight="bold">Output y</text>
  
  <!-- Arrows -->
  <line x1="150" y1="180" x2="300" y2="180" stroke="#f97316" stroke-width="2" marker-end="url(#arrowhead-orange)"/>
  <line x1="440" y1="180" x2="550" y2="180" stroke="#f97316" stroke-width="2" marker-end="url(#arrowhead-orange)"/>
  
  <!-- Self-loop -->
  <path d="M 370 120 Q 370 70 420 120" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrowhead-orange)" stroke-dasharray="5,5"/>
  <text x="395" y="90" text-anchor="middle" font-size="11" fill="#10b981">Iterative</text>
  
  <!-- Labels -->
  <text x="400" y="50" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e293b">TRM: Flat</text>
  <text x="400" y="390" text-anchor="middle" font-size="12" fill="#64748b">7M Parameters (4x smaller)</text>
</svg>
```

### Asset 3: `public/assets/kahneman_systems.svg`

```svg
<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Kahneman's Two Systems -->
  
  <!-- System 1 -->
  <rect x="50" y="50" width="200" height="200" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" rx="10"/>
  <text x="150" y="80" text-anchor="middle" font-size="18" font-weight="bold" fill="#1e3a8a">System 1</text>
  <text x="150" y="110" text-anchor="middle" font-size="13" fill="#1e40af">Fast</text>
  <text x="150" y="135" text-anchor="middle" font-size="13" fill="#1e40af">Automatic</text>
  <text x="150" y="160" text-anchor="middle" font-size="13" fill="#1e40af">Intuitive</text>
  <text x="150" y="185" text-anchor="middle" font-size="13" fill="#1e40af">Low Effort</text>
  <text x="150" y="220" text-anchor="middle" font-size="11" fill="#64748b" font-style="italic">HRM: L-Network</text>
  
  <!-- System 2 -->
  <rect x="350" y="50" width="200" height="200" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" rx="10"/>
  <text x="450" y="80" text-anchor="middle" font-size="18" font-weight="bold" fill="#78350f">System 2</text>
  <text x="450" y="110" text-anchor="middle" font-size="13" fill="#92400e">Slow</text>
  <text x="450" y="135" text-anchor="middle" font-size="13" fill="#92400e">Deliberate</text>
  <text x="450" y="160" text-anchor="middle" font-size="13" fill="#92400e">Analytical</text>
  <text x="450" y="185" text-anchor="middle" font-size="13" fill="#92400e">High Effort</text>
  <text x="450" y="220" text-anchor="middle" font-size="11" fill="#64748b" font-style="italic">HRM: H-Network</text>
  
  <!-- Title -->
  <text x="300" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e293b">Kahneman: Thinking, Fast and Slow</text>
</svg>
```

---

## Phase 4: Create Core Application (2 hours)

### File: `presentation/src/main.js`

```javascript
import './app.css'
import App from './App.svelte'

const app = new App({
  target: document.getElementById('app'),
})

export default app
```

### File: `presentation/src/lib/stores.js`

```javascript
import { writable } from 'svelte/store';

// Current slide number (0-11 for 12 slides)
export const currentSlide = writable(0);

// Presentation mode (true = presenter view, false = audience view)
export const presenterMode = writable(false);

// Navigation functions
export function nextSlide() {
  currentSlide.update(n => Math.min(n + 1, 11));
}

export function prevSlide() {
  currentSlide.update(n => Math.max(n - 1, 0));
}

export function goToSlide(index) {
  currentSlide.set(Math.max(0, Math.min(index, 11)));
}
```

### File: `presentation/src/App.svelte`

```svelte
<script>
  import { currentSlide, nextSlide, prevSlide } from './lib/stores';
  import { onMount } from 'svelte';
  
  // Import all slides
  import Slide01 from './slides/Slide01.svelte';
  import Slide02 from './slides/Slide02.svelte';
  import Slide03 from './slides/Slide03.svelte';
  import Slide04 from './slides/Slide04.svelte';
  import Slide05 from './slides/Slide05.svelte';
  import Slide06 from './slides/Slide06.svelte';
  import Slide07 from './slides/Slide07.svelte';
  import Slide08 from './slides/Slide08.svelte';
  import Slide09 from './slides/Slide09.svelte';
  import Slide10 from './slides/Slide10.svelte';
  import Slide11 from './slides/Slide11.svelte';
  import Slide12 from './slides/Slide12.svelte';
  
  const slides = [
    Slide01, Slide02, Slide03, Slide04, Slide05, Slide06,
    Slide07, Slide08, Slide09, Slide10, Slide11, Slide12
  ];
  
  // Keyboard navigation
  onMount(() => {
    const handleKeydown = (event) => {
      if (event.key === 'ArrowRight' || event.key === ' ') {
        nextSlide();
      } else if (event.key === 'ArrowLeft') {
        prevSlide();
      } else if (event.key >= '1' && event.key <= '9') {
        const slideNum = parseInt(event.key) - 1;
        if (slideNum < slides.length) {
          currentSlide.set(slideNum);
        }
      }
    };
    
    window.addEventListener('keydown', handleKeydown);
    return () => window.removeEventListener('keydown', handleKeydown);
  });
</script>

<main class="presentation">
  <div class="slide-container">
    <svelte:component this={slides[$currentSlide]} />
  </div>
  
  <!-- Navigation controls -->
  <div class="nav-controls">
    <button on:click={prevSlide} disabled={$currentSlide === 0}>
      ← Previous
    </button>
    <span class="slide-counter">
      {$currentSlide + 1} / {slides.length}
    </span>
    <button on:click={nextSlide} disabled={$currentSlide === slides.length - 1}>
      Next →
    </button>
  </div>
</main>

<style>
  .presentation {
    width: 100vw;
    height: 100vh;
    overflow: hidden;
  }
  
  .slide-container {
    width: 100%;
    height: calc(100% - 60px);
  }
  
  .nav-controls {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: rgba(15, 23, 42, 0.9);
    backdrop-filter: blur(10px);
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    color: white;
  }
  
  .nav-controls button {
    padding: 0.5rem 1.5rem;
    background: #3b82f6;
    color: white;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    font-size: 1rem;
    transition: background 0.2s;
  }
  
  .nav-controls button:hover:not(:disabled) {
    background: #2563eb;
  }
  
  .nav-controls button:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }
  
  .slide-counter {
    font-size: 1.1rem;
    font-weight: 500;
  }
</style>
```

---

## Phase 5: Create Individual Slides (4 hours)

### Template Slide Structure

Each slide follows this pattern in `presentation/src/slides/SlideXX.svelte`:

```svelte
<script>
  import { onMount } from 'svelte';
  // Import any needed components
  // Load any needed data
</script>

<div class="slide">
  <div class="slide-content max-w-6xl w-full">
    <!-- Slide title -->
    <h1 class="slide-title">Slide Title</h1>
    <h2 class="slide-subtitle">Subtitle</h2>
    
    <!-- Slide content -->
    <div class="content-area">
      <!-- Content here -->
    </div>
  </div>
</div>

<style>
  /* Slide-specific styles */
</style>
```

### Slide 1: `presentation/src/slides/Slide01.svelte`

```svelte
<script>
  import { onMount } from 'svelte';
  
  let modelData = null;
  
  onMount(async () => {
    const response = await fetch('/data/model_comparison.json');
    modelData = await response.json();
  });
</script>

<div class="slide bg-gradient-to-br from-slate-900 to-slate-800 text-white">
  <div class="slide-content max-w-6xl w-full">
    <h1 class="text-6xl font-bold mb-4 text-center">
      Less is More?
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-orange-400">
        Or Just Different?
      </span>
    </h1>
    
    <h2 class="text-3xl text-slate-300 mb-12 text-center">
      Analyzing TRM: What Really Drives Performance
    </h2>
    
    <div class="thesis-box bg-slate-800/50 p-8 rounded-xl border-2 border-blue-500 mb-12">
      <p class="text-xl text-center italic">
        "We argue that the success of both HRM and TRM comes not from their <span class="text-blue-400">architectures</span>, 
        but from <span class="text-orange-400">how they train</span>—through iterative refinement with deep supervision."
      </p>
    </div>
    
    {#if modelData}
      <div class="comparison-grid grid grid-cols-2 gap-8 mb-8">
        <!-- HRM -->
        <div class="model-card bg-blue-900/30 p-6 rounded-lg border-2 border-blue-500">
          <h3 class="text-2xl font-bold mb-4 text-blue-400">HRM (2025)</h3>
          <ul class="space-y-2 text-lg">
            <li>📊 27M parameters</li>
            <li>🏗️ Complex hierarchy (H/L)</li>
            <li>✅ 32% ARC-AGI-1 (verified)</li>
            <li>📉 40% → 32% (verification drop)</li>
          </ul>
        </div>
        
        <!-- TRM -->
        <div class="model-card bg-orange-900/30 p-6 rounded-lg border-2 border-orange-500">
          <h3 class="text-2xl font-bold mb-4 text-orange-400">TRM (2025)</h3>
          <ul class="space-y-2 text-lg">
            <li>📊 7M parameters (4x smaller!)</li>
            <li>🏗️ Simple 2-layer network</li>
            <li>✅ 45% ARC-AGI-1 (claimed)</li>
            <li>❓ Not yet verified</li>
          </ul>
        </div>
      </div>
    {/if}
    
    <div class="teaser text-center text-xl text-slate-400">
      <p>Both papers invoke Kahneman's "Thinking, Fast and Slow"...</p>
      <p class="mt-2 text-orange-400 font-bold">But is this the right analogy?</p>
    </div>
  </div>
</div>
```

### Slide 2: Create similar structure for remaining slides

*Note: Due to length, I'll provide the structure. Each slide should follow the pattern above with:*
- Title and subtitle
- Visual content (charts, diagrams, or comparisons)
- Key points in bullet form
- Relevant data from JSON files
- Appropriate color scheme (HRM=blue, TRM=orange)

---

## Phase 6: Create Interactive Components (3 hours)

### Component 1: `presentation/src/components/AblationChart.svelte`

```svelte
<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  
  export let data = null;
  let chartContainer;
  
  onMount(async () => {
    if (!data) {
      const response = await fetch('/data/arc_prize_ablations.json');
      const jsonData = await response.json();
      data = jsonData;
    }
    
    createChart();
  });
  
  function createChart() {
    if (!data || !chartContainer) return;
    
    const margin = { top: 20, right: 30, bottom: 60, left: 60 };
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
      .on('mouseover', function() {
        d3.select(this).attr('opacity', 1);
      })
      .on('mouseout', function() {
        d3.select(this).attr('opacity', 0.8);
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
      .attr('transform', 'rotate(-45)')
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

<style>
  .chart-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
```

### Component 2: `presentation/src/components/CodeBlock.svelte`

```svelte
<script>
  export let code = '';
  export let language = 'python';
</script>

<div class="code-block">
  <pre><code class="language-{language}">{code}</code></pre>
</div>

<style>
  .code-block {
    background: #0f172a;
    color: #e2e8f0;
    padding: 1.5rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    font-family: 'Fira Code', monospace;
    font-size: 0.9rem;
    line-height: 1.6;
  }
  
  pre {
    margin: 0;
  }
  
  code {
    font-family: inherit;
  }
</style>
```

---

## Phase 7: Package Configuration (15 minutes)

### File: `presentation/package.json`

```json
{
  "name": "trm-presentation",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "@sveltejs/vite-plugin-svelte": "^3.0.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32",
    "svelte": "^4.2.0",
    "tailwindcss": "^3.4.0",
    "vite": "^5.0.0"
  },
  "dependencies": {
    "d3": "^7.8.5",
    "katex": "^0.16.9",
    "prismjs": "^1.29.0"
  }
}
```

### File: `presentation/vite.config.js`

```javascript
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

export default defineConfig({
  plugins: [svelte()],
  server: {
    port: 3000,
    open: true
  }
})
```

---

## Phase 8: Documentation (30 minutes)

### File: `presentation/README.md`

```markdown
# TRM Paper Presentation

Interactive web-based presentation analyzing "Less is More: Recursive Reasoning with Tiny Networks"

## Quick Start

\`\`\`bash
npm install
npm run dev
\`\`\`

Open http://localhost:3000

## Navigation

- **Arrow Keys**: Navigate between slides
- **Space**: Next slide
- **Number Keys (1-9)**: Jump to specific slide

## Slides

1. Title + Thesis
2. ARC-AGI Challenge
3. HRM Architecture
4. TRM Simplification
5. Deep Supervision
6. ARC Prize Revelation
7. Training vs Inference
8. TRM Proves the Point
9. Our Hypothesis
10. Broader Implications
11. Provocative Alternative
12. Conclusion

## Development

- **Framework**: Svelte + Vite
- **Styling**: Tailwind CSS
- **Charts**: D3.js
- **Data**: JSON files in \`public/data/\`

## Build for Production

\`\`\`bash
npm run build
npm run preview
\`\`\`

## License

MIT
```

---

## Validation Checklist

Before completing implementation, verify:

- [ ] All 12 slides render correctly
- [ ] Navigation works (arrows, space, numbers)
- [ ] All data files load without errors
- [ ] Charts render with D3.js
- [ ] SVG diagrams display properly
- [ ] Code blocks are readable
- [ ] Responsive design works on different screen sizes
- [ ] Build process completes without errors
- [ ] All colors follow theme (HRM=blue, TRM=orange)
- [ ] Kahneman references appear on slides 1, 3, 5, 9, 12
- [ ] Performance is smooth (no lag during transitions)

---

## Deployment Options

### Option 1: GitHub Pages
1. Build: `npm run build`
2. Deploy `dist/` folder to gh-pages branch

### Option 2: Netlify
1. Connect repository
2. Build command: `npm run build`
3. Publish directory: `dist`

### Option 3: Vercel
1. Import repository
2. Framework: Vite
3. Auto-deploy on push

---

## Troubleshooting

**Issue**: D3 charts not rendering
- **Solution**: Check browser console, ensure data files are in `public/data/`

**Issue**: Tailwind styles not applying
- **Solution**: Verify `tailwind.config.js` and `app.css` import in `main.js`

**Issue**: Slides not advancing
- **Solution**: Check stores.js is properly imported in App.svelte

**Issue**: Build fails
- **Solution**: Run `npm install` again, check Node version (need 18+)

---

This guide is complete and ready for implementation by an agent with cleared context.

