import { activate_user } from '$api/client/user';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ fetch, params }) => {
    let { data, error } = await activate_user(fetch, params.uid, params.token);

    if (error) {
        return {
            status: "error",
            message: "Došlo je do greške pri aktivaciji.",
        };
    }

    return {
        status: "success",
        message: "Uspešno ste potvrdili svoju email adresu."
    };
};