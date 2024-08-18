<script lang="ts">
    import { page } from "$app/stores";

    export let id: number;
    export let name: string;
    export let subtitle: string | undefined;

    $: selected = +$page.params.id == id;
</script>

<!-- TODO: Make whole card clickable -->
<div
    class="card card-compact shadow bg-base-100 transition-all hover:-translate-y-1 border-2 border-base-100"
    class:border-red-500="{selected}"
>
    <div class="flex">
        <div class="card-body flex-1">
            <a href="/chat/{id}">
                <div class="card-title">{name}</div>
                {#if subtitle}
                    <p class="text-neutral">{subtitle}</p>
                {/if}
            </a>
        </div>
        <div class="card-body flex-none justify-center">
            <!-- TODO: Add icon -->
            <button class="btn btn-square btn-ghost text-error">DEL</button>
        </div>
    </div>
</div>
