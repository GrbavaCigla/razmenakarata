import type { PageLoad } from "./$types";

export const load = (async ({ params, fetch }) => {
  return {
    // TODO: Add error handling
    // TODO: Unhardcode this url
    events: await fetch("http://127.0.0.1:8000/api/v1/events/")
      .then((resp) => resp.json())
      .then((resp) => resp["results"]),
  };
}) satisfies PageLoad;
