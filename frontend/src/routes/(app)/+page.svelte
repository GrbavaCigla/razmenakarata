<script lang="ts">
  import Navbar from "../../components/Navbar.svelte";
  import EventGrid from "../../components/EventGrid.svelte";
  import Sidebar from "../../components/Sidebar.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
</script>


<div class="flex w-full gap-4 items-start">
  <EventGrid events="{data.events}" />
  <div class="hidden lg:inline-block">
    <Sidebar />
  </div>
</div>
