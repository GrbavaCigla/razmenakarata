import { post_tickets } from '$api/server/post_tickets';
import type { Actions } from './$types';

export const actions = {
    default: async ({ fetch, request, cookies, url }) => await post_tickets(fetch, request, cookies, url),
} satisfies Actions;