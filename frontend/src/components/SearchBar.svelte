<script lang="ts">
    import { search } from "$stores/filter";

    import { Search } from "lucide-svelte";
</script>

<div class="relative font-bold">
    <input
        placeholder="Pretraži"
        class="input p-2 bg-base-200 w-full"
        type="text"
        name=""
        id=""
        bind:value="{$search}"
    />

    <button
        class="absolute btn no-animation right-0 rounded-l-none inline-flex justify-center items-center"
    >
        <Search class="h-6 w-6"></Search>
    </button>
</div>
