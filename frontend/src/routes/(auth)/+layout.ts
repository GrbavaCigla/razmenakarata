import type { LayoutLoad } from './$types';

export const load: LayoutLoad = ({ url }) => {
    return {
        action: url.pathname.split('/')[1]
    };
};