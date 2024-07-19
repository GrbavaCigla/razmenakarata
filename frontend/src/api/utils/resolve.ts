export async function resolve_api<T, E>(
	fetch: (input: RequestInfo | URL, init?: RequestInit | undefined) => Promise<Response>,
	input: RequestInfo | URL,
	init?: RequestInit | undefined,
	session?: string | null
): Promise<{ data: T | null; error: E | null }> {
	async function execute(opts?: RequestInit | undefined) {
		return await fetch(input, opts)
			.then(async (resp) => {
				let text = await resp.text();
				let to_return = text == '' ? {} : JSON.parse(text);

				return resp.ok
					? { data: to_return as T, error: null }
					: { data: null, error: to_return as E };
			})
			.catch((reason) => {
				// TODO: Use reason?
				return {
					data: null,
					error: { detail: 'Something went wrong. Please try again later.', code: 'unknown_error' } as E
				};
			});
	}

	let opts: RequestInit = init == undefined ? {} : init;
	opts.headers = { 'Content-Type': 'application/json' };
	if (session)
		opts.headers = { Authorization: `Token ${session}`, ...opts.headers };

	let resp = await execute(opts);

	return resp;
}
