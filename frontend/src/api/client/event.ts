import type { EventListError, Event } from "$api/models/event";
import type { PaginatedList } from "$api/models/generic";
import { resolve_api } from '$api/utils/resolve';

export async function list_events(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
): Promise<{ data: PaginatedList<Event> | null; error: EventListError | null }> {
    return await resolve_api(fetch, `/api/v1/events/`);
}