export interface User {
    readonly id?: number;
    first_name: string;
    last_name: string;
    email: string;
    password?: string;
    re_password?: string;
}

export interface UserCreateError {
    first_name?: string[];
    last_name?: string[];
    email?: string[];
    password?: string[];
    re_password?: string[];
    detail?: string;
}

export interface UserRetrieveError {
    detail?: string;
}


export interface Activation {
    uid: string;
    token: string;
}

export interface ActivationError {
    uid?: string[];
    token?: string[];
    detail?: string;
}