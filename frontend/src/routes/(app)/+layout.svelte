<script>
  import Navbar from "$components/Navbar.svelte";
  import Sidebar from "$components/Sidebar.svelte";
  import LoginLinkButton from "$src/components/LoginLinkButton.svelte";
  import Alert from "$components/Alert.svelte";
  import { notifications } from "$stores/notification";
</script>

<div class="drawer">
  <input id="main-drawer" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <div class="container mx-auto flex flex-col gap-4 p-4 h-full">
      <div class="sticky top-4 z-20 w-full">
        <Navbar />
      </div>

      {#each $notifications as notif}
        <!-- TODO: Wire on:click to delete current notification -->
        <Alert title="{notif}" />
      {/each}

      <slot />

      <footer class="shadow mt-auto rounded-box p-4 bg-base-100">
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
      <LoginLinkButton />
      <button class="btn btn-primary"> Prodajte kartu </button>
    </ul>
  </div>
</div>
