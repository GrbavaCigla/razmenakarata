import type { TokenPair } from "$api/models/auth";
import type { Ticket, TicketCreateError } from "$api/models/ticket";
import { resolve_api } from "$api/utils/resolve";


export async function create_ticket(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    tokens: TokenPair,
    event_id: number,
    ticket: Ticket
): Promise<{ data: Ticket | null; error: TicketCreateError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/events/${event_id}/tickets/`,
        { method: 'PUT', body: JSON.stringify(ticket) },
        tokens
    );
}

