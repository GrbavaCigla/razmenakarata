<script lang="ts">
  import { onMount } from "svelte";
  import { search, category } from "../stores/filter";
  import fuzzysort from "fuzzysort";
  import EventCard from "./EventCard.svelte";

  export let events: [] = [];

  // TODO: Optimize this using fuzzysort.prepare
  $: filtered = fuzzysort
    .go($search, events, { key: "name", all: true })
    .map(x => x.obj)
    .filter(x => $category == "" ? true : x.category == $category)
</script>

<div class="rounded-box shadow bg-base-100 p-4 w-full h-full">
  {#if events.length == 0}
    <!-- TODO: Make this less ugly -->
    <div class="flex w-full h-full">
      <div class="m-auto p-16">
        <h1 class="text-5xl text-center">No data :(</h1>
        <p class="text-xl font-bold">Something went wrong.</p>
      </div>
    </div>
  {:else}
    <div class="gap-4 grid grid-cols-[repeat(auto-fill,_minmax(240px,_1fr))] ">
      {#each filtered as event}
        <EventCard {...event} />
      {/each}
    </div>
  {/if}
</div>
