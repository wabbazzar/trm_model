# Web-Based Presentation Plan: "Less is More - TRM Paper"

## Project Overview
Create an interactive web-based presentation analyzing the "Less is More: Recursive Reasoning with Tiny Networks" paper, comparing it to its parent work (HRM), and incorporating critical insights from the ARC Prize analysis.

---

## Top 3 Hypotheses (Choose One)

### 🥇 **Hypothesis 1: "The Simplicity Paradox - Less Architecture, More Overfitting"**

**Core Claim**: TRM's superior performance comes from *removing* architectural complexity, which paradoxically reduces overfitting and enables better task-specific memorization through recursive refinement.

**Supporting Evidence**:
- TRM: 7M params, 2 layers → 45% ARC-AGI-1
- HRM: 27M params, 4 layers × 2 networks → 40% ARC-AGI-1
- ARC Prize blog: hierarchy adds minimal value (35.7% → 39%)
- Recursive refinement (outer loop) is the real driver (19% → 39%)

**Testable Predictions**:
1. TRM would fail on truly novel tasks (worse than HRM on cross-dataset transfer)
2. TRM's performance scales with augmentation count more than HRM
3. TRM memorizes better but generalizes worse to unseen task types
4. Removing depth trades model capacity for optimization stability

**Presentation Angle**: "Why bigger models fail where smaller ones succeed - the curse of capacity in few-shot learning"

---

### 🥈 **Hypothesis 2: "Iterative Refinement is All You Need - Architecture is Noise"**

**Core Claim**: The entire debate about hierarchical vs. flat architecture misses the point - what matters is *iterative refinement with supervision at each step* (the outer loop). Both HRM and TRM succeed because of deep supervision, not their architectural choices.

**Supporting Evidence**:
- ARC Prize finding: Outer loop refinement gave 2x performance boost
- TRM removes hierarchy but keeps iterative refinement → better performance
- Both models use adaptive halting (ACT) to determine when to stop refining
- Training with refinement improves even single-pass inference by >15pp

**Testable Predictions**:
1. Any architecture (even vanilla transformer) + deep supervision would match TRM
2. Number of refinement steps during training matters more than during inference
3. The "halt or continue" mechanism is critical for training, not inference
4. Single-pass performance after training with refinement > multi-pass without

**Presentation Angle**: "The hidden variable: why we've been optimizing the wrong thing in neural architecture search"

---

### 🥉 **Hypothesis 3: "ARC-AGI is a Memory Test, Not a Reasoning Test (for these models)"**

**Core Claim**: Both HRM and TRM achieve high scores on ARC-AGI not through genuine abstract reasoning, but through sophisticated task-specific memorization enabled by: (1) training on evaluation tasks, (2) puzzle_id embeddings, and (3) massive data augmentation creating task-specific features.

**Supporting Evidence**:
- ARC Prize: Training on only 400 eval tasks → 31% (vs 41% with all data)
- Only 10pp drop without cross-task transfer
- Models use puzzle_id embeddings - can ONLY work on seen puzzle IDs
- 300 augmentations (vs 1000) achieves near-peak performance
- TRM better scores might just mean better memorization, not reasoning

**Testable Predictions**:
1. Both models would score ~0% on truly held-out ARC tasks with new puzzle_ids
2. Performance correlates with # training augmentations per eval task
3. Removing puzzle_id embeddings (using few-shot context) would collapse performance
4. Models cannot transfer learned "rules" to new instantiations of same concept

**Presentation Angle**: "The emperor has no clothes: what ARC-AGI scores really measure"

---

## Recommended Hypothesis: **#2 - "Iterative Refinement is All You Need"**

**Why This is Strongest**:
1. **Unifies findings**: Explains both TRM's success AND HRM's relative failure
2. **Actionable insights**: Suggests clear path forward (focus on training dynamics, not architecture)
3. **Balanced critique**: Acknowledges genuine contributions while questioning narrative
4. **Empirically grounded**: Directly supported by ARC Prize ablations
5. **Novel angle**: Shifts focus from "what architecture" to "how we train"

---

## Presentation Structure

### Section 1: Setup & Context (5 slides)
**Goal**: Establish the problem and why these papers matter

- **Slide 1**: Title + Your Hypothesis Statement
- **Slide 2**: The Reasoning Challenge
  - LLMs struggle on ARC-AGI (Gemini 2.5 Pro: 4.9%)
  - Traditional scaling isn't working
  - Need new approaches
- **Slide 3**: Enter HRM (2025)
  - 27M params, brain-inspired
  - Two-level hierarchy (H/L networks)
  - 40% on ARC-AGI-1 with 1000 examples
  - Viral reception (4M+ Twitter views)
- **Slide 4**: The Plot Twist - ARC Prize Analysis
  - Official verification: 32% (not 40%) on hidden test
  - Key finding: Hierarchy barely matters
  - Real driver: Deep supervision (outer loop)
