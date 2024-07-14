import type { User, UserCreateError, UserRetrieveError } from '$api/models/user';
import { resolve_api } from '$api/utils/resolve';
import type { TokenPair } from '$api/models/auth';

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
	tokens: TokenPair
): Promise<{ data: User | null; error: UserRetrieveError | null }> {
	return await resolve_api(
		fetch,
		`/api/v1/users/me/`,
		{ method: 'get' },
		tokens
	);
}

export async function update_user(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	tokens: TokenPair,
	user: User
) {
	return await resolve_api(
		fetch,
		`/api/v1/users/me/`,
		{ method: 'put', body: JSON.stringify(user) },
		tokens
	);
}
