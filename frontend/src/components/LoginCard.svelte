<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { login, type ErrorDisplay } from "$api/login";
  import { access_token, refresh_token } from "$stores/auth";
  import Entry from "$components/Entry.svelte";

  const dispatch = createEventDispatcher();

  let is_login: boolean = true;
  let username: string;
  let password: string;
  let error: ErrorDisplay = { username: [], password: [], detail: null };

  async function on_submit(value: boolean) {
    if (value != is_login) {
      is_login = value;
      return;
    }

    const [body, _error] = await login(username, password);

    error = _error;

    if (body != null) {
      $access_token = body.access;
      $refresh_token = body.refresh;

      dispatch("success");
    }
  }
</script>

<!-- TODO: Translate error messages -->
<div class="bg-base-100 rounded-box sm:shadow max-w-lg w-full p-8">
  <form
    method="POST"
    class="flex flex-col gap-4"
    on:submit|preventDefault
  >
    <span class="text-3xl font-bold text-center">
      {#if is_login}
        Ulogujte se
      {:else}
        Registrujte se
      {/if}
    </span>

    <Entry
      name="username"
      placeholder="Username"
      errors="{error.username}"
      error="{error.detail != null}"
      bind:value="{username}"
    />

    <Entry
      type="password"
      name="password"
      placeholder="Password"
      errors="{error.password}"
      error="{error.detail != null}"
      bind:value="{password}"
    />

    <div class="flex btn-group no-animation">
      <input
        type="submit"
        on:click="{() => (on_submit(true))}"
        class="btn transition-all"
        class:btn-primary="{is_login}"
        class:flex-1="{is_login}"
        value="Ulogujte se"
      />
      <input
        type="submit"
        on:click="{() => (on_submit(false))}"
        class="btn transition-all"
        class:btn-primary="{!is_login}"
        class:flex-1="{!is_login}"
        value="Registrujte se"
      />
    </div>
    {#if error.detail != null}
      <p class="text-error">{error.detail}</p>
    {/if}
  </form>
</div>
