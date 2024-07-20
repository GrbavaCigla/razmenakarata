import { create_ticket } from "$api/client/ticket";
import type { Ticket } from "$api/models/ticket";
import { handle_redirect } from "$api/utils/handle_redirect";
import { unwrap_form } from "$api/utils/unwrap_form";
import { fail, type Cookies } from "@sveltejs/kit";

export async function post_tickets(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    request: Request,
    cookies: Cookies,
    url: URL
) {
    let form = unwrap_form<Ticket>(await request.formData());
    form.online = form.online ?? 'off';

    let { data, error } = await create_ticket(
        fetch,
        cookies.get("session") ?? "",
        form.event,
        { ...form, amount: 1 }
    );

    if (error) {
        return fail(400, error);
    }

    throw handle_redirect(url);
}