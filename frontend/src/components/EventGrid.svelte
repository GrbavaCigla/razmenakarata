<script lang="ts">
  import { onMount } from "svelte";
  import fuzzysort from "fuzzysort";
  import EventCard from "./EventCard.svelte";

  export let search_value: string = "";
  let events: [] = [];

  // TODO: Optimize this using fuzzysort.prepare
  $: filtered = fuzzysort
    .go(search_value, events, { key: "name", all: true })
    .map((x) => x.obj);

  onMount(async () => {
    // TODO: Unhardcode this url
    const res = await fetch("http://127.0.0.1:8000/api/events/?format=json");
    events = await res.json();
  });
</script>

<div
  class="rounded-box shadow bg-base-100 p-4 gap-4 grid w-full grid-cols-[repeat(auto-fill,_minmax(240px,_1fr))] h-full overflow-y-auto items-start"
>
  {#if events.length == 0}
    <!-- TODO: Make this less ugly -->
    <div class="leading-normal text-center p-16">
      <h1 class="text-3xl">No data :(</h1>
      <p class="font-bold">Something went wrong.</p>
    </div>
  {:else}
    {#each filtered as event}
      <EventCard {...event} />
    {/each}
  {/if}
</div>
