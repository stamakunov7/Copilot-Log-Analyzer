import { useEffect } from 'react'

export default function useWebSocketLogs(url:string, onMessage:(data:any)=>void){
  useEffect(()=>{
    const ws = new WebSocket(url)
    ws.onmessage = e => onMessage(e.data)
    return ()=> ws.close()
  }, [url])
}
