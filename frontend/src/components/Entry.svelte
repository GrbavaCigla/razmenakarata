<script lang="ts">
  export let name: string | null;
  export let placeholder: string | null;
  export let value: string = "";
  export let errors: string[] = [];
  export let type: string = "text";

  function type_action(node: any) {
    node.type = type;
  }

  $: is_error = errors.length != 0;
</script>

<div>
  <label for="{name}" class="sr-only">{placeholder}</label>
  <!-- TODO: Remove red border on error, only red outline should be there -->
  <input
    use:type_action
    class="input w-full bg-base-200"
    class:input-error="{is_error}"
    placeholder="{placeholder}"
    name="{name}"
    id="{name}"
    bind:value="{value}"
  />
  {#each errors as error}
    <label class="text-error" for="{name}">{error}</label>
  {/each}
</div>
