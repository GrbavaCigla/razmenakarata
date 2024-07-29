import type { Chat, ChatCreateError, ChatListError } from "$api/models/chat";
import type { PaginatedList } from "$api/models/generic";
import { resolve_api } from "$api/utils/resolve";


export async function create_chat(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    session: string,
    ticket_id: number
): Promise<{ data: Chat | null; error: ChatCreateError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/chat/`,
        { method: 'POST', body: JSON.stringify({ "ticket": ticket_id }) },
        session
    );
}


export async function list_chats(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    session: string,
): Promise<{ data: PaginatedList<Chat> | null; error: ChatListError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/chat/`,
        { method: "GET" },
        session
    );
}
