<script lang="ts">
  import FilterBar from "../components/FilterBar.svelte";
  import EventGrid from "../components/EventGrid.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
</script>

<div class="container mx-auto flex flex-col gap-4 items-start p-8 h-full">
  <FilterBar />
  <EventGrid events="{data.events}" />
</div>
