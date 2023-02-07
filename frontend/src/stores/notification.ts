import { writable, type Writable } from "svelte/store";

export const notifications: Writable<string[]> = writable([]);
