<script lang="ts">
    import { page } from "$app/stores";
    import type { PageData } from "./$types";
    import { onMount } from "svelte";

    let socket: WebSocket | undefined;
    let is_loaded = false;
    let message: string;

    export let data: PageData;

    onMount(() => (is_loaded = true));

    let messages: { message: string; user_id: number }[] = [];

    $: init_socket(+$page.params["id"], is_loaded);

    function init_socket(id: number | undefined, is_loaded: boolean) {
        messages = [];
        if (socket != null) {
            socket.removeEventListener("message", on_message);
            socket.close();
        }
        if (id == null || !is_loaded) return;
        socket = new WebSocket(`/ws/chat/${id}/?token=${data.session}`);
        socket.addEventListener("message", on_message);
        return socket;
    }

    function on_message(event: MessageEvent<any>) {
        messages = [...messages, JSON.parse(event.data)];
    }

    function send_message() {
        if (socket != null) {
            socket.send(
                JSON.stringify({
                    message: message,
                }),
            );
        }
    }
</script>

<div
    class="bg-base-200 h-full w-full border-8 rounded-box border-base-100 flex flex-col"
>
    <div class="flex-1 w-fill p-2">
        {#each messages as msg}
            <div
                class="chat"
                class:chat-end="{data.user.id == msg.user_id}"
                class:chat-start="{data.user.id != msg.user_id}"
            >
                <div
                    class="chat-bubble"
                    class:bg-primary="{data.user.id == msg.user_id}"
                    class:text-primary-content="{data.user.id == msg.user_id}"
                >
                    {msg.message}
                </div>
            </div>
        {/each}
    </div>
    <div class="w-full self-end join p-2">
        <textarea
            bind:value="{message}"
            class="join-item input resize-none flex-1 p-2"
        ></textarea>
        <button class="join-item btn btn-primary" on:click="{send_message}">
            Pošaljite
        </button>
    </div>
</div>
