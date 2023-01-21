<script>
  import "../app.postcss";
  import Navbar from "../components/Navbar.svelte";
  import Sidebar from "../components/Sidebar.svelte";
</script>

<div class="drawer bg-base-200">
  <input id="main-drawer" type="checkbox" class="drawer-toggle" />
  <div class="drawer-content">
    <div class="container mx-auto flex flex-col gap-4 p-4 h-full">
      <div class="sticky top-4 z-20 w-full">
        <Navbar />
      </div>

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
      <div class="btn btn-ghost">Ulogujte se</div>
      <div class="btn btn-primary">Prodajte kartu</div>
    </ul>
  </div>
</div>
