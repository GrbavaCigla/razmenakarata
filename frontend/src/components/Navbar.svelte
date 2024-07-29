<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import LoginLinkButton from "$components/LoginLinkButton.svelte";
</script>

<div
    class="rounded-box justify-between shadow bg-base-100 p-4 gap-4 flex w-full items-center"
>
    <a href="/" class="logo hidden mx-4 sm:block">rk</a>
    <div class="lg:basis-2/5 lg:mx-8 w-full">
        <SearchBar />
    </div>
    <div class="gap-4 hidden lg:flex items-center">
        <LoginLinkButton />
        <a class="btn btn-primary" href="/tickets">Prodajte kartu</a>
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
