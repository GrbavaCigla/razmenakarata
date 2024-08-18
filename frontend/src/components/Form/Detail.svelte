<script lang="ts">
    export let form: any;

    $: details = (form?.non_field_errors ?? []).concat(
        form?.detail == null ? [] : [form?.detail],
    );
    $: is_error = details.length == 0;
</script>

<div class="space-y-2">
    {#each details as detail}
        <p class="text-error text-center" class:hidden="{is_error}">
            {detail}
        </p>
    {/each}
</div>
