import { create_ticket } from "$api/client/ticket";
import type { Ticket } from "$api/models/ticket";
import { unwrap_form } from "$api/utils/unwrap_form";

export async function post_tickets(
    request: Request,
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
) {
    let form = unwrap_form<Ticket>(await request.formData());

    // let { data, error } = await create_ticket(fetch, request.);
}