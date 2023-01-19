<script lang="ts">
  import { category } from "../stores/filter";
</script>

<div class="card card-compact bg-base-100">
  <div class="card-body flex gap-4">
    <select class="select bg-base-200">
      <option value="grad">Grad</option>
    </select>
    <select class="select bg-base-200" bind:value="{$category}">
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
</div>
