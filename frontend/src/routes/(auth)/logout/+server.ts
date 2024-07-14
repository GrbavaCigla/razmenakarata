import { handle_redirect } from '$api/utils/handle_redirect';
import type { RequestHandler } from '@sveltejs/kit';

export const GET: RequestHandler = ({ cookies, url }) => {
	cookies.delete('refresh', { path: '/' });

	throw handle_redirect(url);
};
