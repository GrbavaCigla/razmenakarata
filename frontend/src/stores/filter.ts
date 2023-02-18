import { writable, type Writable } from "svelte/store";

export const search: Writable<string> = writable("");
export const category: Writable<string> = writable("");
export const city: Writable<string> = writable("");
