# Data Corrections for Ablation Study

## Source Verification

### From TRM Paper (less_is_more_extracted.txt, lines 99-109):

> "An independent analysis on the ARC-AGI benchmark showed that deep supervision seems to be the primary driver of the performance gains (ARC Prize Foundation, 2025a). **Using deep supervision doubled accuracy over single-step supervision (going from 19% to 39% accuracy)**, while **recursive hierarchical reasoning only slightly improved accuracy over a regular model with a single forward pass (going from 35.7% to 39.0% accuracy)**."

## The Two Separate Ablations

### Ablation 1: Deep Supervision (Outer Loop)
- **Without deep supervision** (single-step): **19%**
- **With deep supervision** (outer loop): **39%**
- **Improvement**: +20pp (105% relative increase, 2.05x multiplier)

### Ablation 2: Hierarchical Architecture  
- **Without hierarchy** (single transformer): **35.7%**
- **With hierarchy** (H/L networks): **39%**
- **Improvement**: +3.3pp (9.2% relative increase)

## Corrected JSON Structure

```json
{
  "title": "ARC Prize HRM Ablation Study Results",
  "source": "ARC Prize Foundation (2025) as cited in Jolicoeur-Martineau 2025",
  "url": "https://arcprize.org/blog/hrm-analysis",
  "note": "These are two separate ablation studies, not cumulative effects",
  
  "ablation_1_deep_supervision": {
    "name": "Deep Supervision Impact",
    "description": "Effect of adding outer loop refinement",
    "experiments": [
      {
        "condition": "Without Deep Supervision",
        "accuracy": 0.19,
        "description": "Single-step supervision",
        "color": "#94a3b8"
      },
      {
        "condition": "With Deep Supervision",
        "accuracy": 0.39,
        "description": "Outer loop refinement (up to 16 steps)",
        "color": "#10b981"
      }
    ],
    "improvement": 0.20,
    "improvement_percentage": 105.3,
    "multiplier": 2.05,
    "key_insight": "Deep supervision DOUBLES performance"
  },
  
  "ablation_2_hierarchy": {
    "name": "Hierarchical Architecture Impact", 
    "description": "Effect of adding H/L network hierarchy",
    "experiments": [
      {
        "condition": "Without Hierarchy",
        "accuracy": 0.357,
        "description": "Single transformer with forward pass",
        "color": "#94a3b8"
      },
      {
        "condition": "With Hierarchy", 
        "accuracy": 0.39,
        "description": "H-network + L-network recursion",
        "color": "#3b82f6"
      }
    ],
    "improvement": 0.033,
    "improvement_percentage": 9.2,
    "key_insight": "Hierarchy adds minimal value (only 9% improvement)"
  },
  
  "comparison": {
    "deep_supervision_effect": "+20pp (2x improvement)",
    "hierarchy_effect": "+3.3pp (9% improvement)", 
    "ratio": "Deep supervision is ~6x more impactful than hierarchy"
  }
}
```

## For Visualization

For the bar chart on Slide 6, use this simpler structure:

```json
{
  "experiments": [
    {
      "name": "Baseline\n(No Deep Supervision)",
      "accuracy": 0.19,
      "label": "19%",
      "color": "#94a3b8"
    },
    {
      "name": "Baseline\n(No Hierarchy)",
      "accuracy": 0.357,
      "label": "35.7%",
      "color": "#94a3b8"
    },
    {
      "name": "+ Deep Supervision",
      "accuracy": 0.39,
      "label": "39% (+20pp)",
      "color": "#10b981",
      "highlight": true
    },
    {
      "name": "+ Hierarchy",
      "accuracy": 0.39,
      "label": "39% (+3.3pp)",
      "color": "#3b82f6"
    }
  ]
}
```

## Training vs Inference Numbers

From the TRM paper discussion (verified):

```
Train with 1 step, Test with 1 step:  19%
Train with 4 steps, Test with 1 step:  35% (improvement: +16pp)
Train with 4 steps, Test with 4 steps: 39% (improvement: +4pp more)
```

Note: The TRM paper says "+15pp" in one place and we calculated +16pp (35-19=16). Use **+16pp** as it's the accurate math.

## Model Comparison Numbers  

All verified from papers:

| Model | Parameters | ARC-AGI-1 | Source |
|-------|-----------|-----------|--------|
| HRM (claimed) | 27M | 40% | HRM paper |
| HRM (verified) | 27M | **32%** | ARC Prize verification |
| TRM (claimed) | 7M | **45%** | TRM paper |
| TRM (verified) | 7M | Not yet verified | - |

## Summary of Errors in Original JSON

1. **Mixed two separate ablations** as if they were cumulative
2. **Created confusing "Hierarchy (H/L Networks)" entry** at 35.7% - this was the BASELINE for the hierarchy comparison
3. **Improvement percentages were wrong** - calculated from wrong baselines
4. **Structure didn't make it clear** these were separate experiments

## Recommendation

Use the **"For Visualization"** structure above in the IMPLEMENTATION_GUIDE.md. It's clearer and accurately represents the two separate ablations side-by-side.

