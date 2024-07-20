<script lang="ts">
    import Scaffold from "$components/Scaffold.svelte";
    import FormTile from "$components/FormTile.svelte";
    import type { ActionData, PageData } from "./$types";
    import Entry from "$components/Form/Entry.svelte";
    import Select from "$components/Form/Select.svelte";
    import Detail from "$components/Form/Detail.svelte";
    import { enhance } from "$app/forms";

    export let data: PageData;
    export let form: ActionData;

    function update_data(id: number) {
        let events = data.events.filter((obj: any) => obj.id == id);
        if (events.length == 0) return [];
        return events[0].packages;
    }

    let selected_event_id: number;
    $: packages = update_data(selected_event_id);
</script>

<Scaffold>
    <div class="card bg-base-100 shadow">
        <div class="card-body">
            <form
                action=""
                method="POST"
                class="gap-4 grid grid-cols-1 sm:grid-cols-2 mx-auto"
                use:enhance
            >
                <FormTile title="Događaj">
                    <Select
                        name="event"
                        error="{form}"
                        placeholder="Izaberi događaj"
                        bind:value="{selected_event_id}"
                    >
                        {#each data.events as event}
                            <option value="{event.id}">{event.name}</option>
                        {/each}
                    </Select>
                </FormTile>
                <FormTile title="Online">
                    <input name="online" type="checkbox" class="toggle" />
                </FormTile>
                <FormTile title="Cena">
                    <Entry name="price" error="{form}" type="number" />
                </FormTile>
                <FormTile title="Paket">
                    <Select name="package" error="{form}">
                        {#each packages as pkg}
                            <option value="{pkg.id}">{pkg.name}</option>
                        {/each}
                    </Select>
                </FormTile>
                <Detail {form} />
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
