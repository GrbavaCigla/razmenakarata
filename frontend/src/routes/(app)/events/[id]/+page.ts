import { list_tickets } from "$api/client/ticket";
import { error } from "@sveltejs/kit";
import type { PageLoad } from "./$types";

export const load = (async ({ params, fetch, parent }) => {
  let event_id = ((await parent()).events ?? []).findIndex((event) => event.id == +params.id);

  if (event_id == -1) {
    error(404, { message: "Not found." });
  }

  // TODO: Add error handling
  const load_tickets = async () => {
    let { data, error } = await list_tickets(fetch, +params.id);

    return data?.results ?? [];
  };

  return {
    event_id: event_id,
    tickets: await load_tickets(),
  };
}) satisfies PageLoad;
