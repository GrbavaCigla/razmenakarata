import { writable, type Writable } from "svelte/store";
import { browser } from "$app/environment";

// TODO: Refactor this to be session store
export const access_token: Writable<string | null> = writable(
  (browser && localStorage.getItem("access_token")) || null
);
export const refresh_token: Writable<string | null> = writable(
  (browser && localStorage.getItem("refresh_token")) || null
);

refresh_token.subscribe((val) => {
  if (val && browser) localStorage.setItem("refresh_token", val);
});
access_token.subscribe((val) => {
  if (val && browser) localStorage.setItem("access_token", val);
});
