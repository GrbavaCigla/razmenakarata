<script lang="ts">
    export let title: string = "";
</script>

<div class="alert shadow bg-base-100">
    <div>
        <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="stroke-info flex-shrink-0 w-6 h-6"
        >
            <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            >
            </path>
        </svg>
        <span>{title}</span>
    </div>
    <div class="flex-none">
        <!-- TODO: Add X svg here -->
        <button class="btn btn-sm btn-square" on:click>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-white"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                ><path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12"
                >
                </path>
            </svg>
        </button>
    </div>
</div>
