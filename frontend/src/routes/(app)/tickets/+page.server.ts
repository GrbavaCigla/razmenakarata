import { post_tickets } from '$api/server/post_tickets';
import type { Actions } from './$types';

export const actions = {
    default: async ({ fetch, request, cookies }) => await post_tickets(fetch, request, cookies),
} satisfies Actions;