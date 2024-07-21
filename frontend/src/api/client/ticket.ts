import type { PaginatedList } from "$api/models/generic";
import type { Ticket, TicketCreateError, TicketListError } from "$api/models/ticket";
import { resolve_api } from "$api/utils/resolve";


export async function create_ticket(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    session: string,
    event_id: number,
    ticket: Ticket
): Promise<{ data: Ticket | null; error: TicketCreateError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/events/${event_id}/tickets/`,
        { method: 'POST', body: JSON.stringify(ticket) },
        session
    );
}

export async function list_tickets(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    event_id: number,
): Promise<{ data: PaginatedList<Ticket> | null; error: TicketListError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/events/${event_id}/tickets/`,
    );
}

