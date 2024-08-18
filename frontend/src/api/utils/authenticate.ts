import { retrieve_me } from "$api/client/user";
import type { Cookies } from "@sveltejs/kit";

export async function authenticate_user(cookies: Cookies, fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>) {
    if (cookies.get("session")) {
        let { data, error } = await retrieve_me(fetch, cookies.get("session") ?? "");

        if (data) {
            return { session: cookies.get("session") ?? "", user: data };
        }
    }

    cookies.delete("session", { path: "/" });

    return { session: null, user: null };
}
