<script lang="ts">
    import { enhance } from "$app/forms";
    import EventDescriptionCard from "$components/EventDescriptionCard.svelte";
    import Scaffold from "$components/Scaffold.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<Scaffold>
    <EventDescriptionCard {...data.events[data.event_id]} />

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
                                    <div
                                        class="h-5 w-10 rounded-btn border-none bg-success"
                                    ></div>
                                {:else}
                                    <div
                                        class="h-5 w-10 rounded-btn border-none bg-error"
                                    ></div>
                                {/if}
                            </td>
                            <td class="hidden md:table-cell">{ticket.amount}</td
                            >
                            <td>{ticket.package}</td>
                            <td>{ticket.price}</td>
                            <td>{ticket.owner}</td>
                            <td>
                                <form action="" method="post" use:enhance>
                                    <input
                                        type="hidden"
                                        name="ticket_id"
                                        value="{ticket.id}"
                                    />
                                    <button class="btn btn-sm btn-secondary">
                                        Kupi
                                    </button>
                                </form>
                            </td>
                        </tr>
                    {/each}
                </tbody>
            </table>

            {#if (data?.tickets?.length ?? 0) == 0}
                <div class="h-96 flex justify-center items-center">
                    <!-- TODO: Add icon -->
                    <p class="text-3xl">Nema karata za ovaj događaj.</p>
                </div>
            {/if}
        </div>
    </div>
</Scaffold>
