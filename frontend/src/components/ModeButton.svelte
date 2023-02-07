<script lang="ts">
  import { createEventDispatcher } from "svelte";

  export let is_login: boolean = true;

  const dispatch = createEventDispatcher();

  function submit(_is_login: boolean) {
    if (is_login == _is_login) {
      dispatch("submit", {
        is_login: is_login,
      });
    } else {
      is_login = _is_login;
    }
  }
</script>

<div class="flex btn-group no-animation">
  <input
    type="submit"
    on:click="{() => submit(true)}"
    class="btn transition-all"
    class:btn-primary="{is_login}"
    class:flex-1="{is_login}"
    value="Ulogujte se"
  />
  <input
    type="submit"
    on:click="{() => submit(false)}"
    class="btn transition-all"
    class:btn-primary="{!is_login}"
    class:flex-1="{!is_login}"
    value="Registrujte se"
  />
</div>
