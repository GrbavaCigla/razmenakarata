import { post_chat } from '$api/server/chat';
import type { Actions } from './$types';

export const actions = {
    default: async ({ fetch, request, cookies, url }) => await post_chat(fetch, request, cookies, url),
} satisfies Actions;