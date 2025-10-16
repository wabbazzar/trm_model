# Citation System Implementation for TRM Presentation

**Created**: 2025-10-16  
**Status**: Planning  
**Priority**: Medium

---

## Objective

Add interactive citations to the presentation slides that link directly to source materials, enabling viewers to verify claims and explore primary sources.

---

## Strategy: Hybrid Citation System

### Primary Approach
Link to **authoritative online sources** with specific page/section references:
- ArXiv papers (official versions)
- ARC Prize Foundation blog posts
- OpenReview if available

### Secondary Approach
Maintain local reference files for development:
- Keep extracted txt files in `docs/papers/` for finding exact quotes
- Use line numbers internally for tracking during development
- Don't expose txt files to end users

---

## Implementation Plan

### Phase 1: Setup Citation Infrastructure (1 hour)

#### 1.1 Create Citation Data File
**File**: `presentation/public/data/citations.json`

```json
{
  "citations": [
    {
      "id": "trm-2025",
      "authors": "Jolicoeur-Martineau et al.",
      "title": "Less is More: Recursive Reasoning with Tiny Networks",
      "year": 2025,
      "url": "https://arxiv.org/abs/XXXX.XXXXX",
      "type": "paper",
      "local_pdf": "/papers/less_is_more_jolicoeur_martineau.pdf"
    },
    {
      "id": "hrm-2025",
      "authors": "Wang et al.",
      "title": "Hierarchical Reasoning Model",
      "year": 2025,
      "url": "https://arxiv.org/abs/XXXX.XXXXX",
      "type": "paper",
      "local_pdf": "/papers/hierarchical_reasoning_model_wang.pdf"
    },
    {
      "id": "arc-prize-2025",
      "authors": "ARC Prize Foundation",
      "title": "HRM Analysis and Verification",
      "year": 2025,
      "url": "https://arcprize.org/blog/hrm-analysis",
      "type": "blog"
    }
  ],
  "references": [
    {
      "cite_id": "deep-supervision-2x",
      "citation_id": "trm-2025",
      "quote": "Using deep supervision doubled accuracy over single-step supervision (going from 19% to 39% accuracy)",
      "location": "lines 99-109",
      "page": "N/A",
      "section": "Ablation Studies",
      "slide": 6,
      "context": "ARC Prize ablation results showing deep supervision impact"
    },
    {
      "cite_id": "hierarchy-minimal",
      "citation_id": "trm-2025",
      "quote": "recursive hierarchical reasoning only slightly improved accuracy over a regular model with a single forward pass (going from 35.7% to 39.0% accuracy)",
      "location": "lines 106-107",
      "page": "N/A",
      "section": "Ablation Studies",
      "slide": 6,
      "context": "ARC Prize ablation results showing hierarchy has minimal impact"
    },
    {
      "cite_id": "kahneman-inspiration",
      "citation_id": "hrm-2025",
      "quote": "Inspired by hierarchical and multi-timescale processing in the human brain... the brain dynamically modulates the 'runtime' of circuits according to task complexity",
      "location": "page 7",
      "page": 7,
      "section": "Introduction",
      "slide": 3,
      "context": "HRM's biological inspiration from Kahneman"
    }
  ]
}
```

#### 1.2 Create Citation Component
**File**: `presentation/src/components/Citation.svelte`

