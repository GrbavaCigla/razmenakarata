<script lang="ts">
    export let name: string = "";
    export let thumbnail: string = "";
    export let location: string = "";
</script>

<!-- TODO: Finish the design -->
<div class="card card-compact shadow hover:scale-125 hover:z-10 bg-base-100 transition-all">
    <!-- TODO: Unhardcode this -->
    <figure><img src={thumbnail} alt="thumbnail" width="280" height="140"></figure>
    <div class="card-body">
        <div class="card-title">
            {name}
        </div>
        {location}
    </div>
</div>
