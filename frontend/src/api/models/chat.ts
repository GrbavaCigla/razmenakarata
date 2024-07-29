import type { Ticket } from "./ticket"

export interface Chat {
    readonly id?: number,
    ticket: number | Ticket,
    user?: number
}

export interface ChatListError {
    detail?: string
}

export interface ChatCreateError {
    ticket?: string[],
    detail?: string
}