```svelte
<script>
  export let citeId = '';
  export let inline = false;
  
  let reference = null;
  let citation = null;
  let showPopup = false;
  
  import { onMount } from 'svelte';
  
  onMount(async () => {
    const response = await fetch('/data/citations.json');
    const data = await response.json();
    reference = data.references.find(r => r.cite_id === citeId);
    if (reference) {
      citation = data.citations.find(c => c.id === reference.citation_id);
    }
  });
  
  function togglePopup() {
    showPopup = !showPopup;
  }
</script>

{#if reference && citation}
  {#if inline}
    <sup class="citation-inline">
      <button on:click={togglePopup} class="citation-button">
        [{reference.citation_id}]
      </button>
    </sup>
  {:else}
    <div class="citation-block">
      <button on:click={togglePopup} class="citation-link">
        📚 {citation.authors} ({citation.year})
      </button>
    </div>
  {/if}
  
  {#if showPopup}
    <div class="citation-popup">
      <div class="citation-popup-content">
        <button class="close-btn" on:click={togglePopup}>✕</button>
        <h4>{citation.title}</h4>
        <p class="authors">{citation.authors} ({citation.year})</p>
        
        {#if reference.quote}
          <blockquote>"{reference.quote}"</blockquote>
        {/if}
        
        <div class="location">
          {#if reference.page !== 'N/A'}
            <p>📄 Page {reference.page}</p>
          {/if}
          {#if reference.section}
            <p>📑 Section: {reference.section}</p>
          {/if}
        </div>
        
        <div class="links">
          <a href={citation.url} target="_blank" rel="noopener noreferrer">
            View Source →
          </a>
          {#if citation.local_pdf}
            <a href={citation.local_pdf} target="_blank">
              View Local PDF →
            </a>
          {/if}
        </div>
      </div>
    </div>
  {/if}
{/if}

<style>
  .citation-button {
    background: none;
    border: none;
    color: #3b82f6;
    cursor: pointer;
    font-size: 0.8em;
    padding: 0;
    text-decoration: none;
  }
  
  .citation-button:hover {
    text-decoration: underline;
  }
  
  .citation-popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }
  
  .citation-popup-content {
    background: white;
    padding: 2rem;
    border-radius: 0.5rem;
    max-width: 600px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
    color: #1e293b;
  }
  
  .close-btn {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    color: #64748b;
  }
  
  blockquote {
    border-left: 4px solid #3b82f6;
    padding-left: 1rem;
    margin: 1rem 0;
    font-style: italic;
    color: #475569;
  }
  
  .links {
    margin-top: 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .links a {
    color: #3b82f6;
    text-decoration: none;
  }
  
  .links a:hover {
    text-decoration: underline;
  }
</style>
```

---

### Phase 2: Map Citations to Slides (2-3 hours)

Go through each slide and identify claims that need citations:

#### Slide 1: Title + Thesis
- [ ] Thesis statement (general claim, no citation needed)
- [ ] Model parameter counts (cite both papers)
- [ ] Verification numbers (cite ARC Prize)

#### Slide 2: ARC-AGI Challenge
- [ ] LLM performance numbers (cite TRM paper references)
- [ ] Gemini 2.5 Pro: 4.9% (cite TRM paper line 70)

#### Slide 3: Enter HRM
- [x] Kahneman quote (cite HRM paper page 7)
- [ ] 40% claimed, 32% verified (cite HRM paper + ARC Prize)

#### Slide 4: TRM Simplifies
- [ ] Parameter counts (cite TRM paper)
- [ ] Performance numbers (cite TRM paper)

#### Slide 5: Deep Supervision
- [ ] Code example (cite TRM or HRM paper methodology)
- [ ] 16 refinement steps (cite papers)

#### Slide 6: ARC Prize Revelation ⚠️ HIGH PRIORITY
- [x] 19% → 39% deep supervision (cite TRM paper lines 99-109)
- [x] 35.7% → 39% hierarchy (cite TRM paper lines 106-107)
- [x] Official quote (cite ARC Prize blog)

#### Slide 7: Training vs Inference
- [ ] Training/inference matrix data (cite ARC Prize Figure 5)
- [ ] +16pp, +4pp findings (cite ARC Prize analysis)

#### Slide 8: TRM Proves the Point
- [ ] Component comparison (cite both papers)

