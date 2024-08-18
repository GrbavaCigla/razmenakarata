import type { Activation, ActivationError, User, UserCreateError, UserRetrieveError } from '$api/models/user';
import { resolve_api } from '$api/utils/resolve';

export async function create_user(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    user: User
): Promise<{ data: User | null; error: UserCreateError | null }> {
    return await resolve_api(fetch, `/api/v1/users/`, {
        method: 'POST',
        body: JSON.stringify(user)
    });
}

export async function retrieve_me(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    session: string
): Promise<{ data: User | null; error: UserRetrieveError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/users/me/`,
        { method: 'GET' },
        session
    );
}

export async function retrieve_user(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    user_id: number,
    session: string
): Promise<{ data: User | null; error: UserRetrieveError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/users/${user_id}/`,
        { method: 'GET' },
        session
    );
}


export async function update_user(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    session: string,
    user: User
) {
    return await resolve_api(
        fetch,
        `/api/v1/users/me/`,
        { method: 'PUT', body: JSON.stringify(user) },
        session
    );
}


export async function activate_user(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    uid: string,
    token: string
): Promise<{ data: Activation | null; error: ActivationError | null }> {
    return await resolve_api(
        fetch,
        `/api/v1/users/activation/`,
        { method: 'POST', body: JSON.stringify({ uid: uid, token: token }) }
    );
}