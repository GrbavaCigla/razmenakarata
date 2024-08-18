import { destroy_session } from "$api/client/auth";
import { handle_redirect } from "$api/utils/handle_redirect";

import type { Actions } from './$types';

export const actions = {
    default: async ({ fetch, cookies, url }) => {
        let { error } = await destroy_session(fetch, cookies.get("session") ?? "");

        cookies.delete('session', { path: '/' });

        throw handle_redirect(url);
    },
} satisfies Actions;