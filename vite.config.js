import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/customer-prediction/', // Add this line with your subfolder name
  esbuild: {
    loader: {
      '.js': 'jsx',
      '.jsx': 'jsx'
    }
  },
  server: {
    headers: {
      'Content-Type': 'application/javascript'
    },
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})