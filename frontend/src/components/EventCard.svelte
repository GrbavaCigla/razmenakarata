<script lang="ts">
  export let id: string = "";
  export let categories: string[] = [];
  export let name: string = "";
  export let thumbnail: string = "";
  export let location: string = "";
  export let city: string = "";
  export let description: string = "";
  export let start_date: string = "";
  export let end_date: string = "";
  export let packages: string = "";

  let date: string = Intl.DateTimeFormat('sr-RS').format(new Date(start_date));
</script>

<div
  class="card card-compact shadow md:hover:-translate-y-1 z-10 bg-base-100 transition-all"
>
  <figure>
    <!-- TODO: Add backend option to get images in different sizes -->
    <img
      src="{thumbnail}?width=200&height=144"
      class="w-full"
      alt="thumbnail"
      width="200"
      height="144"
    />
  </figure>
  <div class="card-body justify-between">
    <div>
      {#each categories as categ}
        <span class="badge mb-1 mr-1">{categ}</span>
      {/each}
      <div class="card-title">
        <a href="/{id}/">
          {name}
        </a>
      </div>
    </div>
    <div class="font-black text-neutral flex justify-between items-end">
      <span>{city}</span>
      <span>{date}</span>
    </div>
  </div>
</div>
