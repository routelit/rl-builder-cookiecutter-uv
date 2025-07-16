import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'
import { fileURLToPath } from 'url';

// Get current directory in ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../{{cookiecutter.project_slug}}/static',
    emptyOutDir: true,
    manifest: true, // Generate manifest.json for asset tracking
    lib: {
      entry: path.resolve(__dirname, 'src/index.ts'),
      name: '{{cookiecutter.project_pascal_case}}',
      fileName: (format) => `{{cookiecutter.project_name}}.${format}.js`,
      formats: ['es', 'umd']
    },
    rollupOptions: {
      external: ['react', 'react-dom', 'react/jsx-runtime', 'routelit-client'],
      output: {
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
          'react/jsx-runtime': 'jsxRuntime',
          'routelit-client': 'RoutelitClient',
        }
      }
    },
    minify: true,
    sourcemap: true,
  }
})