- **Slide 5**: Enter TRM (October 2025)
  - 7M params (1/4 the size)
  - NO hierarchy - single network
  - 45% on ARC-AGI-1 (better than HRM!)
  - "Less is More" - but why?

### Section 2: Methods Deep-Dive (7 slides)
**Goal**: Explain how the models actually work

- **Slide 6**: HRM Architecture
  - Visual diagram: H network (slow) + L network (fast)
  - Mathematical formulation
  - Key components: Input embedding, recursion, output head
- **Slide 7**: HRM's Two Key Ideas
  - **Idea 1**: Hierarchical recursion (at different frequencies)
  - **Idea 2**: Deep supervision (outer loop refinement)
  - Which one matters more?
- **Slide 8**: TRM's Simplification
  - Visual comparison: HRM vs TRM
  - Removed: Hierarchy, multiple networks, biological justification
  - Kept: Deep supervision, adaptive halting, iterative refinement
- **Slide 9**: The Outer Loop (Deep Supervision)
  - Predict → Evaluate → Refine (repeat)
  - Carries latent state forward (detached gradients)
  - Like ResNet but through time
  - Adaptive halting: "am I done yet?"
- **Slide 10**: The Secret Sauce - Training Dynamics
  - Training WITH refinement improves single-pass inference
  - 19% → 39% (just from outer loop)
  - vs 35.7% → 39% (adding hierarchy)
  - Refinement at training time > refinement at inference time
- **Slide 11**: Data Augmentation Strategy
  - Rotate, flip, recolor tasks
  - Creates task-specific feature space
  - HRM: 1000 augments, TRM: better with same
  - Critical finding: Only 300 needed for peak performance
- **Slide 12**: The Puzzle_ID Problem
  - Models use task-specific embeddings
  - Can ONLY work on tasks seen during training
  - Not few-shot learners - they're memorizers
  - Fundamental limitation

### Section 3: Critical Analysis (6 slides)
**Goal**: Present your hypothesis with evidence

- **Slide 13**: Your Hypothesis Statement
  - "Iterative Refinement is All You Need - Architecture is Noise"
  - Bold claim supported by convergent evidence
- **Slide 14**: Evidence #1 - The Ablation Data
  - ARC Prize findings table
  - Outer loop: 2x improvement
  - Hierarchy: 9.2% improvement
  - 6x more impact from refinement
- **Slide 15**: Evidence #2 - TRM's Success Doesn't Need Hierarchy
  - Removes 2 networks → better performance
  - If hierarchy mattered, this shouldn't work
  - Simpler model = easier to optimize
  - All benefits retained
- **Slide 16**: Evidence #3 - Training vs Inference Refinement
  - Models trained with 4 steps, tested with 1 step
  - Still 15pp better than baseline
  - Refinement teaches the model, not just refines output
  - Changes the learned representation
- **Slide 17**: The Mechanism - Why This Works
  - Hypothesis: Deep supervision = implicit curriculum learning
  - Early steps learn coarse solutions
  - Later steps learn refinements
  - Model learns to predict corrections
  - Like training on multiple difficulty levels simultaneously
- **Slide 18**: Implications & What This Means
  - Architecture search might be overrated
  - Training dynamics underexplored
  - "How you train" > "What you train"
  - Path forward: Focus on optimization, not design

### Section 4: Counter-Arguments & Limitations (3 slides)
**Goal**: Address weaknesses honestly

- **Slide 19**: Alternative Explanations
  - Maybe TRM just has better hyperparameters?
  - Maybe smaller = less overfitting (complexity control)?
  - Maybe the specific architecture still matters (just differently)?
- **Slide 20**: The Memorization Problem
  - Both models might just memorize well
  - Test on hidden set: HRM 32%, claimed 40%
  - Cross-task transfer: Only 10pp drop (31% → 41%)
  - Are they learning rules or patterns?
- **Slide 21**: What We Still Don't Know
  - Would vanilla transformer + deep supervision match TRM?
  - How much does architecture matter (really)?
  - Why does TRM outperform HRM specifically?
  - Can these insights transfer to other domains?

### Section 5: Broader Implications (3 slides)
**Goal**: Connect to bigger picture

- **Slide 22**: For ARC-AGI Specifically
  - Current scores may overstate reasoning ability
  - Need better evaluation protocol
  - Puzzle_ID embeddings are a fundamental problem
  - True test: Completely novel tasks
- **Slide 23**: For AI Research Generally
  - Deep supervision deserves more attention
  - Iterative refinement is powerful but underused
  - Small models + smart training > big models + standard training
  - The "Less is More" insight is real
- **Slide 24**: Open Questions & Future Work
  - Can we remove puzzle_ID dependency?
  - Apply deep supervision to LLMs?
  - What's the theoretical basis for refinement?
  - How to scale to more complex tasks?

