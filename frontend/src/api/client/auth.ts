import type { TokenObtainError, TokenPair, TokenRefreshError } from '$api/models/auth';
import { resolve_api } from '$api/utils/resolve';

export async function retrieve_token(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	email: string,
	password: string
): Promise<{ data: TokenPair | null; error: TokenObtainError | null }> {
	return await resolve_api(fetch, `/api/v1/auth/token/`, {
		method: 'post',
		body: JSON.stringify({ email: email, password: password })
	});
}

export async function refresh_token(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	refresh: string
): Promise<{ data: TokenPair | null; error: TokenRefreshError | null }> {
	return await resolve_api(fetch, `/api/v1/auth/refresh/`, {
		method: 'post',
		body: JSON.stringify({ refresh: refresh })
	});
}

export async function verify_token(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	access: string
): Promise<boolean> {
	return await fetch(`/api/v1/auth/refresh/`, {
		method: 'post',
		body: JSON.stringify({ access: access })
	}).then((resp) => resp.ok);
}
