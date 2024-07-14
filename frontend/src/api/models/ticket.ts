export interface Ticket {
	readonly id?: number;
    price: number,
    event: number,
    amount: number,
    online: boolean,
    package?: number,
    owner: string,
}

export interface TicketCreateError {
    price?: string[],
    event?: string[],
    amount?: string[],
    online?: string[],
    package?: string[],
    owner?: string[],
	detail?: string;
}

export interface TicketRetrieveError {
	detail?: string;
}