### Section 6: Conclusion (1 slide)
- **Slide 25**: Key Takeaways
  - TRM shows architecture simplification can improve performance
  - Iterative refinement during training is the real innovation
  - Both models may be sophisticated memorizers, not reasoners
  - Path forward: Focus on training dynamics and generalization tests
  - **Your hypothesis**: The architecture debate is a distraction

---

## Interactive Web Features

### Core Functionality
1. **Visual Architecture Comparison**
   - Interactive SVG diagrams
   - Toggle between HRM and TRM
   - Animated forward pass
   - Highlight differences

2. **Live Refinement Visualization**
   - Show iterative refinement steps
   - Display intermediate predictions
   - Visualize latent space evolution
   - Before/after comparisons

3. **Data Exploration Dashboard**
   - Performance vs parameters scatter plot
   - Ablation results interactive table
   - Augmentation count vs accuracy
   - Training vs inference refinement impact

4. **ARC-AGI Task Examples**
   - Embed 3-5 example tasks
   - Show input → output transformations
   - Display model predictions
   - Highlight successes and failures

5. **Hypothesis Testing Tool**
   - Present your 3 hypotheses
   - Let viewers vote
   - Show supporting evidence for each
   - Interactive argument map

### Technical Implementation

**Framework**: React + D3.js or Svelte + D3.js
- Svelte might be lighter and faster for this use case
- D3.js for complex visualizations

**Structure**:
```
presentation/
├── public/
│   ├── data/
│   │   ├── arc_prize_ablations.json
│   │   ├── performance_data.json
│   │   └── example_tasks.json
│   └── assets/
│       ├── trm_diagram.svg
│       └── hrm_diagram.svg
├── src/
│   ├── components/
│   │   ├── Slide.svelte
│   │   ├── ArchitectureDiagram.svelte
│   │   ├── PerformanceChart.svelte
│   │   ├── RefinementVisualizer.svelte
│   │   └── HypothesisPoll.svelte
│   ├── stores/
│   │   └── presentation.js
│   ├── slides/
│   │   ├── 01-intro.svelte
│   │   ├── 02-context.svelte
│   │   └── ...
│   └── App.svelte
├── package.json
└── vite.config.js
```

**Key Libraries**:
- Svelte (or React)
- D3.js (visualizations)
- Reveal.js (presentation framework)
- Prism.js (code highlighting)
- KaTeX (math rendering)

---

## Data Preparation

### Files to Create

1. **`arc_prize_data.json`**
```json
{
  "ablations": {
    "baseline": {"accuracy": 0.357, "description": "Single forward pass"},
    "with_hierarchy": {"accuracy": 0.390, "description": "+2 networks"},
    "deep_supervision": {"accuracy": 0.390, "description": "Outer loop only"},
    "both": {"accuracy": 0.410, "description": "Full HRM"}
  },
  "refinement_impact": {
    "train_1_test_1": 0.19,
    "train_4_test_1": 0.35,
    "train_4_test_4": 0.39
  }
}
```

2. **`model_comparison.json`**
```json
{
  "models": [
    {"name": "TRM", "params": 7, "arc1": 0.45, "arc2": 0.08, "sudoku": 0.87},
    {"name": "HRM", "params": 27, "arc1": 0.40, "arc2": 0.05, "sudoku": 0.55},
    {"name": "Gemini 2.5", "params": "unknown", "arc1": "N/A", "arc2": 0.049}
  ]
}
```

3. **`augmentation_study.json`**
- Data from Figure 7 of ARC Prize blog
- Augmentation count vs performance

---

## Development Timeline

### Phase 1: Data Preparation (2 hours)
- Extract key data from papers
- Create JSON data files
- Prepare ARC-AGI example tasks
- Collect images/diagrams

### Phase 2: Core Infrastructure (3 hours)
- Set up Svelte + Vite project
- Implement slide navigation
- Create reusable components
- Set up D3.js integration

### Phase 3: Content Development (5 hours)
- Build all 25 slides
- Implement visualizations
- Add interactive elements
- Write narrative text

### Phase 4: Polish & Testing (2 hours)
- Responsive design
- Transitions and animations
- Cross-browser testing
- Performance optimization

**Total Estimated Time**: 12 hours

---

## Success Metrics

1. **Clarity**: Audience understands the key difference (refinement vs architecture)
2. **Engagement**: Interactive elements get used
3. **Persuasiveness**: Hypothesis is compelling (even if not everyone agrees)
4. **Depth**: Technical details are accurate and insightful
5. **Novelty**: Brings new perspective beyond the papers themselves

---

## Next Steps

1. **Choose your hypothesis** (recommend #2)
2. **Review and approve this plan**
3. **Gather additional data** if needed
4. **Begin implementation**

Would you like me to proceed with building this presentation based on Hypothesis #2?

