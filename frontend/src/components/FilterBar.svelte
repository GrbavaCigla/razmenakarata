<script lang="ts">
  import SearchBar from "./SearchBar.svelte";

  export let search_value: string = "";
  export let category: string = "";
</script>

<div class="w-full flex justify-between">
  <div class="rounded-box shadow bg-base-100 p-4 gap-4 flex justify-center">
    <SearchBar bind:value={search_value} />
    <select class="select bg-base-200">
      <option value="grad">Grad</option>
    </select>
    <select bind:value="{category}" class="select bg-base-200">
      <option value="">Kategorija</option>
      <option value="Doček 7531">Doček 7531</option>
      <option value="Dom kulture">Dom kulture</option>
      <option value="Koncerti">Koncerti</option>
      <option value="Festivali">Festivali</option>
      <option value="Pozorište">Pozorište</option>
      <option value="Sport">Sport</option>
      <option value="Događaji">Događaji</option>
    </select>
  </div>
  <div class="rounded-box shadow bg-base-100 p-4 gap-4 flex">
    <select class="select bg-base-200">
      <option value="alfabetski">Alfabetski</option>
    </select>
    <select class="select bg-base-200">
      <option value="rastuce">Rastuće</option>
      <option value="opadajuce">Opadajuće</option>
    </select>
  </div>
</div>
