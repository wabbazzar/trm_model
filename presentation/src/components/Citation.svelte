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
  
  function handleBackgroundClick(event) {
    if (event.target === event.currentTarget) {
      showPopup = false;
    }
  }
  
  function handleKeydown(event) {
    if (event.key === 'Escape') {
      showPopup = false;
    }
  }
</script>

<svelte:window on:keydown={handleKeydown} />

{#if reference && citation}
  {#if inline}
    <sup class="citation-inline">
      <button on:click={togglePopup} class="citation-button" title="View citation">
        <span class="citation-icon">📚</span>
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
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <div class="citation-popup" on:click={handleBackgroundClick}>
      <div class="citation-popup-content">
        <button class="close-btn" on:click={togglePopup} title="Close">✕</button>
        <h4 class="title">{citation.title}</h4>
        <p class="authors">{citation.authors} ({citation.year})</p>
        
        {#if reference.quote}
          <blockquote>{@html reference.quote}</blockquote>
        {/if}
        
        <div class="location">
          {#if reference.section}
            <p>📑 Section: {reference.section}</p>
          {/if}
          {#if reference.page !== 'N/A'}
            <p>📄 Page {reference.page}</p>
          {/if}
        </div>
        
        <div class="links">
          <a href={citation.url} target="_blank" rel="noopener noreferrer" class="primary-link">
            View Source →
          </a>
        </div>
      </div>
    </div>
  {/if}
{/if}

<style>
  .citation-inline {
    margin-left: 2px;
  }
  
  .citation-button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0 2px;
    font-size: 1em;
    vertical-align: super;
    line-height: 0;
  }
  
  .citation-icon {
    font-size: 1.1em;
    transition: transform 0.2s;
  }
  
  .citation-button:hover .citation-icon {
    transform: scale(1.2);
  }
  
  .citation-block {
    margin: 0.5rem 0;
  }
  
  .citation-link {
    background: #3b82f6;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.25rem;
    cursor: pointer;
    font-size: 0.9rem;
  }
  
  .citation-link:hover {
    background: #2563eb;
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
    animation: fadeIn 0.2s;
  }
  
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
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
    box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    animation: slideUp 0.3s;
  }
  
  @keyframes slideUp {
    from {
      transform: translateY(20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
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
    width: 2rem;
    height: 2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.25rem;
  }
  
  .close-btn:hover {
    background: #f1f5f9;
    color: #1e293b;
  }
  
  .title {
    font-size: 1.25rem;
    font-weight: bold;
    margin: 0 0 0.5rem 0;
    color: #0f172a;
    padding-right: 2rem;
  }
  
  .authors {
    color: #64748b;
    font-size: 0.9rem;
    margin: 0 0 1rem 0;
  }
  
  blockquote {
    border-left: 4px solid #3b82f6;
    padding-left: 1rem;
    margin: 1rem 0;
    font-style: italic;
    color: #475569;
    background: #f8fafc;
    padding: 1rem;
    border-radius: 0.25rem;
  }
  
  .location {
    margin: 1rem 0;
    color: #64748b;
    font-size: 0.9rem;
  }
  
  .location p {
    margin: 0.25rem 0;
  }
  
  .links {
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #e2e8f0;
  }
  
  .primary-link {
    display: inline-block;
    color: #3b82f6;
    text-decoration: none;
    font-weight: 500;
    padding: 0.5rem 1rem;
    background: #eff6ff;
    border-radius: 0.25rem;
    transition: background 0.2s;
  }
  
  .primary-link:hover {
    background: #dbeafe;
    text-decoration: underline;
  }
</style>

