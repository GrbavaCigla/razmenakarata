<script lang="ts">
    import Entry from "$components/Entry.svelte";
    import type { PageData, ActionData } from "./$types";
    import { enhance } from "$app/forms";
    import { page } from "$app/stores";

    export let data: PageData;
    export let form: ActionData;

    let is_loading = false;

    $: is_login = data.action == "login";
</script>

<form
    method="POST"
    class="flex flex-col gap-4"
    action="?/{data.action}{$page.url.searchParams.get('redirect') == null
        ? ''
        : '&redirect=' + $page.url.searchParams.get('redirect')}"
    use:enhance="{() => {
        is_loading = true;
        return async ({ update }) => {
            is_loading = false;
            update();
        };
    }}"
>
    <span class="text-3xl font-bold text-center">
        {#if is_login}
            Ulogujte se
        {:else}
            Registrujte se
        {/if}
    </span>

    {#if !is_login}
        <div class="flex w-full gap-4">
            <Entry
                name="first_name"
                error="{form}"
                placeholder="First name"
                type="text"
            />
            <Entry
                name="last_name"
                error="{form}"
                placeholder="Last name"
                type="text"
            />
        </div>
    {/if}

    <Entry name="email" error="{form}" placeholder="Email" type="email" />

    <div>
        <Entry
            name="password"
            error="{form}"
            placeholder="Password"
            type="password"
        />
        {#if is_login}
            <label for="password">
                <!-- TODO: Add password reset -->
                <a href="#" class="text-blue-500 mt-1 ml-2">
                    Forgot password?
                </a>
            </label>
        {/if}
    </div>

    {#if !is_login}
        <Entry
            name="re_password"
            error="{form}"
            placeholder="Repeat password"
            type="password"
        />
    {/if}

    <!-- TODO: Add animations -->
    <div class="flex btn-group no-animation">
        {#if is_login}
            <button class="btn btn-primary flex-1">
                Ulogujte se
                <span class="loading" class:hidden="{!is_loading}"></span>
            </button>
            <a href="/register/" class="btn">Registrujte se</a>
        {:else}
            <a href="/login/" class="btn">Ulogujte se</a>
            <button class="btn btn-primary flex-1">
                Registrujte se
                <span class="loading" class:hidden="{!is_loading}"></span>
            </button>
        {/if}
    </div>
    <p
        class="text-error text-center"
        class:hidden="{form == null || form?.detail == null}"
    >
        {form?.detail ?? ""}
    </p>
</form>
