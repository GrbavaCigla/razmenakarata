<script lang="ts">
  import SearchBar from "./SearchBar.svelte";

  export let search_value: string = "";
</script>

<div class="w-full flex justify-between">
  <div class="rounded-box shadow bg-base-100 p-4 gap-4 flex justify-center">
    <SearchBar bind:value={search_value} />
    <select class="select bg-base-200">
      <option value="grad">Grad</option>
    </select>
    <select class="select bg-base-200">
      <option value="kategorija">Kategorija</option>
      <option value="docek7531">Doček 7531</option>
      <option value="domkulture">Dom kulture</option>
      <option value="koncerti">Koncerti</option>
      <option value="festivali">Festivali</option>
      <option value="pozorište">Pozorište</option>
      <option value="sport">Sport</option>
      <option value="događaji">Događaji</option>
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
