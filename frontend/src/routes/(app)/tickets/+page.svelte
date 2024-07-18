<script lang="ts">
    import Scaffold from "$components/Scaffold.svelte";
    import FormTile from "$components/FormTile.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;

    function update_data(id: number | undefined) {
        if (id == null) {
            return []
        }
        let event = data.events.filter((obj: any) => obj.id == id)[0];
        return event.packages;
    }

    let selected_event_id: number | undefined;
    $: packages = update_data(selected_event_id);
</script>

<Scaffold>
    <div class="card bg-base-100 shadow">
        <div class="card-body">
            <form
                action=""
                method="POST"
                class="gap-4 grid grid-cols-1 sm:grid-cols-2 mx-auto"
            >
                <FormTile title="Događaj">
                    <select
                        class="select bg-base-200"
                        bind:value="{selected_event_id}"
                    >
                        {#each data.events as event}
                            <option value="{event.id}">{event.name}</option>
                        {/each}
                    </select>
                </FormTile>
                <FormTile title="Online">
                    <input type="checkbox" class="toggle" />
                </FormTile>
                <FormTile title="Cena">
                    <input type="number" class="input bg-base-200" />
                </FormTile>
                <FormTile title="Paket">
                    <select class="select bg-base-200">
                        {#each packages as pkg}
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
