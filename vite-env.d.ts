/// <reference types="vite/client" />

declare module 'vite' {
  export function defineConfig(config: any): any;
}

interface ImportMeta {
  url: string;
}
