<!-- TODO: Finish this. IMPORTANT -->
<script lang="ts">
	import { page } from "$app/stores";
	import { notifications } from "$src/stores/notification";
	import { onMount } from "svelte";

	function logout() {
		$notifications = [
			...$notifications,
			"Uspešno ste se izlogovali sa Vašeg naloga.",
		];
	}
</script>

{#if $page.data.tokens.access == null}
	<a class="btn btn-ghost" href="/login">Ulogujte se</a>
{:else}
	<div class="dropdown dropdown-end hidden lg:inline-block">
		<div class="avatar placeholder">
			<div
				class="bg-neutral text-neutral-content mask mask-squircle h-10 w-10"
			>
				<!-- TODO: Add user initials -->
				<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
				<!-- svelte-ignore a11y-label-has-associated-control -->
				<label
					tabindex="0"
					class="btn no-animation text-lg font-bold m-1">JD</label
				>
			</div>
		</div>
		<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
		<ul
			tabindex="0"
			class="dropdown-content menu p-2 mt-1 shadow bg-base-100 rounded-box w-52"
		>
			<form method="GET" action="/logout">
				<input type="hidden" name="redirect" value="{$page.url.pathname}" />
				<li>
					<button type="submit">Izlogujte se</button>
				</li>
			</form>
			<li><a href="/profile">Moj nalog</a></li>
		</ul>
	</div>
	<a class="btn btn-ghost lg:hidden" href="/account">Moj nalog</a>
{/if}
