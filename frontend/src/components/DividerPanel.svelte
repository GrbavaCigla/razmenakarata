<div class="flex flex-row h-full items-stretch gap-2">
    <div class="w-1/4 space-y-2">
        <slot name="panel"></slot>
    </div>
    <div class="flex-1 shadow bg-base-100 card">
        <slot name="body"></slot>
    </div>
</div>
