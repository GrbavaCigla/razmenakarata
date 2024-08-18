import { PROTECTED_ROUTES } from '$src/config';
import { authenticate_user } from '$api/utils/authenticate';
import { redirect, type Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
    if (!event.url.pathname.startsWith("/api")) {
        let { session, user } = await authenticate_user(event.cookies, event.fetch);
        event.locals.session = session;
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
