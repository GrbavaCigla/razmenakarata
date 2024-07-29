<script lang="ts">
    import UserVerification from "$components/UserVerification.svelte";
    import type { PageData } from "./$types";

    export let data: PageData;
</script>

<UserVerification
    title="Verifikujte se"
    message="{data.message}"
    status="{data.status}"
/>
