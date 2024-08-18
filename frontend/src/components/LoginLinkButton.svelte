<!-- TODO: Finish this. IMPORTANT -->
<script lang="ts">
    import { enhance } from "$app/forms";
    import { page } from "$app/stores";
    import { notifications } from "$src/stores/notification";
</script>

{#if $page.data.session == null}
    <a class="btn btn-ghost" href="/login">Ulogujte se</a>
{:else}
    <div class="dropdown dropdown-end hidden lg:inline-block">
        <div class="avatar placeholder indicator">
            <span class="indicator-item badge badge-primary h-0 p-1.5 right-0.5 top-0.5"></span>
            <div class="mask mask-squircle h-10 w-10">
                <!-- TODO: Add user initials -->
                <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
                <!-- svelte-ignore a11y-label-has-associated-control -->
                <label
                    tabindex="0"
                    class="btn btn-neutral no-animation text-lg font-bold m-1"
                >
                    {$page.data.user.first_name[0].toUpperCase()}{$page.data.user.last_name[1].toUpperCase()}
                </label>
            </div>
        </div>
        <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
        <ul
            tabindex="0"
            class="dropdown-content menu p-2 mt-1 shadow bg-base-100 rounded-box w-52"
        >
            <li><a href="/profile">Moj nalog</a></li>
            <li><a href="/chat">Konverzacije</a></li>
            <form method="POST" action="/logout" use:enhance>
                <input
                    type="hidden"
                    name="redirect"
                    value="{$page.url.pathname}"
                />
                <li>
                    <button>Izlogujte se</button>
                </li>
            </form>
        </ul>
    </div>
    <a class="btn btn-ghost lg:hidden" href="/account">Moj nalog</a>
{/if}
