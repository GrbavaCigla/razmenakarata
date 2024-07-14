import { PROTECTED_ROUTES } from '$src/config';
import { authenticateUser } from '$api/utils/authenticate';
import { redirect, type Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	if (!event.url.pathname.startsWith("/api")) {
		let { tokens, user } = await authenticateUser(event.cookies, event.fetch);
		event.locals.tokens = tokens;
		event.locals.user = user;
	
		for (var i of PROTECTED_ROUTES) {
			if (event.url.pathname.startsWith(i)) {
				if (!event.locals.user) {
					throw redirect(303, `/login?redirect=${event.url.pathname}`);
				}
			}
		}
	}

	const response = resolve(event);

	return response;
};
