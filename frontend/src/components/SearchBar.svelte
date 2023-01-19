<script lang="ts">
  import { search } from "../stores/filter";
</script>

<div class="relative font-bold">
  <input
    placeholder="Pretraži"
    class="input p-2 bg-base-200 w-full"
    type="text"
    name=""
    id=""
    bind:value="{$search}"
  />

  <button
    class="absolute btn no-animation right-0 rounded-l-none inline-flex justify-center items-center"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="h-5 w-5"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2.5"
        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
      >
      </path>
    </svg>
  </button>
</div>
