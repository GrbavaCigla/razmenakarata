<script lang="ts">
    import Entry from "$components/Entry.svelte";
    import type { PageData, ActionData } from "./$types";
    import { enhance } from "$app/forms";

    export let data: PageData;
    export let form: ActionData;

    $: is_login = data.action == "login";
</script>

<form method="POST" class="flex flex-col gap-4" action="?/{data.action}" use:enhance>
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
            <input
                type="submit"
                class="btn btn-primary flex-1"
                value="Ulogujte se"
            />
            <a href="/register/" class="btn">Registrujte se</a>
        {:else}
            <a href="/login/" class="btn">Ulogujte se</a>
            <input
                type="submit"
                class="btn transition-all btn-primary flex-1"
                value="Registrujte se"
            />
        {/if}
    </div>
	<p class="text-error text-center" class:hidden={form == null || form?.detail == null}>{form?.detail ?? ''}</p>
</form>
