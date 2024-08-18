export interface Package {
    readonly id?: number;
    name: string,
}

export interface Event {
    readonly id?: number;
    thumbnail: URL,
    name: string,
    description: string,
    city: string,
    location: string,
    packages: Package[],
    categories: string[],
}

export interface EventListError {
    detail?: string;
}