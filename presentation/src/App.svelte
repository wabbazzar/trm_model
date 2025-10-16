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
  
  const slides = [
    Slide01, Slide02, Slide03, Slide04, Slide05, Slide06,
    Slide07, Slide08, Slide09
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
    height: calc(100vh - 60px);
    overflow: hidden;
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

