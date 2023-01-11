<script lang="ts">
    export let name: string = "";
    export let thumbnail: string = "";
    export let location: string = "";
</script>

<!-- TODO: Finish the design -->
<div class="card card-compact shadow">
    <!-- TODO: Unhardcode this -->
    <figure><img src={"http://127.0.0.1:8000" + thumbnail} alt="thumbnail"></figure>
    <div class="card-body">
        <div class="card-title">
            {name}
        </div>
        {location}
    </div>
</div>