<script lang="ts">
  import { access_token } from "$stores/auth";

</script>

<!-- TODO: This check apparently doesn't work -->
{#if $access_token == null}
  <a class="btn btn-ghost" href="/login">Ulogujte se</a>
{:else}
  <a href="/account">
    <div class="avatar placeholder hidden lg:inline-flex">
      <div class="bg-neutral text-neutral-content mask mask-squircle h-10 w-10">
        <!-- TODO: Add user initials -->
        <span class="text-lg font-bold">JD</span>
      </div>
    </div>
  </a>
  <a class="btn btn-ghost lg:hidden" href="/account">Nalog</a>
{/if}
