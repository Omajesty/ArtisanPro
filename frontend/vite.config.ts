import tailwindcss from '@tailwindcss/vite'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), tailwindcss()],
  server: {
    // In development, the browser calls /api/... on the Vite server (port 5173),
    // and Vite forwards it to FastAPI (port 8000). Same origin, so no CORS setup needed.
    proxy: {
      '/api': 'http://localhost:8000',
    },
  },
})
