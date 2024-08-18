import { browser } from "$app/environment";
import { notifications } from "$stores/notification";
import type { Cookies } from "@sveltejs/kit";
import { default as JSCookies } from "js-cookie";

export { NotificationStatus, type Notification } from "./model";

import { NotificationStatus, type Notification } from "./model";

export let Notifications = {
    store_reset(): { [id: number]: Notification } {
        return JSON.parse(browser && JSCookies.get("notifications") || "{}");
    },
    remove(id: number, cookies?: Cookies | undefined): undefined {
        if (browser) {
            notifications.update((notifs) => {
                delete notifs[id];
                return notifs;
            })
        } else if (cookies != null) {
            let notifs = JSON.parse(cookies.get("notifications") || "{}");
            delete notifs[id];
            cookies.set("notifications", JSON.stringify(notifs), { path: "/" });
        }
    },
    set(notification: Notification, cookies?: Cookies | undefined): undefined {
        if (browser) {
            notifications.update((notifs) => {
                notifs[notification.message.hashCode()] = notification;
                return notifs;
            })
        } else if (cookies != null) {
            let notifs = JSON.parse(cookies.get("notifications") || "{}");
            notifs[notification.message.hashCode()] = notification;
            cookies.set("notifications", JSON.stringify(notifs), { path: "/", httpOnly: false });
        }
    },
    set_form(form: any, cookies?: Cookies | undefined) {
        if (form != null) {
            for (let message of combine_errors(form)) {
                this.set({
                    message: message as string,
                    status: NotificationStatus.ERROR
                }, cookies)
            }
        }
    }
}

function combine_errors(form: any) {
    let messages: string[] = [];
    if (form != null) {
        for (let [key, val] of Object.entries(form)) {
            if (val instanceof Array) {
                messages.push(...val);
            } else if (typeof val === "string") {
                messages.push(val);
            }
        }
    }
    return messages;
}

declare global {
    interface String {
        hashCode(): number;
    }
}


String.prototype.hashCode = function () {
    return this.split("").reduce(
        function (a, b) {
            a = ((a << 5) - a) + b.charCodeAt(0);
            return a & a
        }, 0);
}

