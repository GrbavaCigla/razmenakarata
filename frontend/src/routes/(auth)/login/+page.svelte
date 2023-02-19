<script lang="ts">
  import { goto } from "$app/navigation";
  import LoginCard from "$src/components/LoginCard.svelte";
  import { notifications } from "$stores/notification";
</script>

<!-- TODO: Break this down to components -->
<h1 class="logo text-6xl">rk</h1>
<LoginCard
  on:success="{() => {
    $notifications = [
      ...$notifications,
      'Uspešno ste se ulogovali na Vaš nalog.',
    ];
    goto('/');
  }}"
/>
