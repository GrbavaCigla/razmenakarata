import { login } from '$api/server/login';
import { register } from '$api/server/register';
import type { Actions } from './$types';

export const actions = {
    login: async ({ fetch, request, cookies, url }) => await login(fetch, request, cookies, url,),
    register: async ({ fetch, request, url }) => await register(fetch, request, url),
} satisfies Actions;