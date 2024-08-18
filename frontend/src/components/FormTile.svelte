<script lang="ts">
    export let title: string;
</script>

<div class="flex flex-col space-y-2">
    <span class="font-bold">{title}</span>
    <slot />
</div>
