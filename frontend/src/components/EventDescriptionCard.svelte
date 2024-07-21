<script lang="ts">
    export let thumbnail: URL | null;
    export let name: string | null;
    export let description: string | null;
</script>

<div class="bg-base-100 card xl:card-side shadow">
  <img
    src="{thumbnail?.toString()}"
    class="rounded-t-box xl:rounded-t-none xl:rounded-l-box xl:w-96 object-cover"
    alt=""
  />
  <div class="card-body">
    <h2 class="card-title">{name}</h2>
    <!-- TODO: Collapse because on mobile this is too long -->
    <p>{description}</p>
  </div>
</div>
