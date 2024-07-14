export interface TokenPair {
	access?: string;
	refresh?: string;
}

export interface TokenObtainError {
	email?: string[];
	password?: string[];
	detail?: string;
}

export interface TokenRefreshError {
	refresh?: string[];
	detail?: string;
}
