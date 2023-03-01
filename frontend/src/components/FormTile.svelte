<script lang="ts">
  export let name: string;
</script>

<div class="flex flex-col space-y-2">
  <span class="font-bold">{name}</span>
  <slot />
</div>
