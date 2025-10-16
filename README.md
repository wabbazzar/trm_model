# TRM Research Repository

Research and analysis of **"Less is More: Recursive Reasoning with Tiny Networks"** (Jolicoeur-Martineau, 2025) and its predecessor **Hierarchical Reasoning Model (HRM)** (Wang et al., 2025).

## 📚 Contents

This repository contains:

1. **Paper Analysis**: Extracted texts and comparative analysis
2. **Interactive Presentation**: Web-based presentation of research findings
3. **TRM Model Code**: Original implementation from Samsung SAIL Montreal (submodule)

## 🎯 Key Hypothesis

**"Iterative Refinement is All You Need"**

We argue that the success of both HRM and TRM comes not from their architectures, but from how they train—through iterative refinement with deep supervision. The hierarchical vs. flat architecture debate is secondary to training dynamics.

## 📊 Repository Structure

```
trm_model/
├── presentation/              # Interactive web presentation (Svelte + D3.js)
│   ├── src/                  # Source code
│   ├── public/               # Static assets and data
│   └── README.md             # Presentation documentation
├── docs/
│   ├── papers/               # Extracted paper texts
│   │   ├── less_is_more_extracted.txt
│   │   └── hierarchical_reasoning_model_extracted.txt
│   └── tickets/
│       ├── HYPOTHESIS_SUMMARY.md
│       ├── presentation_plan_final.md
│       └── IMPLEMENTATION_GUIDE.md
├── TinyRecursiveModels/      # Original TRM implementation (cloned)
└── README.md                 # This file
```

## 🚀 Quick Start

### View the Presentation

```bash
cd presentation
npm install
npm run dev
```

Open http://localhost:3000

### Navigation
- **Arrow Keys**: Navigate slides
- **Space**: Next slide
- **1-9**: Jump to slide

## 📖 Presentation Outline (12 Slides)

1. **Title + Thesis**: Introduction and main hypothesis
2. **ARC-AGI Challenge**: Why these papers matter
3. **HRM Architecture**: Kahneman's "Thinking, Fast and Slow" in neural networks
4. **TRM Simplification**: Removing hierarchy improves performance
5. **Deep Supervision**: The hidden variable
6. **ARC Prize Revelation**: Ablation study results
7. **Training vs Inference**: Where the magic happens
8. **TRM Proves the Point**: Empirical validation
9. **Our Hypothesis**: Iterative refinement is all you need
10. **Broader Implications**: What this means for AI research
11. **Provocative Alternative**: Is ARC-AGI just a memory test?
12. **Conclusion**: The Kahneman irony

## 🔬 Key Findings

### From ARC Prize Analysis (2025)
- **Deep supervision (outer loop)**: 2x improvement (19% → 39%)
- **Hierarchy (H/L networks)**: 9% improvement (35.7% → 39%)
- **Training with refinement**: Improves single-pass inference by 16pp
- **Cross-task transfer**: Limited (90% performance from task-specific training)

### Model Comparison
| Model | Parameters | ARC-AGI-1 | ARC-AGI-2 |
|-------|-----------|-----------|-----------|
| **HRM** | 27M | 32% (verified) | 2% |
| **TRM** | 7M | 45% (claimed) | 8% |
| Gemini 2.5 Pro | Unknown | N/A | 4.9% |
| o3-mini | Unknown | 21% | 3% |

## 📝 Papers Analyzed

### Primary Paper
**Less is More: Recursive Reasoning with Tiny Networks**
- Author: Alexia Jolicoeur-Martineau (Samsung SAIL Montreal)
- Published: October 2025
- arXiv: 2510.04871

### Parent Paper
**Hierarchical Reasoning Model**
- Authors: Wang et al. (Sapient Intelligence)
- Published: June 2025
- arXiv: 2506.21734

### Critical Analysis
**The Hidden Drivers of HRM's Performance on ARC-AGI**
- Source: ARC Prize Foundation
- URL: https://arcprize.org/blog/hrm-analysis
- Date: August 2025

## 🎓 Research Questions

1. **Does architecture matter?** Our analysis suggests training dynamics matter more
2. **What is "reasoning"?** Are these models reasoning or memorizing?
3. **Can this generalize?** Will insights transfer beyond puzzle tasks?
4. **What about LLMs?** Can deep supervision improve language models?

## 🛠️ Technical Stack

### Presentation
- **Framework**: Svelte 4
- **Build**: Vite
- **Styling**: Tailwind CSS
- **Visualization**: D3.js
- **Math**: KaTeX
- **Code**: Prism.js

### Model (Original)
- **Framework**: PyTorch
- **Size**: 7M parameters (TRM) / 27M (HRM)
- **Architecture**: 2-layer transformer (TRM)
- **Training**: Deep supervision with adaptive halting

## 📄 License

This research repository: MIT License

Original TRM code: See TinyRecursiveModels/LICENSE

## 🙏 Acknowledgments

- Alexia Jolicoeur-Martineau for TRM paper and code
- Wang et al. for HRM paper
- ARC Prize Foundation for critical analysis
- Daniel Kahneman for the conceptual framework

## 📧 Contact

For questions about this analysis: [Your contact info]

For questions about TRM: research@samsung.com (Samsung SAIL Montreal)

## 🔗 Links

- [TRM Paper](https://arxiv.org/abs/2510.04871)
- [HRM Paper](https://arxiv.org/abs/2506.21734)
- [ARC Prize Analysis](https://arcprize.org/blog/hrm-analysis)
- [TRM Code](https://github.com/SamsungSAILMontreal/TinyRecursiveModels)

---

**Last Updated**: October 2025
