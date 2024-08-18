<script lang="ts">
    import { NotificationStatus } from "$utils/notifications";
    import { CircleAlert, CircleX, CircleCheck, Info, X } from "lucide-svelte";

    export let title: string = "";
    export let status: NotificationStatus = NotificationStatus.INFO;
</script>

<div class="alert shadow bg-base-100">
    {#if status == NotificationStatus.INFO}
        <Info class="stroke-info flex-shrink-0 w-6 h-6"></Info>
    {:else if status == NotificationStatus.SUCCESS}
        <CircleCheck class="stroke-info flex-shrink-0 w-6 h-6"></CircleCheck>
    {:else if status == NotificationStatus.WARNING}
        <CircleAlert class="stroke-info flex-shrink-0 w-6 h-6"></CircleAlert>
    {:else if status == NotificationStatus.ERROR}
        <CircleX class="stroke-info flex-shrink-0 w-6 h-6"></CircleX>
    {/if}
    <span>{title}</span>
    <button class="btn btn-sm btn-square btn-error" on:click>
        <X class="h-5 w-5"></X>
    </button>
</div>
