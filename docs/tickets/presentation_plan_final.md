# Web Presentation: "Iterative Refinement is All You Need"
## TRM Paper Analysis - 12 Slide Structure

---

## Presentation Overview

**Core Thesis**: Architecture (hierarchy vs flat) is a distraction—what drives performance is iterative refinement during training, not architectural complexity during inference.

**Kahneman Integration**: Use "Thinking, Fast and Slow" as the narrative thread connecting biological inspiration to practical reality.

**Total Slides**: 12 (10 main + 1 provocative ending + 1 conclusion)

---

## Slide Structure

### **Slide 1: Title + Thesis**
**"Less is More? Or Just Different?"**

**Content**:
- Title: Analyzing TRM - What Really Drives Performance
- Subtitle: When iterative refinement beats architectural complexity
- Your name & date
- **Thesis Statement**: "The success of both HRM and TRM comes not from their architectures, but from how they train—through iterative refinement with deep supervision."

**Visual**: Side-by-side comparison
- Left: HRM (27M params, complex hierarchy) → 32% verified
- Right: TRM (7M params, simple 2-layer) → 45% claimed

**Kahneman Teaser**: "Both papers invoke Kahneman's 'Thinking, Fast and Slow'—but is this the right analogy?"

---

### **Slide 2: The ARC-AGI Challenge**
**"Why These Papers Matter"**

**Content**:
- ARC-AGI tests abstract reasoning (not knowledge)
- LLMs struggle despite massive scale:
  - Gemini 2.5 Pro: 4.9% on ARC-AGI-2
  - o3-mini: 21% on ARC-AGI-1
  - Deepseek R1: 15.8% on ARC-AGI-1
- Need: Different approaches beyond scaling

**Visual**: 
- Example ARC-AGI task (3x3 grid transformation)
- Bar chart: LLMs vs HRM vs TRM

**Key Point**: "Something fundamentally different is needed"

---

### **Slide 3: Enter HRM - The Biological Inspiration**
**"Thinking, Fast and Slow... in Neural Networks?"**

**Content**:
- **HRM's Core Idea** (Wang et al., 2025):
  - Two networks at different "timescales"
  - H-network (slow, abstract planning) ← System 2
  - L-network (fast, detailed execution) ← System 1
  - Recursive interaction between them
  
**Kahneman Connection**:
```
Brain's System 1: Fast, automatic, intuitive
Brain's System 2: Slow, deliberate, analytical

HRM's L-network: Operates at high frequency (fast)
HRM's H-network: Operates at low frequency (slow)
```

**Visual**: 
- Diagram of HRM architecture
- Kahneman's two systems mapped to H/L networks
- Mathematical formulation showing recursion

**Quote from HRM Paper**: 
> "Inspired by hierarchical and multi-timescale processing in the human brain... the brain dynamically modulates the 'runtime' of circuits according to task complexity" (p. 7)

**Result**: 40% on ARC-AGI-1 (claimed), 32% verified

---

### **Slide 4: TRM Simplifies - No Hierarchy Needed**
**"What if System 1/System 2 is the wrong analogy?"**

