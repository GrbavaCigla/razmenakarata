import { create_chat } from "$api/client/chat";
import { handle_redirect } from "$api/utils/handle_redirect";
import { unwrap_form } from "$api/utils/unwrap_form";
import { Notifications } from "$utils/notifications";
import { fail, type Cookies } from "@sveltejs/kit";

export async function post_chat(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    request: Request,
    cookies: Cookies,
    url: URL
) {
    let form = unwrap_form<{ ticket_id: number }>(await request.formData());

    let { data, error } = await create_chat(
        fetch,
        cookies.get("session") ?? "",
        form.ticket_id,
    );

    // TODO: Use this error and ignore only if unique constraint failed
    if (error) {
        Notifications.set_form(error, cookies);
        return fail(400, error);
    }

    if (data && data.id) {
        throw handle_redirect(url, `/chat/${data.id}/`);
    }
}