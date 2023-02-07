<script lang="ts">
  import SearchBar from "./SearchBar.svelte";
  import LoginLinkButton from "$components/LoginLinkButton.svelte";
</script>

<div
  class="rounded-box justify-between shadow bg-base-100 p-4 gap-4 flex w-full items-center"
>
  <h1 class="text-2xl font-bold hidden sm:block">Logo</h1>
  <div class="lg:basis-2/5 lg:mx-8 w-full">
    <SearchBar />
  </div>
  <div class="gap-4 hidden lg:flex items-center">
    <LoginLinkButton />
    <button class="btn btn-primary">Prodajte kartu</button>
  </div>
  <label for="main-drawer" class="btn btn-square btn-ghost lg:hidden">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      class="inline-block w-6 h-6 stroke-current"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M4 6h16M4 12h16M4 18h16"
      >
      </path>
    </svg>
  </label>
</div>
