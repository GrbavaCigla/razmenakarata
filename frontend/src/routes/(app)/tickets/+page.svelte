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
    <div class="card-body">
      <form action="POST" class=" gap-4 grid grid-cols-[repeat(auto-fill,_minmax(600px,_1fr))]">
        <FormTile name="Dogadjaj">
          <select class="select bg-base-200 whitespace-pre text-ellipsis w-full" bind:value="{selected_event_id}">
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
          <select class="select bg-base-200">
            {#each selected_event.packages as pkg}
              <option value="{pkg}">{pkg}</option>
            {/each}
          </select>
        </FormTile>
      </form>
    </div>
  </div>
</Scaffold>
