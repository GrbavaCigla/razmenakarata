<script lang="ts">
  import { category, city } from "$stores/filter";

  export let cities: string[];
  export let categories: string[];
</script>

<div class="flex flex-col gap-2">
  <div>
    <span class="font-extrabold opacity-80 mb-0.5 ml-2">Filteri</span>
    <div class="card shadow card-compact bg-base-100">
      <div class="card-body flex gap-4">
        <select class="select bg-base-200" bind:value="{$city}">
          <option value="">Grad</option>
          {#each cities as city}
            <option value="{city}">{city}</option>
          {/each}
        </select>
        <select class="select bg-base-200" bind:value="{$category}">
          <option value="">Kategorija</option>
          {#each categories as category}
            <option value="{category}">{category}</option>
          {/each}
        </select>
      </div>
    </div>
  </div>

  <div>
    <span class="font-extrabold opacity-80 mb-0.5 ml-2">Stranica</span>
    <div
      class="btn-group bg-base-100 rounded-box shadow overflow-hidden w-full"
    >
      <button class="btn no-animation btn-ghost">1</button>
      <button class="btn no-animation btn-ghost">2</button>
      <button class="btn no-animation grow btn-ghost bg-base-100 btn-disabled"
        >...</button
      >
      <button class="btn no-animation btn-ghost">99</button>
      <button class="btn no-animation btn-ghost">100</button>
    </div>
  </div>

  <div>
    <span class="font-extrabold opacity-80 mb-0.5 ml-2">Reklama</span>
    <div class="card shadow card-compact bg-base-100 w-full h-96"></div>
  </div>
</div>
