declare module 'vite' {
  export function defineConfig(config: any): any;
}

declare module '@vitejs/plugin-react' {
  const pluginReact: () => any;
  export default pluginReact;
}
