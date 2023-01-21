<script lang="ts">

    export let id: string = "";
    export let category: string = "";
    export let name: string = "";
    export let thumbnail: string = "";
    export let location: string = "";
    export let description: string = "";
    export let date: string = "";
</script>

<!-- TODO: Finish the design -->
<div class="card card-compact shadow md:hover:scale-105 z-10 bg-base-100 transition-all">
    <!-- TODO: Unhardcode this -->
    <figure><img src={thumbnail} class="w-full" alt="thumbnail" width="280" height="140"></figure>
    <div class="card-body justify-between">
        <div>
            <span class="badge mb-1">{category}</span>
            <div class="card-title">
                {name}
            </div>
        </div>
        <div class="font-black text-neutral flex justify-between items-end">
            <span>{location}</span>
            <span>{date}</span>
        </div>
    </div>
</div>
