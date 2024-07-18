export interface Event {
	readonly id?: number;
    thumbnail: URL,
    name: string,
    description: string,
    city: string,
    location: string,
    packages: string[],
    categories: string[],
}

export interface EventListError {
	detail?: string;
}