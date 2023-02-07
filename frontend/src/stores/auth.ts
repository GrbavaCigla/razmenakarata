import { writable, type Writable } from "svelte/store";

export const access_token: Writable<string | null> = writable(null);
export const refresh_token: Writable<string | null> = writable(null);
