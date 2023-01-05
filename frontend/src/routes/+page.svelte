<script lang="ts">
  import SearchBar from "../components/SearchBar.svelte";
  import FilterBar from "../components/FilterBar.svelte";
  import EventGrid from "../components/EventGrid.svelte";
</script>


<div class="container mx-auto flex flex-col gap-4 items-start p-8 h-full">
  <FilterBar />
  <EventGrid />
</div>
