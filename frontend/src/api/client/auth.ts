import type { Session, SessionDestroyError, SessionObtainError } from '$api/models/auth';
import { resolve_api } from '$api/utils/resolve';

export async function create_session(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	email: string,
	password: string
): Promise<{ data: Session | null; error: SessionObtainError | null }> {
	return await resolve_api(fetch, `/api/v1/auth/login/`, {
		method: 'post',
		body: JSON.stringify({ email: email, password: password })
	});
}

export async function destroy_session(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	session: string,
): Promise<{ data: null; error: SessionDestroyError | null }> {
	return await resolve_api(
		fetch,
		`/api/v1/auth/logout/`,
		{ method: 'post' },
		session,
	);
}
