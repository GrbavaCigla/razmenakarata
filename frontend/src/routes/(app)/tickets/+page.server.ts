import { post_tickets } from '$api/server/post_tickets';
import type { Actions } from './$types';

export const actions = {
    default: async ({request, fetch}) => await post_tickets(request, fetch),
} satisfies Actions;