import { redirect } from '@sveltejs/kit';

export function handle_redirect(url: URL, default_url: string = '/') {
	const redirectTo = url.searchParams.get('redirect');
	if (redirectTo) {
		return redirect(302, `/${redirectTo.slice(1)}`);
	}
	return redirect(302, default_url);
}
