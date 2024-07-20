<script lang="ts">
	export let name: string;
	export let placeholder: string | null = null;
	export let value: string = '';
	export let error: any;
	export let type: 'text' | 'email' | 'password' | 'number' | 'date' = 'text';

	function type_action(node: any) {
		node.type = type;
	}

	let _class: string = '';
	export { _class as class };

	$: is_error = error ? error.non_field_errors != null || error.detail != null || error[name] : false;
	$: errors = is_error && error[name] ? error[name] : [];
</script>

<div class={`w-full ${_class}`}>
	<label for={name} class="sr-only">{placeholder}</label>
	<input
		use:type_action
		class="input w-full bg-base-200"
		class:input-error={is_error}
		{placeholder}
		{name}
		id={name}
		bind:value
	/>
	{#each errors as error}
		<label class="text-error label-text" for={name}>{error}</label>
	{/each}
</div>
