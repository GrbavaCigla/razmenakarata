<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { login, type ErrorDisplay } from "$utils/auth/login";
  import { access_token, refresh_token } from "$stores/auth";
  import Entry from "$components/Entry.svelte";
  import ModeButton from "$components/ModeButton.svelte";

  const dispatch = createEventDispatcher();

  let is_login: boolean;
  let username: string;
  let password: string;
  let error: ErrorDisplay = { username: [], password: [], detail: null };

  async function onlogin() {
    const [body, _error] = await login(username, password);

    error = _error;

    if (body != null) {
      $access_token = body.access;
      $refresh_token = body.refresh;

      dispatch("success");
    }
  }
</script>

<div class="bg-base-100 rounded-box sm:shadow max-w-lg w-full p-8">
  <form method="POST" class="flex flex-col gap-4" on:submit|preventDefault="{onlogin}">
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
      bind:value="{username}"
    />

    <Entry
      type="password"
      name="password"
      placeholder="Password"
      errors="{error.password}"
      bind:value="{password}"
    />

    <ModeButton bind:is_login />
    <!-- TODO: Add error detail -->
  </form>
</div>
