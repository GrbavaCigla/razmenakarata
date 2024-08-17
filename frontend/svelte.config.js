import adapter from "@sveltejs/adapter-auto";
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import path from "path";

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://kit.svelte.dev/docs/integrations#preprocessors
    // for more information about preprocessors
    preprocess: vitePreprocess(),

    kit: {
        adapter: adapter(),
        alias: {
            $components: path.resolve('./src/components'),
            $stores: path.resolve('./src/stores'),
            $routes: path.resolve('./src/routes'),
            $api: path.resolve('./src/api'),
            $utils: path.resolve('./src/utils'),
            $src: path.resolve('./src/'),
        }
    },
};

export default config;
