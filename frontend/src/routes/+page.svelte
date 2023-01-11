<script lang="ts">
  import FilterBar from "../components/FilterBar.svelte";
  import EventGrid from "../components/EventGrid.svelte";

  let search_value: string = "";
  let category: string = "";
</script>


<div class="container mx-auto flex flex-col gap-4 items-start p-8 h-full">
  <FilterBar bind:category bind:search_value={search_value}/>
  <EventGrid category={category} search_value={search_value}/>
</div>
