<script>
  import "$src/app.postcss";
  import { theme } from "$src/stores/theme";
</script>

<div class="relative min-h-screen bg-base-200" data-theme="{$theme}">
  <slot />
</div>