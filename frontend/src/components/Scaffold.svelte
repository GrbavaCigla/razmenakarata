<script>
  import Navbar from "$components/Navbar.svelte";
  import LoginLinkButton from "$components/LoginLinkButton.svelte";
  import Alert from "$components/Alert.svelte";
  import { notifications } from "$stores/notification";
  import { theme } from "$stores/theme";
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

      <footer class="shadow mt-auto rounded-box p-4 bg-base-100 flex justify-between">
        <!-- TODO: Add logo -->
        <p>Copyright © 2023 - All right reserved</p>
        <div class="flex gap-2">
          <p>Tamna tema</p>
          <!-- TODO: Connect to data-theme -->
          <input type="checkbox" class="toggle" bind:value="{$theme}">
        </div>
      </footer>
    </div>
  </div>

  <div class="drawer-side">
    <label for="main-drawer" class="drawer-overlay"></label>
    <ul class="menu gap-2 p-4 w-80 bg-base-200">
      <slot name="sidebar" />
      <div class="divider my-0"></div>
      <LoginLinkButton />
      <a class="btn btn-primary" href="/tickets">Prodajte kartu</a>
    </ul>
  </div>
</div>
