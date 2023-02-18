import { browser } from "$app/environment";
import { writable, type Writable } from "svelte/store";

export const theme: Writable<string | null> = writable(
  (browser && localStorage.getItem("theme")) || null
);

theme.subscribe((val) => {
  if (val && browser) localStorage.setItem("theme", val);
});
