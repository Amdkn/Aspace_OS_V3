/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone', // Requis pour une image Docker optimisée
  typescript: {
    ignoreBuildErrors: true,
  }
};

export default nextConfig;
