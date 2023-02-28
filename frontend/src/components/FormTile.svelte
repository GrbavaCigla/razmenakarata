<script lang="ts">
  export let name: string;
</script>

<div>
  <span class="font-bold sm:justify-self-end self-center">{name}</span>
  <div class="self-center">
    <slot />
  </div>
</div>
