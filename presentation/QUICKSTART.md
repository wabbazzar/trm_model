# TRM Presentation - Quick Start Guide

## 🎉 Installation Complete!

The presentation has been successfully created with all 12 slides, data files, and interactive components.

## 🚀 Running the Presentation

### Start Development Server

```bash
cd /Users/wesleybeckner/code/trm_model/presentation
npm run dev
```

The presentation will open automatically at `http://localhost:3000`

### Navigation

- **Arrow Right / Space**: Next slide
- **Arrow Left**: Previous slide
- **Number Keys (1-9)**: Jump to specific slide
- **Navigation Bar**: Use buttons at bottom of screen

## 📊 Slide Overview

1. **Title + Thesis** - Introduction and core argument
2. **ARC-AGI Challenge** - Context and problem statement
3. **Enter HRM** - Biological inspiration (Kahneman's Systems 1 & 2)
4. **TRM Simplifies** - The paradox of better performance with less complexity
5. **Hidden Variable** - Deep supervision revealed
6. **ARC Prize Revelation** - Ablation study results (interactive chart)
7. **Training vs Inference** - Key findings on training dynamics
8. **TRM Proves the Point** - Component analysis
9. **Our Hypothesis** - "Iterative Refinement is All You Need"
10. **Broader Implications** - Impact on AI research
11. **Provocative Alternative** - The memorization hypothesis
12. **Conclusion** - Summary and call to action

## 🎨 Features

✅ **12 fully-designed slides** with content from the papers
✅ **Interactive D3.js charts** for ablation studies
✅ **SVG architecture diagrams** (HRM, TRM, Kahneman)
✅ **Responsive design** with Tailwind CSS
✅ **Keyboard navigation** for smooth presenting
✅ **Data-driven visualizations** from verified sources

## 📁 Project Structure

```
presentation/
├── public/
│   ├── data/                   # 5 JSON data files
│   └── assets/                 # 3 SVG diagrams
├── src/
│   ├── slides/                 # 12 slide components
│   ├── components/             # AblationChart, CodeBlock
│   ├── lib/stores.js           # State management
│   ├── App.svelte              # Main app
│   └── main.js                 # Entry point
└── README.md
```

## 🔧 Build for Production

```bash
npm run build
npm run preview
```

## 📝 Key Thesis

**"Iterative Refinement is All You Need"**

Architecture (hierarchy vs flat) is a distraction—what drives performance is iterative refinement during training, not architectural complexity during inference.

## 📚 Based On

- **Primary**: Jolicoeur-Martineau et al. (2025) - "Less is More: Recursive Reasoning with Tiny Networks"
- **Secondary**: Wang et al. (2025) - "Hierarchical Reasoning Model (HRM)"
- **Verification**: ARC Prize Foundation (2025) - Official ablation studies

## 🎯 Presentation Time

Designed for a **20-minute conference talk**:
- Slides 1-2: 2 min (setup)
- Slides 3-5: 6 min (context)
- Slides 6-9: 9 min (main argument)
- Slides 10-12: 3 min (implications)

## ✨ Next Steps

1. Run `npm run dev` to view the presentation
2. Navigate through all 12 slides
3. Test interactive charts on slides 6-7
4. Customize content as needed
5. Present!

---

**All TODOs completed! ✅**

Enjoy your presentation! 🎉

