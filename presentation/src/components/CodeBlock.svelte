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

