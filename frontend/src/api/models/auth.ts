export interface Session {
	auth_token: string;
}

export interface SessionObtainError {
	email?: string[];
	password?: string[];
	detail?: string;
}

export interface SessionDestroyError {
	detail?: string;
}