<script lang="ts">
    import ChatContact from "$components/ChatContact.svelte";
    import DividerPanel from "$components/DividerPanel.svelte";
    import Scaffold from "$components/Scaffold.svelte";
    import type { LayoutData } from "./$types";

    export let data: LayoutData;
</script>

<Scaffold>
    <div class="flex-1">
        <DividerPanel>
            <svelte:fragment slot="panel">
                {#each data.chats as chat}
                    <!-- TODO: Add event name -->
                    <ChatContact
                        id="{chat.id}"
                        name="{data.contacts[chat.user].first_name} {data.contacts[chat.user].last_name}"
                        subtitle="{chat.ticket.package}"
                    />
                {/each}
            </svelte:fragment>
            <svelte:fragment slot="body">
                <slot></slot>
            </svelte:fragment>
        </DividerPanel>
    </div>
</Scaffold>