**Content**:
- **TRM's Approach** (Jolicoeur-Martineau, 2025):
  - Single network (no H/L separation)
  - Just 2 layers
  - 7M parameters (vs HRM's 27M)
  - Still uses iteration—but differently

**The Paradox**:
- Removes the "fast/slow" hierarchy
- Gets BETTER performance (45% claimed)
- 4x fewer parameters

**Visual**:
- TRM architecture diagram
- Side-by-side: HRM (complex) vs TRM (simple)
- Performance comparison chart

**Key Question**: "If the biological inspiration matters, why does removing it improve performance?"

---

### **Slide 5: The Hidden Variable - Deep Supervision**
**"The Outer Loop Nobody Talks About"**

**Content**:
Both models share a secret weapon that has nothing to do with hierarchy:

**Deep Supervision (The Outer Loop)**:
```python
for step in range(16):  # Up to 16 refinement steps
    prediction = model(input, current_answer, latent_state)
    
    if good_enough(prediction):
        break  # Adaptive halting
    
    current_answer = prediction  # Refine
    latent_state = latent_state.detach()  # Carry forward
```

**What This Does**:
- Predicts answer
- Evaluates quality
- Refines if needed
- Repeats up to 16 times
- **Crucially**: Trains with this loop, not just infers with it

**Visual**:
- Flow diagram of refinement loop
- Animation concept: Show answer improving over iterations
- Code snippet

**Kahneman Reframe**: "Maybe the real 'System 2' isn't the architecture—it's the iterative refinement process itself"

---

### **Slide 6: The ARC Prize Revelation**
**"Official Verification Changes Everything"**

**Content**:
ARC Prize Foundation (2025) ran controlled ablations on HRM:

**Key Findings**:

| Component | Accuracy | Improvement |
|-----------|----------|-------------|
| Baseline (single pass) | 19% | - |
| + Hierarchy (H/L) | 35.7% → 39% | **+3.3pp (9%)** |
| + Deep Supervision (outer loop) | 19% → 39% | **+20pp (105%)** |

**The Smoking Gun**:
- Outer loop: 2x improvement
- Hierarchy: Marginal improvement
- "The hierarchical architecture had minimal performance impact"

**Visual**:
- Bar chart showing relative contributions
- Highlight the massive outer loop effect
- Small hierarchy effect

**Critical Quote**: 
> "Deep supervision seems to be the primary driver of the performance gains... while recursive hierarchical reasoning only slightly improved accuracy" (ARC Prize, 2025)

---

### **Slide 7: Training vs Inference - The Real Magic**
**"How You Train Matters More Than How You Infer"**

**Content**:
**Experiment**: Train with different refinement steps, test with different steps

**Results**:
```
Train with 1 step, Test with 1 step:  19% accuracy
Train with 4 steps, Test with 1 step:  35% accuracy  (+16pp!)
Train with 4 steps, Test with 4 steps: 39% accuracy  (+4pp more)
```

**The Insight**:
- Training with refinement improves SINGLE-PASS inference by 16pp
- Actual refinement at inference only adds 4pp more
- **The model learns to self-correct, not just corrects at runtime**

**Visual**:
- Matrix heatmap: Training steps (rows) × Inference steps (cols) → Accuracy (color)
- Highlight the key finding: Training impact > Inference impact

**Mechanism Hypothesis**:
Deep supervision = implicit curriculum learning
- Early steps: Learn coarse solutions
- Later steps: Learn refinements
- Model learns to predict corrections
- Not just refining outputs—changing representations

---

### **Slide 8: TRM Proves the Point**
**"Remove Complexity, Keep Performance"**

**Content**:
**TRM's Simplification Strategy**:

What HRM has:
- ✅ Deep supervision (outer loop)
- ✅ Adaptive halting (ACT)
- ✅ Iterative refinement
- ✅ Two networks (H and L)
- ✅ Hierarchical recursion

What TRM keeps:
- ✅ Deep supervision (outer loop)
- ✅ Adaptive halting (ACT)
- ✅ Iterative refinement
- ❌ Just ONE network
- ❌ No hierarchy

**Result**: Better performance (45% vs 40%)

**Visual**:
- Venn diagram showing shared vs unique components
- Arrow showing: Remove hierarchy → Performance improves
- Table: Model size, architecture, performance

**The Proof**:
If hierarchy was essential, removing it should hurt.
Instead, it helps.
Therefore: Hierarchy is not the driver.

---

### **Slide 9: Our Hypothesis**
**"Iterative Refinement is All You Need"**

**Content**:

**The Claim**:
The entire architecture debate (hierarchy vs flat, H/L networks vs single network) is a distraction. What actually drives performance is:

1. **Deep supervision** during training
2. **Iterative refinement** at both train and inference time  
3. **Adaptive halting** to know when to stop
4. Architecture is secondary

**Supporting Evidence**:
- ✅ ARC Prize ablations: 2x from outer loop, 9% from hierarchy
- ✅ TRM's simplification: Remove hierarchy → improve performance
- ✅ Training dynamics: Train with refinement helps single-pass inference
- ✅ Both models share deep supervision, differ in architecture

**Testable Predictions**:
1. Vanilla 2-layer Transformer + deep supervision → ~40% on ARC-AGI
2. Remove deep supervision from TRM → collapse to ~20%
3. Apply deep supervision to CNN/RNN → see similar 2x improvement
4. Architecture choice has <10% impact vs refinement strategy

**Visual**:
- Central diagram: Deep supervision as the core
- Peripheral: Different architectures as interchangeable wrappers
- Formula: Performance = f(training_strategy) >> f(architecture)

**Kahneman Revisited**: 
"The real 'System 2' thinking isn't in the neural architecture—it's in the training loop that teaches models to think iteratively"

---

### **Slide 10: Broader Implications**
**"What This Means for AI Research"**

**Content**:

**For ARC-AGI Research**:
- Focus on training dynamics, not architecture search
- Deep supervision should be standard baseline
- Architecture ablations may be misleading without it

**For Deep Learning Generally**:
- "How you train" > "What you train"
- Iterative refinement is underexplored
- Small models + smart training > big models + standard training

**For Neural Architecture Search**:
- May be optimizing the wrong dimension
- Training protocol should be the search space
- Architecture might be less important than we think

**Open Questions**:
- What's the theoretical basis for why deep supervision works?
- Can we apply this to LLMs? (Chain-of-Thought during training?)
- What's the optimal number of refinement steps?
- Does this generalize beyond puzzle tasks?

**Visual**:
- Mind map: Central insight radiating to different domains
- "Future Work" roadmap

---

### **Slide 11: The Provocative Alternative**
**"Or... Is ARC-AGI Just a Memory Test?"**

**Content**:
**Hypothesis #3**: Maybe both models are sophisticated memorizers, not reasoners

**The Uncomfortable Evidence**:

1. **Training on Evaluation Tasks**:
   - HRM trained on 400 eval tasks + 400 training tasks
   - Trained on ONLY eval tasks: 31% (vs 41% with all data)
   - Only 10pp drop = 90% of performance from "memorizing" eval tasks

2. **The Puzzle_ID Smoking Gun**:
   - Both models use task-specific embeddings (`puzzle_id`)
   - Can ONLY predict on tasks with seen `puzzle_id`s
   - Not few-shot learners—zero-shot on memorized patterns
   - Literally cannot work on novel task IDs

3. **Augmentation Dependency**:
   - 1000 augmentations per task
   - 300 augmentations achieves 95% of max performance
   - Building rich per-task feature spaces
   - Memorizing transformations, not learning rules?

4. **Verification Drop**:
   - HRM claimed: 40% → Verified: 32% (-8pp)
   - TRM claimed: 45% → Verified: ???
   - Similar drop → ~36% (still good, but less impressive)

**The Provocative Question**:
"Are these models learning abstract reasoning, or just building very sophisticated lookup tables?"

**Visual**:
- Flow diagram: Training data → Puzzle_ID embedding → Task-specific features → Prediction
- Highlight the data leakage loop
- Warning symbol on "Generalization?"

**Counter-argument**:
- 31% on cross-task transfer > 0% (some generalization happening)
- Maybe this IS how abstraction works (compositional features)
- "Memorization" vs "learning" is philosophical

**The Test**:
True validation requires completely novel tasks with unseen puzzle_ids. Until then, we can't be sure.

---

### **Slide 12: Conclusion**
**"Less is More, But Why?"**

**Content**:

**What We Know**:
1. ✅ TRM beats HRM despite being simpler (45% vs 32% verified)
2. ✅ Deep supervision drives 2x improvement (empirically proven)
3. ✅ Hierarchy contributes minimally (9% improvement)
4. ✅ Training with refinement > inference with refinement

**What We Believe** (Hypothesis #2):
- Architecture is overrated
- Training dynamics is underexplored  
- Iterative refinement during training is the key innovation
- "Less is more" because simplicity aids optimization

**What We Question** (Hypothesis #3):
- Are these models really reasoning?
- Or sophisticated memorization?
- Need better evaluation protocols
- True test: Completely novel tasks

**The Kahneman Irony**:
Both papers invoke "Thinking, Fast and Slow" as biological inspiration. But the real "System 2" thinking might not be in the architecture at all—it's in the meta-level training process that teaches models to iteratively refine their thinking.

**Key Takeaway**:
> "The next breakthrough won't come from better architectures—it will come from better training strategies."

**Call to Action**:
- Test vanilla architectures + deep supervision
- Explore other refinement strategies
- Develop better generalization benchmarks
- Focus on how we optimize, not what we optimize

**Final Visual**:
- Simple diagram: Training Strategy (large circle) ⊃ Architecture (small circle)
- "Focus here" arrow pointing to training strategy

---

## Technical Implementation Plan

### Technology Stack
- **Framework**: Svelte (lighter than React for this use case)
- **Visualization**: D3.js + Chart.js
- **Presentation**: Reveal.js integration
- **Math**: KaTeX
- **Code**: Prism.js
- **Animations**: Svelte transitions + CSS animations

### Key Interactive Features

1. **Architecture Comparison Tool** (Slides 3-4)
   - Toggle between HRM and TRM diagrams
   - Animated forward pass
   - Parameter count comparison

2. **Ablation Study Visualizer** (Slide 6)
   - Interactive bar chart
   - Click to see detailed breakdowns
   - Animate the 2x vs 9% comparison

3. **Training vs Inference Matrix** (Slide 7)
   - Interactive heatmap
   - Hover for exact values
   - Highlight key findings

4. **Refinement Loop Animation** (Slide 5)
   - Step-by-step visualization
   - Show answer improving
   - Adaptive halting demonstration

5. **Hypothesis Comparison** (Slide 9)
   - Side-by-side evidence
   - Collapsible sections
   - Interactive predictions checklist

6. **Puzzle_ID Flow Diagram** (Slide 11)
   - Trace data flow
   - Highlight the embedding dependency
   - Show task-specific nature

### Data Files to Create

```
presentation/data/
├── arc_prize_ablations.json      # Slide 6 data
├── training_inference_matrix.json # Slide 7 data
├── model_comparison.json          # Slides 1, 4, 8
├── augmentation_study.json        # Slide 11 data
└── example_tasks.json             # Background examples
```

### Project Structure

```
presentation/
├── public/
│   ├── data/
│   └── assets/
│       ├── hrm_architecture.svg
│       ├── trm_architecture.svg
│       └── kahneman_diagram.svg
├── src/
│   ├── slides/
│   │   ├── Slide01_Title.svelte
│   │   ├── Slide02_Challenge.svelte
│   │   └── ... (through Slide12)
│   ├── components/
│   │   ├── ArchitectureDiagram.svelte
│   │   ├── AblationChart.svelte
│   │   ├── RefinementAnimation.svelte
│   │   └── MatrixHeatmap.svelte
│   ├── stores/
│   │   └── presentation.js
│   └── App.svelte
├── package.json
└── vite.config.js
```

### Development Timeline

**Phase 1: Data & Assets** (2 hours)
- Extract data from papers and ARC Prize blog
- Create JSON files
- Design SVG diagrams for architectures

**Phase 2: Core Slides** (4 hours)
- Build static content for all 12 slides
- Implement slide navigation
- Add KaTeX math rendering

**Phase 3: Interactive Components** (4 hours)
- Architecture comparison tool
- Ablation study chart
- Training/inference heatmap
- Refinement animation

**Phase 4: Polish** (2 hours)
- Transitions and animations
- Responsive design
- Cross-browser testing
- Performance optimization

**Total**: 12 hours

---

## Key Narrative Beats

1. **Hook**: "Less is more" - but what does that really mean?
2. **Setup**: ARC-AGI is hard, LLMs fail, need new approaches
3. **Act 1**: HRM uses biological inspiration (Kahneman's systems)
4. **Twist**: TRM removes biology, gets better results
5. **Investigation**: What's really driving performance?
6. **Revelation**: ARC Prize shows outer loop is the secret
7. **Proof**: Training dynamics matter more than architecture
8. **Hypothesis**: Iterative refinement is all you need
9. **Doubt**: Or is it all just memorization?
10. **Resolution**: Focus on training, question evaluation
11. **Lesson**: The Kahneman analogy misled us
12. **Call to action**: Change how we do research

---

## Backup Slides (Optional)

If you have extra time or Q&A, prepare these:

**B1: Mathematical Details**
- Formal definition of deep supervision
- ACT (Adaptive Computation Time) mathematics
- Gradient flow analysis

**B2: Other Tasks**
- Sudoku: HRM 55% → TRM 87%
- Maze: HRM 75% → TRM 85%
- Generalization beyond ARC-AGI

**B3: Detailed Ablations**
- Full ARC Prize experimental setup
- Statistical significance
- Augmentation count analysis (Figure 7)

**B4: Future Experiments**
- Proposed tests for Hypothesis #2
- How to test Hypothesis #3
- Research roadmap

---

## Presentation Tips

1. **Kahneman Thread**: Mention it on slides 1, 3, 5, 9, and 12 to create continuity
2. **Build Tension**: Slides 1-5 set up the puzzle, 6-9 solve it, 10-11 question it, 12 resolves
3. **Visual Consistency**: Use same color scheme for HRM (blue) and TRM (orange) throughout
4. **Pause Points**: After slides 6, 9, and 11 for audience processing
5. **Backup Evidence**: Have paper quotes ready for Q&A
6. **Time Management**: 
   - Slides 1-2: 2 min
   - Slides 3-5: 6 min (setup)
   - Slides 6-9: 9 min (main argument)
   - Slides 10-12: 3 min (implications)
   - **Total: 20 minutes** (perfect for conference talk)

---

Ready to build when you confirm! 🚀

