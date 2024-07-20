<script lang="ts">
    export let name: string;
    export let value: any | undefined = undefined;
    export let placeholder: string | null = null;
    export let error: any;

    let _class: string = "";
    export { _class as class };

	$: is_error = error ? error.non_field_errors != null || error.detail != null || error[name] : false;
    $: errors = is_error && error[name] ? error[name] : [];
</script>

<div class="{`w-full ${_class}`}">
    <label for="{name}" class="sr-only">{placeholder}</label>
    <select
        class="select bg-base-200 w-full"
        class:input-error="{is_error}"
        {placeholder}
        {name}
        id="{name}"
        bind:value
    >
        <slot />
    </select>
    {#each errors as error}
        <label class="text-error label-text" for="{name}">{error}</label>
    {/each}
</div>
