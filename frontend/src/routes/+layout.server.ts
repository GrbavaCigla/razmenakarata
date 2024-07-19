import type { ServerLoadEvent } from '@sveltejs/kit';
import type { LayoutServerLoad } from './$types';

export const trailingSlash = 'always';

export const load: LayoutServerLoad = async ({ locals }: ServerLoadEvent) => {
	return {
		user: locals.user,
		session: locals.session
	};
};
