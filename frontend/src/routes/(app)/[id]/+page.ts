import type { PageLoad } from "./$types";

export const load = (async ({ params }) => {
  // TODO: Add error handling
  // TODO: Unhardcode this url
  const promises = await Promise.all([
    fetch("http://127.0.0.1:8000/api/v1/events/" + params.id)
      .then((resp) => resp.json()),
    fetch("http://127.0.0.1:8000/api/v1/events/" + params.id + "/tickets")
      .then((resp) => resp.json())
      .then((resp) => resp["results"]),
  ]);

  return {
    event: promises[0],
    tickets: promises[1],
  };
}) satisfies PageLoad;
