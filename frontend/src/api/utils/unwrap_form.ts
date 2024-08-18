export function unwrap_form<T>(form: FormData): T {
    return Object.fromEntries(form.entries()) as T;
}