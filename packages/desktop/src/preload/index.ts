import { contextBridge, ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'

contextBridge.exposeInMainWorld('electron', electronAPI)
contextBridge.exposeInMainWorld('api', {
  runPipeline: (relPath: string) => ipcRenderer.invoke('run-pipeline', relPath)
})