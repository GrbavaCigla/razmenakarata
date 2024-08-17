import Cookies from "js-cookie";
import { writable, type Writable } from "svelte/store";
import { browser } from "$app/environment";
import type { Notification } from "$utils/notifications/model";

export const notifications: Writable<{ [id: number]: Notification }> = writable(
    JSON.parse((browser && Cookies.get("notifications")) || "{}")
);

notifications.subscribe((val) => {
    Cookies.set("notifications", JSON.stringify(val), { path: "/" });
});
