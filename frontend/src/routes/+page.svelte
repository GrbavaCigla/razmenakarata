<script lang="ts">
  import Navbar from "../components/Navbar.svelte";
  import EventGrid from "../components/EventGrid.svelte";
  import Sidebar from "../components/Sidebar.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;
</script>

<div class="drawer h-full">
  <input id="main-drawer" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <div class="container mx-auto flex flex-col gap-4 p-4">
      <div class="sticky top-4 z-20 w-full">
        <Navbar />
      </div>
      <div class="flex w-full gap-4 items-start">
        <EventGrid events="{data.events}" />
        <div class="hidden lg:inline-block">
          <Sidebar />
        </div>
      </div>
      <footer class="shadow rounded-box p-4 bg-base-100">
        <!-- TODO: Add logo -->
        <p>Copyright © 2023 - All right reserved</p>
      </footer>
    </div>
  </div>

  <div class="drawer-side">
    <label for="main-drawer" class="drawer-overlay"></label>
    <ul class="menu gap-2 p-4 w-80 bg-base-100">
      <Sidebar />
      <div class="divider my-0"></div>
      <div class="btn btn-ghost">Ulogujte se</div>
      <div class="btn btn-primary">Prodajte kartu</div>
    </ul>
  </div>
</div>
