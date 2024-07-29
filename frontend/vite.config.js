import { sveltekit } from '@sveltejs/kit/vite';

/** @type {import('vite').UserConfig} */
const config = {
	server: {
		proxy: {
			'/api': 'http://127.0.0.1:8000/',
			'/ws': 'ws://127.0.0.1:8000/'
		}
	},
	plugins: [sveltekit()],
	envDir: '../',
	envPrefix: 'SVELTE_',
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
};

export default config;
