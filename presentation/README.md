# TRM Paper Presentation

Interactive web-based presentation analyzing "Less is More: Recursive Reasoning with Tiny Networks"

## Quick Start

```bash
npm install
npm run dev
```

Open http://localhost:3000

## Navigation

- **Arrow Keys**: Navigate between slides
- **Space**: Next slide
- **Number Keys (1-9)**: Jump to specific slide

## Slides

1. **Title + Thesis** - "Less is More? Or Just Different?"
2. **The ARC-AGI Challenge** - Why these papers matter
3. **Enter HRM** - Biological inspiration with Kahneman
4. **TRM Simplifies** - No hierarchy needed
5. **The Hidden Variable** - Deep supervision revealed
6. **The ARC Prize Revelation** - Ablation study results
7. **Training vs Inference** - How you train matters more
8. **TRM Proves the Point** - Remove complexity, keep performance
9. **Our Hypothesis** - Iterative refinement is all you need
10. **Broader Implications** - What this means for AI research
11. **The Provocative Alternative** - Or is it just memorization?
12. **Conclusion** - Less is more, but why?

## Core Thesis

Architecture (hierarchy vs flat) is a distraction—what drives performance is **iterative refinement during training**, not architectural complexity during inference.

## Development

- **Framework**: Svelte + Vite
- **Styling**: Tailwind CSS
- **Charts**: D3.js
- **Data**: JSON files in `public/data/`

## Build for Production

```bash
npm run build
npm run preview
```

## Project Structure

```
presentation/
├── public/
│   ├── data/                   # JSON data files
│   │   ├── arc_prize_ablations.json
│   │   ├── training_inference_matrix.json
│   │   ├── model_comparison.json
│   │   ├── augmentation_study.json
│   │   └── example_arc_task.json
│   └── assets/                 # SVG diagrams
│       ├── hrm_architecture.svg
│       ├── trm_architecture.svg
│       └── kahneman_systems.svg
├── src/
│   ├── slides/                 # 12 slide components
│   ├── components/             # Reusable components
│   │   ├── AblationChart.svelte
│   │   └── CodeBlock.svelte
│   ├── lib/
│   │   └── stores.js           # Svelte stores
│   ├── App.svelte              # Main app
│   ├── main.js                 # Entry point
│   └── app.css                 # Styles
├── package.json
├── vite.config.js
└── tailwind.config.js
```

## Key Features

- **Interactive Charts**: D3.js-powered ablation study visualizations
- **Architecture Diagrams**: SVG diagrams comparing HRM and TRM
- **Kahneman Integration**: Narrative thread connecting biological inspiration to reality
- **Responsive Design**: Works on different screen sizes
- **Keyboard Navigation**: Full keyboard support

## License

MIT

