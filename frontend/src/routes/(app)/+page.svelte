<script lang="ts">
    import EventGrid from "$components/EventGrid.svelte";
    import Sidebar from "$components/Sidebar.svelte";
    import type { PageData } from "./$types";
    import Scaffold from "$components/Scaffold.svelte";

    export let data: PageData;

    $: cities = [...new Set(data.events.map((e) => e.city))];
    $: categories = [...new Set(data.events.map((c) => c.categories).flat())];
</script>

<Scaffold>
    <div class="flex w-full gap-4 items-start">
        <EventGrid events="{data.events}" />
        <div class="hidden lg:inline-block">
            <Sidebar {cities} {categories} />
        </div>
    </div>
    <svelte:fragment slot="sidebar">
        <Sidebar {cities} {categories} />
    </svelte:fragment>
</Scaffold>