#### Slide 9: Our Hypothesis
- [ ] Testable predictions (original work, no citation needed)
- [ ] Supporting evidence (cite previous slides' sources)

#### Slide 10: Broader Implications
- [ ] Open questions (original work)

#### Slide 11: Provocative Alternative
- [ ] 31% vs 41% cross-task transfer (cite ARC Prize blog)
- [ ] Puzzle_ID embeddings (cite papers' methodology sections)
- [ ] Augmentation study (cite ARC Prize Figure 7)
- [ ] Verification drop 40% → 32% (cite ARC Prize)

#### Slide 12: Conclusion
- [ ] Summary statistics (reference previous slides)

---

### Phase 3: Implementation Pattern

For each citation, follow this pattern:

**Before**:
```svelte
<p>Deep supervision provides 2x improvement (19% → 39%)</p>
```

**After**:
```svelte
<script>
  import Citation from '../components/Citation.svelte';
</script>

<p>
  Deep supervision provides 2x improvement (19% → 39%)
  <Citation citeId="deep-supervision-2x" inline={true} />
</p>
```

**Developer reference** (in code comment):
```html
<!-- Source: less_is_more_extracted.txt, lines 99-109 -->
```

---

### Phase 4: Create References Slide (30 minutes)

Add a new slide at the end:

**File**: `presentation/src/slides/Slide13.svelte` (optional backup slide)

```svelte
<div class="slide">
  <h1 class="slide-title text-center">References</h1>
  
  <div class="references">
    <div class="reference">
      <h3>[trm-2025]</h3>
      <p>Jolicoeur-Martineau et al. (2025). "Less is More: Recursive Reasoning with Tiny Networks"</p>
      <a href="https://arxiv.org/abs/XXXX.XXXXX">ArXiv Link</a>
    </div>
    
    <div class="reference">
      <h3>[hrm-2025]</h3>
      <p>Wang et al. (2025). "Hierarchical Reasoning Model"</p>
      <a href="https://arxiv.org/abs/XXXX.XXXXX">ArXiv Link</a>
    </div>
    
    <div class="reference">
      <h3>[arc-prize-2025]</h3>
      <p>ARC Prize Foundation (2025). "HRM Analysis and Verification"</p>
      <a href="https://arcprize.org/blog/hrm-analysis">Blog Post</a>
    </div>
  </div>
</div>
```

---

## File Organization

```
presentation/
├── public/
│   ├── data/
│   │   ├── citations.json           # NEW: Citation database
│   │   └── ... (existing data files)
│   └── papers/                       # NEW: Local PDF copies
│       ├── less_is_more.pdf         # Copy from docs/papers/
│       └── hrm.pdf                   # Copy from docs/papers/
├── src/
│   ├── components/
│   │   ├── Citation.svelte          # NEW: Citation component
│   │   └── ... (existing components)
│   └── slides/
│       ├── Slide01.svelte            # MODIFY: Add citations
│       ├── ... (modify all slides)
│       └── Slide13.svelte            # NEW: References slide (optional)
│
docs/papers/                          # KEEP: Development reference
├── less_is_more_extracted.txt        # Line numbers for finding quotes
├── hrm_extracted.txt                 # Line numbers for finding quotes
└── ... (original PDFs)
```

---

## Usage Workflow

### For You (Developer):
1. Find claim in slide
2. Locate quote in `docs/papers/*_extracted.txt` (use line numbers)
3. Add entry to `citations.json` with:
   - Quote text
   - Line number (for your reference)
   - Page number (for viewers)
   - ArXiv URL
4. Add `<Citation citeId="..." />` to slide
5. Add comment: `<!-- Source: file.txt, lines X-Y -->`

### For Viewers:
1. See superscript citation number or link
2. Click to view popup with:
   - Full quote
   - Source attribution
   - Link to original paper
3. Click through to verify on ArXiv/blog

---

## Checklist

### Infrastructure Setup
- [ ] Create `citations.json` with initial data
- [ ] Create `Citation.svelte` component
- [ ] Copy PDFs to `public/papers/`
- [ ] Test citation popup functionality
- [ ] Add keyboard shortcut to close popup (Escape key)

### Data Population
- [ ] Get ArXiv URLs for both papers
- [ ] Get ARC Prize blog URL
- [ ] Map all quotes from txt files to page numbers
- [ ] Create citation entries for all key claims

### Slide Integration
- [ ] Add citations to Slide 1 (verification numbers)
- [ ] Add citations to Slide 2 (LLM performance)
- [ ] Add citations to Slide 3 (Kahneman quote)
- [ ] Add citations to Slide 4 (parameter counts)
- [ ] Add citations to Slide 5 (methodology)
- [ ] Add citations to Slide 6 (ablation results) ⚠️ Priority
- [ ] Add citations to Slide 7 (training/inference data)
- [ ] Add citations to Slide 8 (component analysis)
- [ ] Add citations to Slide 11 (memorization evidence)
- [ ] Create Slide 13 (References) - optional

### Testing & Polish
- [ ] Test all citation popups
- [ ] Verify all external links work
- [ ] Ensure citations don't break slide layout
- [ ] Add smooth transitions/animations
- [ ] Test keyboard navigation
- [ ] Test on different screen sizes

---

## Next Steps

1. **Immediate**: Get official ArXiv URLs for both papers
2. **Then**: Create basic Citation component and test on Slide 6
3. **After approval**: Go slide-by-slide adding citations with user

---

## Notes

- Keep txt files in `docs/papers/` for development only
- Don't expose line numbers to end users
- Use page numbers and section names in popups
- Link to authoritative sources (ArXiv, blogs)
- Local PDFs as backup for offline viewing
- Citations should be unobtrusive (superscript or small icons)
- Popups should be easy to dismiss (click outside or Escape)

---

## Estimated Time

- **Setup**: 1 hour
- **Data population**: 1 hour  
- **Slide integration**: 2-3 hours (depends on number of citations)
- **Testing**: 30 minutes

**Total**: 4.5-5.5 hours

