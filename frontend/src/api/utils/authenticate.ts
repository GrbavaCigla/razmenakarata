import { refresh_token } from '$api/client/auth';
import { retrieve_user } from '$api/client/user';
import type { TokenPair } from '$api/models/auth';
import type { Cookies } from '@sveltejs/kit';

export async function authenticateUser(cookies: Cookies, fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>) {
	// TODO: Refresh only when needed
	if (cookies.get('refresh')) {
		let { data, error } = await refresh_token(fetch, cookies.get('refresh')!);

		let resp = await retrieve_user(fetch, data ?? {});

		if (data) {
			return { tokens: { ...data, refresh: cookies.get('refresh')! }, user: resp.data };
		}
	}

	cookies.delete('refresh', { path: '/' });

	return { tokens: {} as TokenPair, user: null };
}
