export type LogEvent = {
  id?: number
  session_id: number
  level: string
  message: string
  meta?: any
  timestamp?: string
}
