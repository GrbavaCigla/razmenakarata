<script lang="ts">
  import type { PageData } from "./$types";

  export let data: PageData;
</script>

<div class="bg-base-100 card xl:card-side shadow">
  <img src="{data.event.thumbnail}" class="rounded-t-box xl:rounded-l-box xl:w-96 object-cover" alt="" />
  <div class="card-body">
    <h2 class="card-title">{data.event.name}</h2>
    <!-- TODO: Collapse because on mobile this is too long -->
    <p>{data.event.description}</p>
  </div>
</div>

<div class="shadow rounded-box p-2 bg-base-100">
  <div class="overflow-auto">
    <table class="table w-full">
      <thead class="rounded-btn">
        <tr>
          <th class="hidden sm:table-cell">Online</th>
          <th class="hidden md:table-cell">Količina</th>
          <th>Paket</th>
          <th>Cena</th>
          <th>Korisnik</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {#each data.tickets as ticket}
          <tr>
            <td class="hidden sm:table-cell">
              {#if ticket.online}
                <div class="h-5 w-10 rounded-btn border-none bg-success"></div>
              {:else}
                <div class="h-5 w-10 rounded-btn border-none bg-error"></div>
              {/if}
            </td>
            <td class="hidden md:table-cell">{ticket.amount}</td>
            <td>{ticket.package}</td>
            <td>{ticket.price}</td>
            <td>{ticket.owner}</td>
            <td>
              <button class="btn btn-sm btn-secondary">
                Kupi
              </button>
            </td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>
