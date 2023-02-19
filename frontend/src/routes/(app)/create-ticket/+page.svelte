<script lang="ts">
  import Scaffold from "$components/Scaffold.svelte";
  import FormTile from "$src/components/FormTile.svelte";
  import type { PageData } from "./$types";

  export let data: PageData;

  let selected_event_id: number = 0;

  $: selected_event = data.events.filter((obj: any) => obj.id == selected_event_id)[0];
  $: console.log(selected_event);
</script>

<Scaffold>
  <div class="card bg-base-100 shadow">
    <form action="POST" class="card-body grid grid-cols-1 sm:grid-cols-2 gap-4">
      <FormTile name="Dogadjaj">
        <select class="select bg-base-200 w-full sm:w-auto" bind:value="{selected_event_id}">
          {#each data.events as event}
            <option value="{event.id}">{event.name}</option>
          {/each}
        </select>
      </FormTile>
      <FormTile name="Online">
        <input type="toggle" class="toggle">
      </FormTile>
      <FormTile name="Cena">
        <input type="text" class="input bg-base-200">
      </FormTile>
      <FormTile name="Paket">
        <select class="select bg-base-200 w-full sm:w-auto">
          {#each selected_event.packages as pkg}
            <option value="{pkg}">{pkg}</option>
          {/each}
        </select>
      </FormTile>
    </form>
  </div>
</Scaffold>
