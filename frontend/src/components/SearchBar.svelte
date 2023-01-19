<script lang="ts">
  import { search } from "../stores/filter";
</script>

<div class="relative font-bold w-full">
  <input
    placeholder="Pretraži"
    class="input p-2 bg-base-200 w-full"
    type="text"
    name=""
    id=""
    bind:value={$search}
  />
</div>
