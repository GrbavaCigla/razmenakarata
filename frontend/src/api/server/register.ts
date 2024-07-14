import { create_user } from "$api/client/user";
import type { User } from "$api/models/user";
import { handle_redirect } from "$api/utils/handle_redirect";
import { unwrap_form } from "$api/utils/unwrap_form";
import { fail, type Cookies } from "@sveltejs/kit";

export async function register(
    request: Request,
    url: URL,
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
) {
    let form = unwrap_form<User>(await request.formData());

    let { data, error } = await create_user(fetch, form);

    if (error) {
        return fail(400, error);
    }

    throw handle_redirect(url, "/verify");
}