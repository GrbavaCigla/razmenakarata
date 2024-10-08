import { create_session } from "$api/client/auth";
import { handle_redirect } from "$api/utils/handle_redirect";
import { unwrap_form } from "$api/utils/unwrap_form";
import { fail, type Cookies } from "@sveltejs/kit";

export async function login(
    fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
    request: Request,
    cookies: Cookies,
    url: URL,
) {
    let form = unwrap_form<{ email: string, password: string }>(await request.formData());

    let { data, error } = await create_session(fetch, form.email, form.password);

    if (error || data?.auth_token == null) {
        return fail(400, error);
    }

    cookies.set('session', data.auth_token!, {
        httpOnly: true,
        path: '/',
        sameSite: 'strict',
        secure: true,
        maxAge: 60 * 60 * 24 * 7
    });

    throw handle_redirect(url);
}