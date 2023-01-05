<script lang="ts">
    export let name: string = "";
    export let thumbnail: string = "";
    export let location: string = "";
</script>

<div class="card shadow">
    <figure><img src={thumbnail} alt="thumbnail"></figure>
    <div class="card-body">
        <div class="card-title">
            {name}
        </div>
        {location}
    </div>
</div>