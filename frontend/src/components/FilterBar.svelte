<script lang="ts">
  import SearchBar from "./SearchBar.svelte";
</script>

<div class="w-full flex justify-between">
  <div class="rounded-box shadow bg-base-100 p-4 gap-4 flex justify-center">
    <SearchBar />
    <select class="select bg-base-200">
      <option value="city">City</option>
    </select>
    <select class="select bg-base-200">
      <option value="category">Category</option>
    </select>
  </div>
  <div class="rounded-box shadow bg-base-100 p-4 gap-4 flex">
    <select class="select bg-base-200">
      <option value="alphabetical">Alphabetical</option>
    </select>
    <select class="select bg-base-200">
      <option value="ascending">Ascending</option>
      <option value="descending">Descending</option>
    </select>
  </div>
</div>
