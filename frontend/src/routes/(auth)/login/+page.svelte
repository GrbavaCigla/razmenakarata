<script lang="ts">
	import { slide } from 'svelte/transition';

	let is_login = true;

	function login() {
		if (!is_login) {
			is_login = !is_login;
		} else {

		}
	}

	function register() {
		if (is_login) {
			is_login = !is_login;
		} else {

		}
	}
</script>

<div class="h-screen w-screen flex flex-col justify-center items-center bg-base-100 sm:bg-inherit">
  <h1 class="font-bold text-4xl mb-4">Logo</h1>
  <div class="bg-base-100 rounded-box sm:shadow max-w-lg w-full p-8 flex flex-col gap-4">
		<span class="text-3xl font-bold text-center">
			{#if is_login}
			Ulogujte se
			{:else}
			Registrujte se
			{/if}
		</span>

		{#if !is_login}
    	<input type="text" transition:slide placeholder="Username" class="input w-full bg-base-200" />
		{/if}

    <input type="email" placeholder="Email" class="input w-full bg-base-200" />
    <input type="password" placeholder="Password" class="input w-full bg-base-200" />

		{#if !is_login}
    	<input type="password" transition:slide placeholder="Repeat password" class="input w-full bg-base-200" />
		{/if}

		{#if is_login}
			<label transition:slide class="label cursor-pointer justify-start">
				<input type="checkbox" class="checkbox checkbox-primary" />
				<span class="label-text ml-4">Remember me</span>
			</label>
		{/if}

		<div class="flex btn-group no-animation">
			<button on:click="{login}" class="btn transition-all" class:btn-primary="{is_login}" class:flex-1="{is_login}">Ulogujte se</button>
			<button on:click="{register}" class="btn transition-all" class:btn-primary="{!is_login}" class:flex-1="{!is_login}">Registrujte se</button>
		</div>
  </div>
</div>
