<script lang="ts">
  import Scaffold from "$components/Scaffold.svelte";
  import { create_ticket } from "$api/ticket";
  import FormTile from "$components/FormTile.svelte";
  import type { PageData } from "./$types";
  import { access_token } from "$stores/auth";
  import { notifications } from "$stores/notification";
  import { goto } from "$app/navigation";

  export let data: PageData;

  let selected_event_id: number = 0;
  let selected_ticket: string;
  // TODO: Add default price to package in models
  let price: number = 0;
  let is_online: boolean = false;

  function update_data(id: number) {
    let event = data.events.filter((obj: any) => obj.id == id)[0];

    selected_ticket = event.packages[0];

    return event;
  }

  $: selected_event = update_data(selected_event_id);

  function on_submit() {
    create_ticket(selected_event_id, selected_ticket, is_online, price, $access_token);
    $notifications = [
      ...$notifications,
      "Uspešno ste objavili kartu za prodaju.",
    ];
    goto("/");
  }
</script>

<Scaffold>
  <div class="card bg-base-100 shadow">
    <div class="card-body">
      <form
        method="POST"
        class="gap-4 grid grid-cols-1 sm:grid-cols-2 mx-auto"
        on:submit|preventDefault="{on_submit}"
      >
        <FormTile name="Dogadjaj">
          <select class="select bg-base-200" bind:value="{selected_event_id}">
            {#each data.events as event}
              <option value="{event.id}">{event.name}</option>
            {/each}
          </select>
        </FormTile>
        <FormTile name="Online">
          <input type="checkbox" class="toggle" bind:value="{is_online}" />
        </FormTile>
        <FormTile name="Cena">
          <input type="number" bind:value="{price}" class="input bg-base-200" />
        </FormTile>
        <FormTile name="Paket">
          <select class="select bg-base-200" bind:value="{selected_ticket}">
            {#each selected_event.packages as pkg}
              <option value="{pkg}">{pkg}</option>
            {/each}
          </select>
        </FormTile>
        <div class="col-span-1 sm:col-span-2 sm:text-end">
          <input
            type="submit"
            class="btn btn-primary w-full sm:w-auto"
            value="Prodajte kartu"
          />
        </div>
      </form>
    </div>
  </div>
</Scaffold>
