# Build Stage
FROM node:22-alpine AS builder

WORKDIR /app

# Install dependencies using npm (faster for standard Vite setups without lockfiles yet)
COPY package.json ./
RUN npm install

# Copy application source
COPY . .

# Build Vite SPA
RUN npm run build

# Production Stage (Nginx)
FROM nginx:alpine

# Remove default nginx static assets
RUN rm -rf /usr/share/nginx/html/*

# Copy build artifacts to nginx root
COPY --from=builder /app/dist /usr/share/nginx/html

# Replace default nginx config with our SPA config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
