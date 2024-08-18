// See https://kit.svelte.dev/docs/types#app
// for information about these interfaces

import type { User } from "./api/models/user";

// and what to do when importing types
declare namespace App {
    // interface Error {}
    interface Locals {
        user?: User,
        session?: string,
    }
    // interface PageData {}
    // interface Platform {}
}
