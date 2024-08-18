import { handle_redirect } from '$api/utils/handle_redirect';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ locals, url }) => {
    if (locals.session) throw handle_redirect(url);
};