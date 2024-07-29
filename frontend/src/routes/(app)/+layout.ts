import { list_events } from "$api/client/event";
import type { LayoutLoad } from "./$types";

export const load: LayoutLoad = async ({ fetch }) => {
    const load_events = async () => {
        let { data, error } = await list_events(fetch);

        return data?.results ?? [];
    };

    return {
        events: await load_events()
    };
};