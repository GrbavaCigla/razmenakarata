<script lang="ts">
    import Navbar from "$components/Navbar.svelte";
    import LoginLinkButton from "$components/LoginLinkButton.svelte";
    import Alert from "$components/Alert.svelte";
    import { notifications } from "$stores/notification";
    import { theme } from "$stores/theme";

    function remove_notification(title: string) {
        var index = $notifications.indexOf(title);
        if (index > -1) {
            $notifications.splice(index, 1);
            $notifications = $notifications;
        }
    }
</script>

<!-- TODO: min-h-screen is workaround, find a solution with h-full -->
<div class="drawer min-h-screen">
    <input id="main-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content">
        <div class="container mx-auto flex flex-col gap-4 p-4 h-full">
            <div class="sticky top-4 z-10 w-full">
                <Navbar />
            </div>

            {#each $notifications as notif}
                <!-- TODO: Wire on:click to delete current notification -->
                <Alert
                    title="{notif}"
                    on:click="{remove_notification(notif)}"
                />
            {/each}

            <slot />

            <footer
                class="shadow rounded-box p-4 bg-base-100 flex justify-between mt-auto"
            >
                <!-- TODO: Add logo -->
                <p>Copyright © 2023 - All right reserved</p>
                <div class="flex gap-2">
                    <p>Tamna tema</p>
                    <!-- TODO: Connect to data-theme -->
                    <input
                        type="checkbox"
                        value="dark"
                        class="toggle theme-controller"
                    />
                </div>
            </footer>
        </div>
    </div>

    <div class="drawer-side z-20">
        <label for="main-drawer" class="drawer-overlay"></label>
        <ul class="menu gap-2 p-4 w-80 bg-base-200 min-h-full">
            <slot name="sidebar" />
            <div class="divider my-0"></div>
            <LoginLinkButton />
            <a class="btn btn-primary" href="/tickets">Prodajte kartu</a>
        </ul>
    </div>
</div>
