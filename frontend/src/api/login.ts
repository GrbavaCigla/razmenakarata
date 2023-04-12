export interface ErrorDisplay {
  username: string[];
  password: string[];
  detail: string | null;
}

export async function login(
  username: string,
  password: string
): Promise<[body: any, error: ErrorDisplay]> {
  const resp = await fetch("http://127.0.0.1:8000/api/v1/auth/token/", {
    method: "POST",
		headers: {
			"Content-Type": "application/json"
		},
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  });

  const body = await resp.json();
	const error = {
		username: body.username == null ? [] : body.username,
		password: body.password == null ? [] : body.password,
		detail: body.detail == null ? null : body.detail
	};

  if (resp.ok) {
    return [body, error];
  }

  return [null, error];
}
