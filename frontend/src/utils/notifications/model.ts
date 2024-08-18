export enum NotificationStatus {
    INFO,
    ERROR,
    WARNING,
    SUCCESS
}

export interface Notification {
    status: NotificationStatus,
    message: string,
    subtext?: string,
}