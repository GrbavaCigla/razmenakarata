import { list_chats } from "$api/client/chat";
import { retrieve_user } from "$api/client/user";
import { map_ids } from "$api/utils/map_ids";
import type { LayoutLoad } from "./$types";

export const load: LayoutLoad = async ({ fetch, parent }) => {
    let { session } = await parent();

    const load_chats = async () => {
        let { data, error } = await list_chats(fetch, session ?? "");

        return data?.results ?? [];
    };

    let chats = await load_chats();

    let ids = chats.flatMap((chat) => chat.user ? [chat.user] : []) ?? [];

    return {
        chats: await load_chats(),
        contacts: await map_ids(
            ids,
            (id: number) => retrieve_user(fetch, id, session).then((value) => value.data)
        ),
    };
};