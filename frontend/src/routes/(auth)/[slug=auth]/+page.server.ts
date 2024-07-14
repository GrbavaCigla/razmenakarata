import { login } from '$api/server/login';
import { register } from '$api/server/register';
import type { Actions } from './$types';

export const actions = {
    login: async ({request, cookies, url, fetch}) => await login(request, cookies, url, fetch),
    register: async ({request, url, fetch}) => await register(request, url, fetch),
} satisfies Actions;