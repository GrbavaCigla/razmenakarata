import type { User, UserCreateError, UserRetrieveError } from '$api/models/user';
import { resolve_api } from '$api/utils/resolve';

export async function create_user(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	user: User
): Promise<{ data: User | null; error: UserCreateError | null }> {
	return await resolve_api(fetch, `/api/v1/users/`, {
		method: 'post',
		body: JSON.stringify(user)
	});
}

export async function retrieve_user(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	session: string
): Promise<{ data: User | null; error: UserRetrieveError | null }> {
	return await resolve_api(
		fetch,
		`/api/v1/users/me/`,
		{ method: 'get' },
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
		{ method: 'put', body: JSON.stringify(user) },
		session
	);
}
